"""
Agent Orchestrator: Task Dispatch and Execution

Implements Dependency Inversion Principle—depends on SkillRegistry
abstraction, not concrete skill implementations.

Single Responsibility: This class ONLY dispatches tasks to skills
and handles execution lifecycle. Discovery, validation, and domain
logic are separate concerns.
"""

import logging
import time
from typing import Optional, Callable, Any
from contextlib import contextmanager

from .protocols import (
    AgentContext,
    AgentResult,
    ResultStatus,
    TaskPriority
)
from .registry import SkillRegistry


# ============================================================================
# Logging Configuration
# ============================================================================

logger = logging.getLogger(__name__)


# ============================================================================
# Execution Middleware Types
# ============================================================================

ExecutionMiddleware = Callable[[AgentContext, Callable], AgentResult]


# ============================================================================
# Agent Orchestrator
# ============================================================================

class AgentOrchestrator:
    """
    Dispatches tasks to skills and manages execution lifecycle.
    
    Design Principles:
    - SRP: Only responsible for orchestration and dispatch
    - OCP: Adding skills requires no changes (registry handles discovery)
    - LSP: Any skill matching protocol can substitute
    - DIP: Depends on SkillRegistry abstraction
    
    Features:
    - Execution timing and metrics
    - Middleware support for cross-cutting concerns
    - Error containment (failures don't cascade)
    - Priority-aware execution (future: resource allocation)
    """
    
    def __init__(
        self,
        registry: SkillRegistry,
        enable_timing: bool = True,
        enable_logging: bool = True
    ):
        """
        Initialize orchestrator with skill registry.
        
        Args:
            registry: SkillRegistry instance for skill lookup
            enable_timing: Add execution duration to result metadata
            enable_logging: Log all skill executions
        """
        self._registry = registry
        self._enable_timing = enable_timing
        self._enable_logging = enable_logging
        self._middleware: list[ExecutionMiddleware] = []
    
    # ========================================================================
    # Public API
    # ========================================================================
    
    def execute_task(
        self,
        skill_name: str,
        context: AgentContext
    ) -> AgentResult:
        """
        Execute a task by dispatching to the appropriate skill.
        
        This is the primary entry point for all task execution.
        
        Args:
            skill_name: Identifier of skill to execute
            context: Execution context with parameters
            
        Returns:
            AgentResult with execution outcome
            
        Error Handling:
            - Skill not found → FAILURE result
            - Invalid result type → FAILURE result
            - Exception during execution → FAILURE result with details
            - Never propagates exceptions (error containment)
        """
        if self._enable_logging:
            logger.info(
                f"⚙ Executing: {skill_name} "
                f"[priority={context.priority.value}]"
            )
        
        # Lookup skill
        skill = self._registry.get_skill(skill_name)
        
        if not skill:
            return self._create_not_found_result(skill_name)
        
        # Execute with timing and error handling
        with self._measure_execution() as timer:
            result = self._execute_with_middleware(skill, context)
        
        # Add execution metadata
        if self._enable_timing:
            result.metadata["execution_time_ms"] = timer.elapsed_ms
            result.metadata["skill_name"] = skill_name
        
        # Log result
        if self._enable_logging:
            status_symbol = "✓" if result.success else "✗"
            logger.info(
                f"{status_symbol} {skill_name}: {result.message} "
                f"({timer.elapsed_ms:.2f}ms)"
            )
        
        return result
    
    def execute_batch(
        self,
        tasks: list[tuple[str, AgentContext]]
    ) -> list[AgentResult]:
        """
        Execute multiple tasks in sequence.
        
        Future: Support parallel execution with asyncio.
        
        Args:
            tasks: List of (skill_name, context) tuples
            
        Returns:
            List of AgentResult in same order as input
        """
        results = []
        
        for skill_name, context in tasks:
            result = self.execute_task(skill_name, context)
            results.append(result)
            
            # Short-circuit on critical failures
            if (not result.success and 
                context.priority == TaskPriority.CRITICAL):
                logger.error(
                    f"⚠ Critical task failed: {skill_name}, "
                    f"aborting batch"
                )
                break
        
        return results
    
    def add_middleware(self, middleware: ExecutionMiddleware) -> None:
        """
        Register execution middleware for cross-cutting concerns.
        
        Middleware can:
        - Log requests/responses
        - Add authentication
        - Rate limit
        - Cache results
        - Transform context
        
        Example:
            def timing_middleware(context, next_handler):
                start = time.time()
                result = next_handler(context)
                result.metadata['duration'] = time.time() - start
                return result
            
            orchestrator.add_middleware(timing_middleware)
        """
        self._middleware.append(middleware)
    
    def list_available_skills(self) -> list[str]:
        """
        Get all skills available for execution.
        
        Delegates to registry (SRP).
        """
        return self._registry.list_skills()
    
    # ========================================================================
    # Execution Implementation (Private)
    # ========================================================================
    
    def _execute_with_middleware(
        self,
        skill: Callable,
        context: AgentContext
    ) -> AgentResult:
        """
        Execute skill with middleware chain and error handling.
        
        Middleware executes in FIFO order (first registered, first executed).
        """
        # Build execution chain with middleware
        def execute_skill(ctx: AgentContext) -> AgentResult:
            return self._safe_execute_skill(skill, ctx)
        
        # Wrap with middleware in reverse order (innermost first)
        handler = execute_skill
        for middleware in reversed(self._middleware):
            current_handler = handler
            handler = lambda ctx, h=current_handler, m=middleware: m(ctx, h)
        
        # Execute chain
        return handler(context)
    
    def _safe_execute_skill(
        self,
        skill: Callable,
        context: AgentContext
    ) -> AgentResult:
        """
        Execute skill with comprehensive error handling.
        
        Ensures no exceptions propagate to caller (error containment).
        """
        try:
            # Execute skill
            result = skill(context)
            
            # Validate result type
            if not isinstance(result, AgentResult):
                return AgentResult(
                    status=ResultStatus.FAILURE,
                    data=None,
                    message=(
                        f"Skill returned invalid type: {type(result).__name__}"
                    ),
                    error_details={
                        "expected_type": "AgentResult",
                        "actual_type": type(result).__name__
                    }
                )
            
            return result
            
        except Exception as e:
            # Catch all exceptions and convert to failure result
            logger.exception(f"✗ Skill execution failed with exception")
            
            return AgentResult(
                status=ResultStatus.FAILURE,
                data=None,
                message=f"Execution error: {str(e)}",
                error_details={
                    "exception_type": type(e).__name__,
                    "exception_message": str(e),
                    "traceback": self._get_exception_traceback(e)
                }
            )
    
    def _create_not_found_result(self, skill_name: str) -> AgentResult:
        """
        Create standardized result for missing skills.
        
        Includes helpful diagnostic information.
        """
        available = self._registry.list_skills()
        
        return AgentResult(
            status=ResultStatus.FAILURE,
            data=None,
            message=f"Skill not found: {skill_name}",
            metadata={
                "requested_skill": skill_name,
                "available_skills": available,
                "suggestions": self._suggest_similar_skills(
                    skill_name, 
                    available
                )
            }
        )
    
    @staticmethod
    def _suggest_similar_skills(
        skill_name: str,
        available: list[str],
        max_suggestions: int = 3
    ) -> list[str]:
        """
        Suggest similar skill names using simple string similarity.
        
        Future: Use Levenshtein distance or other fuzzy matching.
        """
        suggestions = []
        
        for candidate in available:
            # Simple substring matching
            if skill_name.lower() in candidate.lower():
                suggestions.append(candidate)
            elif candidate.lower() in skill_name.lower():
                suggestions.append(candidate)
        
        return suggestions[:max_suggestions]
    
    @staticmethod
    def _get_exception_traceback(exc: Exception) -> str:
        """
        Extract formatted traceback from exception.
        
        Useful for debugging but not included in message (too verbose).
        """
        import traceback
        return ''.join(traceback.format_exception(
            type(exc),
            exc,
            exc.__traceback__
        ))
    
    @contextmanager
    def _measure_execution(self):
        """
        Context manager for measuring execution duration.
        
        Usage:
            with self._measure_execution() as timer:
                # do work
            print(timer.elapsed_ms)
        """
        class Timer:
            def __init__(self):
                self.start = time.perf_counter()
                self.elapsed_ms = 0.0
            
            def stop(self):
                self.elapsed_ms = (time.perf_counter() - self.start) * 1000
        
        timer = Timer()
        try:
            yield timer
        finally:
            timer.stop()


