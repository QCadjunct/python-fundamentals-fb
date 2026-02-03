"""
Skill Decorators: Type-Safe Function Wrappers

This module provides decorators for common cross-cutting concerns using
TypeVar to maintain perfect type safety. Each decorator preserves the
original function's signature for IDE support and type checking.

Key Innovation: Using TypeVar with bound=Callable ensures decorators
don't break type checking while adding functionality.

Usage:
    from core.decorators import validate_context, timed, cached
    
    @timed
    @validate_context
    def execute(context: AgentContext) -> AgentResult:
        # Implementation
        pass
"""

from typing import Callable, TypeVar, Any, cast, ParamSpec
from functools import wraps
import time
import logging
from datetime import datetime, timedelta

from .protocols import AgentContext, AgentResult, ResultStatus


# ============================================================================
# Type Variables for Type-Safe Decorators
# ============================================================================

# Python 3.10+ syntax for TypeVar
F = TypeVar("F", bound=Callable[..., Any])

# ParamSpec preserves function signature (Python 3.10+)
P = ParamSpec("P")
R = TypeVar("R")


# ============================================================================
# Logging Setup
# ============================================================================

logger = logging.getLogger(__name__)


# ============================================================================
# Core Decorators
# ============================================================================

def validate_context(func: F) -> F:
    """
    Decorator that validates AgentContext before skill execution.
    
    Ensures:
    - Context is not None
    - Context is proper AgentContext instance
    - Context has required fields
    
    Returns AgentResult with validation errors instead of raising exceptions.
    
    Example:
        @validate_context
        def execute(context: AgentContext) -> AgentResult:
            # context is guaranteed valid here
            pass
    """
    
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> AgentResult:
        # Extract context from arguments
        context = None
        if args:
            context = args[0]
        elif 'context' in kwargs:
            context = kwargs['context']
        
        # Validate context exists
        if context is None:
            return AgentResult(
                status=ResultStatus.FAILURE,
                data=None,
                message="Context is required but was None",
                error_details={
                    "decorator": "validate_context",
                    "function": func.__name__
                }
            )
        
        # Validate context type
        if not isinstance(context, AgentContext):
            return AgentResult(
                status=ResultStatus.FAILURE,
                data=None,
                message=f"Expected AgentContext, got {type(context).__name__}",
                error_details={
                    "decorator": "validate_context",
                    "function": func.__name__,
                    "received_type": type(context).__name__
                }
            )
        
        # Validate required fields
        if not context.task:
            return AgentResult(
                status=ResultStatus.FAILURE,
                data=None,
                message="Context.task is required but empty",
                error_details={
                    "decorator": "validate_context",
                    "function": func.__name__
                }
            )
        
        # Context is valid, proceed with execution
        return func(*args, **kwargs)
    
    return cast(F, wrapper)


def timed(func: F) -> F:
    """
    Decorator that measures execution time and adds to result metadata.
    
    Automatically adds 'execution_time_ms' and 'execution_timestamp'
    to the AgentResult metadata.
    
    Example:
        @timed
        def execute(context: AgentContext) -> AgentResult:
            # Expensive operation
            return AgentResult(...)
        
        # Result will have metadata['execution_time_ms']
    """
    
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> AgentResult:
        start = time.perf_counter()
        start_timestamp = datetime.now().isoformat()
        
        result = func(*args, **kwargs)
        
        elapsed_ms = (time.perf_counter() - start) * 1000
        
        # Add timing metadata to result
        if isinstance(result, AgentResult):
            result.metadata["execution_time_ms"] = elapsed_ms
            result.metadata["execution_timestamp"] = start_timestamp
            result.metadata["decorated_by"] = "timed"
        
        return result
    
    return cast(F, wrapper)


def logged(func: F) -> F:
    """
    Decorator that logs skill execution with structured information.
    
    Logs:
    - Entry: Function name, context task
    - Exit: Status, execution time, message
    - Errors: Full error details
    
    Example:
        @logged
        def execute(context: AgentContext) -> AgentResult:
            return AgentResult(...)
    """
    
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> AgentResult:
        # Extract context for logging
        context = args[0] if args else kwargs.get('context')
        task_name = context.task if isinstance(context, AgentContext) else "unknown"
        
        logger.info(
            f"→ Entering {func.__name__}",
            extra={"task": task_name, "function": func.__name__}
        )
        
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        
        if isinstance(result, AgentResult):
            log_level = logging.INFO if result.success else logging.ERROR
            logger.log(
                log_level,
                f"← Exiting {func.__name__}: {result.status.value}",
                extra={
                    "task": task_name,
                    "function": func.__name__,
                    "status": result.status.value,
                    "message": result.message,
                    "execution_time_ms": elapsed_ms
                }
            )
        
        return result
    
    return cast(F, wrapper)


