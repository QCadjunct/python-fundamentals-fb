"""
Core Protocols: Structural Contracts for Zero-Coupling Architecture

This module defines the behavioral contracts that skills must satisfy.
Skills need not import these protocols—they simply match the structural shape.

PEP 544: Protocol classes provide structural subtyping (static duck typing).
"""

from typing import Protocol, Any, runtime_checkable
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


# ============================================================================
# Domain Models (Pydantic v2)
# ============================================================================

class TaskPriority(str, Enum):
    """Task execution priority levels."""
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"


class AgentContext(BaseModel):
    """
    Immutable context passed to every skill execution.
    
    Using Pydantic v2 for:
    - Automatic validation
    - JSON serialization
    - Immutability (frozen=True)
    - Type coercion
    """
    
    task: str = Field(
        description="The skill/task identifier to execute"
    )
    
    parameters: dict[str, Any] = Field(
        default_factory=dict,
        description="Task-specific parameters as key-value pairs"
    )
    
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional context (user, session, timestamps, etc.)"
    )
    
    priority: TaskPriority = Field(
        default=TaskPriority.NORMAL,
        description="Execution priority for resource allocation"
    )
    
    model_config = ConfigDict(
        frozen=True,  # Immutable after creation
        validate_assignment=True,  # Validate on field updates (if unfrozen)
        extra="forbid"  # Reject unexpected fields
    )


class ResultStatus(str, Enum):
    """Standardized result status codes."""
    SUCCESS = "success"
    FAILURE = "failure"
    PARTIAL = "partial"
    SKIPPED = "skipped"


class AgentResult(BaseModel):
    """
    Standardized return value from all skill executions.
    
    Enforces consistent error handling and response structure across
    the entire agentic system.
    """
    
    status: ResultStatus = Field(
        description="Execution outcome status"
    )
    
    data: Any = Field(
        default=None,
        description="Skill-specific return data (JSON-serializable)"
    )
    
    message: str = Field(
        description="Human-readable status message"
    )
    
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional execution metadata (timing, resources, etc.)"
    )
    
    error_details: dict[str, Any] | None = Field(
        default=None,
        description="Detailed error information if status is FAILURE"
    )
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra="allow"  # Allow skills to add custom fields
    )
    
    @property
    def success(self) -> bool:
        """Convenience property for boolean success check."""
        return self.status in (ResultStatus.SUCCESS, ResultStatus.PARTIAL)


# ============================================================================
# Protocol Definitions (Structural Contracts)
# ============================================================================

@runtime_checkable
class AgentSkill(Protocol):
    """
    Primary structural contract for synchronous agentic skills.
    
    Any function matching this signature satisfies the contract WITHOUT
    needing to explicitly inherit from this Protocol class.
    
    The @runtime_checkable decorator enables isinstance() checks, though
    the primary value is static type checking via mypy/pyright.
    
    Example:
        def execute(context: AgentContext) -> AgentResult:
            # Implementation here
            pass
        
        # This function satisfies AgentSkill protocol structurally
    """
    
    def execute(self, context: AgentContext) -> AgentResult:
        """
        Execute the skill with provided context.
        
        Args:
            context: Immutable execution context with task parameters
            
        Returns:
            AgentResult containing execution outcome and data
            
        Raises:
            Should NOT raise exceptions—failures should return
            AgentResult with status=FAILURE and error_details populated.
        """
        ...


@runtime_checkable
class AsyncAgentSkill(Protocol):
    """
    Structural contract for asynchronous agentic skills.
    
    Use for I/O-bound operations (API calls, database queries, file operations).
    """
    
    async def execute(self, context: AgentContext) -> AgentResult:
        """Async variant of skill execution."""
        ...


@runtime_checkable  
class StreamingAgentSkill(Protocol):
    """
    Structural contract for streaming/chunked response skills.
    
    Use for LLM streaming, real-time data processing, or large file handling.
    """
    
    async def execute_stream(
        self, 
        context: AgentContext
    ) -> AsyncIterator[AgentResult]:
        """
        Execute skill and yield incremental results.
        
        Yields:
            AgentResult chunks as they become available
        """
        ...


@runtime_checkable
class ValidatableSkill(Protocol):
    """
    Optional protocol for skills that support pre-execution validation.
    
    Skills implementing this protocol can have their parameters validated
    before actual execution (fail-fast principle).
    """
    
    def validate(self, context: AgentContext) -> AgentResult:
        """
        Validate context parameters without executing the skill.
        
        Returns:
            AgentResult with status=SUCCESS if valid, FAILURE otherwise
        """
        ...


@runtime_checkable
class SkillMetadata(Protocol):
    """
    Optional protocol for skills that expose metadata for discovery/documentation.
    
    Enables auto-generation of CLI help, API documentation, etc.
    """
    
    def get_metadata(self) -> dict[str, Any]:
        """
        Return skill metadata for documentation/discovery.
        
        Expected keys (all optional):
            - description: str
            - parameters: dict[str, dict]  # Parameter schemas
            - examples: list[dict]  # Usage examples
            - tags: list[str]  # Categorization tags
            - version: str
            - author: str
        """
        ...


# ============================================================================
# Helper Types
# ============================================================================

from typing import Callable, Awaitable

# Type aliases for common skill function signatures
SyncSkillFunc = Callable[[AgentContext], AgentResult]
AsyncSkillFunc = Callable[[AgentContext], Awaitable[AgentResult]]


# ============================================================================
# Validation Utilities
# ============================================================================

def is_valid_skill_signature(func: Callable) -> bool:
    """
    Runtime check if a function matches AgentSkill protocol signature.
    
    This is used during auto-discovery to validate skills before registration.
    
    Args:
        func: Function to validate
        
    Returns:
        True if function signature matches protocol
    """
    import inspect
    
    # Must be callable
    if not callable(func):
        return False
    
    # Get signature
    try:
        sig = inspect.signature(func)
    except (ValueError, TypeError):
        return False
    
    # Must accept exactly one positional argument
    params = [p for p in sig.parameters.values() 
              if p.kind in (inspect.Parameter.POSITIONAL_OR_KEYWORD,
                           inspect.Parameter.POSITIONAL_ONLY)]
    
    if len(params) != 1:
        return False
    
    # Parameter should be annotated as AgentContext (if annotated)
    param = params[0]
    if param.annotation not in (inspect.Parameter.empty, AgentContext):
        return False
    
    # Return type should be AgentResult (if annotated)
    if sig.return_annotation not in (inspect.Signature.empty, AgentResult):
        return False
    
    return True


def validate_skill_result(result: Any) -> bool:
    """
    Runtime check if a value matches AgentResult structure.
    
    Args:
        result: Value to validate
        
    Returns:
        True if result is a valid AgentResult
    """
    return isinstance(result, AgentResult)