# ============================================================================
# Built-in Middleware
# ============================================================================

def logging_middleware(context: AgentContext, next_handler: Callable) -> AgentResult:
    """
    Middleware that logs request and response details.
    
    Example:
        orchestrator.add_middleware(logging_middleware)
    """
    logger.debug(f"→ Request: {context.task} with params: {context.parameters}")
    result = next_handler(context)
    logger.debug(f"← Response: {result.status.value} - {result.message}")
    return result


def caching_middleware(
    cache: dict[str, AgentResult],
    cache_key_fn: Callable[[AgentContext], str] = None
):
    """
    Middleware factory that caches results.
    
    Example:
        cache = {}
        middleware = caching_middleware(cache)
        orchestrator.add_middleware(middleware)
    """
    if cache_key_fn is None:
        # Default: cache by task name and sorted parameters
        def cache_key_fn(ctx):
            params_str = str(sorted(ctx.parameters.items()))
            return f"{ctx.task}:{params_str}"
    
    def middleware(context: AgentContext, next_handler: Callable) -> AgentResult:
        key = cache_key_fn(context)
        
        if key in cache:
            logger.debug(f"⚡ Cache hit: {key}")
            return cache[key]
        
        result = next_handler(context)
        
        if result.success:
            cache[key] = result
            logger.debug(f"💾 Cached result: {key}")
        
        return result
    
    return middleware


# ============================================================================
# Factory Functions
# ============================================================================

def create_orchestrator(
    registry: SkillRegistry,
    **kwargs
) -> AgentOrchestrator:
    """
    Convenience factory for creating orchestrators.
    
    Usage:
        orchestrator = create_orchestrator(registry)
        result = orchestrator.execute_task("skill_name", context)
    """
    return AgentOrchestrator(registry, **kwargs)