def cached(ttl_seconds: int = 300) -> Callable[[F], F]:
    """
    Decorator factory that caches AgentResult based on context parameters.
    
    Caches results for the specified TTL (time-to-live). Cache key is
    generated from context.task and context.parameters.
    
    Args:
        ttl_seconds: How long to cache results (default: 300 seconds)
    
    Example:
        @cached(ttl_seconds=60)
        def execute(context: AgentContext) -> AgentResult:
            # Expensive operation
            return AgentResult(...)
        
        # Second call with same params returns cached result
    """
    
    cache: dict[str, tuple[AgentResult, datetime]] = {}
    
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> AgentResult:
            # Generate cache key from context
            context = args[0] if args else kwargs.get('context')
            
            if not isinstance(context, AgentContext):
                # Can't cache without proper context
                return func(*args, **kwargs)
            
            # Create cache key from task and sorted parameters
            params_str = str(sorted(context.parameters.items()))
            cache_key = f"{context.task}:{params_str}"
            
            # Check cache
            if cache_key in cache:
                cached_result, cached_time = cache[cache_key]
                
                # Check if cache is still valid
                if datetime.now() - cached_time < timedelta(seconds=ttl_seconds):
                    logger.debug(f"⚡ Cache hit: {cache_key}")
                    
                    # Add cache metadata
                    cached_result.metadata["cache_hit"] = True
                    cached_result.metadata["cached_at"] = cached_time.isoformat()
                    
                    return cached_result
                else:
                    # Cache expired, remove it
                    del cache[cache_key]
            
            # Execute function
            result = func(*args, **kwargs)
            
            # Cache successful results only
            if isinstance(result, AgentResult) and result.success:
                cache[cache_key] = (result, datetime.now())
                result.metadata["cache_hit"] = False
                logger.debug(f"💾 Cached result: {cache_key}")
            
            return result
        
        return cast(F, wrapper)
    
    return decorator


def retry(max_attempts: int = 3, delay_seconds: float = 1.0) -> Callable[[F], F]:
    """
    Decorator factory that retries failed skill executions.
    
    Retries skills that return FAILURE status up to max_attempts times,
    with exponential backoff between attempts.
    
    Args:
        max_attempts: Maximum number of execution attempts
        delay_seconds: Initial delay between retries (exponentially increases)
    
    Example:
        @retry(max_attempts=3, delay_seconds=1.0)
        def execute(context: AgentContext) -> AgentResult:
            # Potentially flaky operation
            return AgentResult(...)
    """
    
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> AgentResult:
            last_result = None
            
            for attempt in range(1, max_attempts + 1):
                result = func(*args, **kwargs)
                
                if isinstance(result, AgentResult):
                    if result.success:
                        # Add retry metadata
                        result.metadata["retry_attempt"] = attempt
                        result.metadata["retry_needed"] = attempt > 1
                        return result
                    
                    last_result = result
                    
                    # Don't retry on last attempt
                    if attempt < max_attempts:
                        # Exponential backoff
                        wait_time = delay_seconds * (2 ** (attempt - 1))
                        logger.warning(
                            f"⚠ Attempt {attempt}/{max_attempts} failed for {func.__name__}, "
                            f"retrying in {wait_time}s..."
                        )
                        time.sleep(wait_time)
            
            # All attempts failed
            if last_result:
                last_result.metadata["retry_attempts"] = max_attempts
                last_result.metadata["all_attempts_failed"] = True
                last_result.message = (
                    f"{last_result.message} (failed after {max_attempts} attempts)"
                )
            
            return last_result
        
        return cast(F, wrapper)
    
    return decorator


def require_params(*required_params: str) -> Callable[[F], F]:
    """
    Decorator factory that validates required parameters exist in context.
    
    Checks context.parameters for required keys before executing skill.
    Returns FAILURE result if any required parameters are missing.
    
    Args:
        *required_params: Parameter names that must exist in context.parameters
    
    Example:
        @require_params('dataset', 'operation')
        def execute(context: AgentContext) -> AgentResult:
            # Guaranteed to have dataset and operation params
            dataset = context.parameters['dataset']
            operation = context.parameters['operation']
            ...
    """
    
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> AgentResult:
            # Extract context
            context = args[0] if args else kwargs.get('context')
            
            if not isinstance(context, AgentContext):
                return AgentResult(
                    status=ResultStatus.FAILURE,
                    data=None,
                    message="Invalid context for parameter validation"
                )
            
            # Check for missing parameters
            missing = [
                param for param in required_params
                if param not in context.parameters
            ]
            
            if missing:
                return AgentResult(
                    status=ResultStatus.FAILURE,
                    data=None,
                    message=f"Missing required parameters: {', '.join(missing)}",
                    error_details={
                        "decorator": "require_params",
                        "missing_params": missing,
                        "required_params": list(required_params),
                        "received_params": list(context.parameters.keys())
                    }
                )
            
            # All required params present
            return func(*args, **kwargs)
        
        return cast(F, wrapper)
    
    return decorator


def enrich_metadata(**metadata_fields: Any) -> Callable[[F], F]:
    """
    Decorator factory that adds custom metadata to AgentResult.
    
    Automatically enriches result metadata with provided key-value pairs.
    Useful for tagging skills with categories, versions, or other metadata.
    
    Args:
        **metadata_fields: Key-value pairs to add to result metadata
    
    Example:
        @enrich_metadata(skill_category='analytics', version='1.0.0')
        def execute(context: AgentContext) -> AgentResult:
            return AgentResult(...)
        
        # Result will have metadata['skill_category'] = 'analytics'
    """
    
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> AgentResult:
            result = func(*args, **kwargs)
            
            # Add metadata to result
            if isinstance(result, AgentResult):
                result.metadata.update(metadata_fields)
                result.metadata["enriched_by"] = "enrich_metadata"
            
            return result
        
        return cast(F, wrapper)
    
    return decorator


# ============================================================================
# Decorator Combinators
# ============================================================================

def standard_skill_decorators(func: F) -> F:
    """
    Meta-decorator that applies common decorator stack for skills.
    
    Applies (in order):
    1. validate_context - Ensure valid context
    2. timed - Measure execution time
    3. logged - Log execution
    
    Example:
        @standard_skill_decorators
        def execute(context: AgentContext) -> AgentResult:
            # Gets validation, timing, and logging automatically
            pass
    """
    
    return logged(timed(validate_context(func)))


# ============================================================================
# Usage Examples (for documentation)
# ============================================================================

if __name__ == "__main__":
    # Example 1: Single decorator
    @timed
    def example_skill_1(context: AgentContext) -> AgentResult:
        time.sleep(0.1)  # Simulate work
        return AgentResult(
            status=ResultStatus.SUCCESS,
            data={"result": "done"},
            message="Example 1 complete"
        )
    
    # Example 2: Stacked decorators
    @logged
    @timed
    @validate_context
    def example_skill_2(context: AgentContext) -> AgentResult:
        return AgentResult(
            status=ResultStatus.SUCCESS,
            data={"result": "done"},
            message="Example 2 complete"
        )
    
    # Example 3: Parametrized decorators
    @cached(ttl_seconds=60)
    @retry(max_attempts=3, delay_seconds=0.5)
    @require_params('dataset', 'operation')
    def example_skill_3(context: AgentContext) -> AgentResult:
        return AgentResult(
            status=ResultStatus.SUCCESS,
            data={"result": "done"},
            message="Example 3 complete"
        )
    
    # Example 4: Standard decorator stack
    @standard_skill_decorators
    def example_skill_4(context: AgentContext) -> AgentResult:
        return AgentResult(
            status=ResultStatus.SUCCESS,
            data={"result": "done"},
            message="Example 4 complete"
        )
    
    # Example 5: Custom metadata
    @enrich_metadata(skill_category='example', version='1.0.0', author='system')
    @timed
    def example_skill_5(context: AgentContext) -> AgentResult:
        return AgentResult(
            status=ResultStatus.SUCCESS,
            data={"result": "done"},
            message="Example 5 complete"
        )
    
    print("✓ All decorator examples compiled successfully")
    print("  Type safety preserved with TypeVar!")
