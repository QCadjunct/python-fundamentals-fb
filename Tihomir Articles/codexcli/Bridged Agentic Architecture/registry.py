"""
Skill Registry: Auto-Discovery via Reflection

Implements the Open/Closed Principle—new skills are added by creating
files in the skills directory without modifying this code.

Single Responsibility: This class ONLY discovers and registers skills.
Validation, execution, and orchestration are separate concerns.
"""

import inspect
import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Callable, Dict, List
import logging
from dataclasses import dataclass

from .protocols import (
    AgentContext, 
    AgentResult, 
    AgentSkill,
    SyncSkillFunc,
    is_valid_skill_signature
)


# ============================================================================
# Logging Configuration
# ============================================================================

logger = logging.getLogger(__name__)


# ============================================================================
# Domain Models
# ============================================================================

@dataclass(frozen=True)
class SkillInfo:
    """
    Metadata about a registered skill.
    
    Immutable record of skill discovery for introspection.
    """
    name: str
    module_path: Path
    function: Callable
    signature: inspect.Signature
    docstring: str | None
    
    def __repr__(self) -> str:
        return f"SkillInfo(name={self.name}, path={self.module_path.name})"


# ============================================================================
# Skill Registry with Auto-Discovery
# ============================================================================

class SkillRegistry:
    """
    Auto-discovers and registers skills via module introspection.
    
    Design Principles:
    - SRP: Only responsible for discovery and registration
    - OCP: Adding skills requires no code changes here
    - DIP: Depends on Protocol abstraction, not concrete implementations
    
    Performance:
    - O(N) initialization where N = number of skill files
    - O(1) lookup after initialization
    - Skills loaded lazily to reduce startup time
    """
    
    def __init__(
        self, 
        skills_dir: Path | str,
        naming_convention: str = "execute",
        eager_load: bool = True
    ):
        """
        Initialize registry and discover skills.
        
        Args:
            skills_dir: Directory containing skill modules
            naming_convention: Expected function name in skill modules
            eager_load: If True, import all modules at init (fail-fast)
                       If False, import modules on first use (lazy)
        """
        self.skills_dir = Path(skills_dir)
        self.naming_convention = naming_convention
        self._skills: Dict[str, SkillInfo] = {}
        self._load_errors: Dict[str, Exception] = {}
        
        if not self.skills_dir.exists():
            raise FileNotFoundError(
                f"Skills directory not found: {self.skills_dir}"
            )
        
        if eager_load:
            self._discover_all_skills()
    
    # ========================================================================
    # Public API
    # ========================================================================
    
    def get_skill(self, name: str) -> SyncSkillFunc | None:
        """
        Retrieve skill function by name.
        
        Returns:
            Skill function if found, None otherwise
            
        Performance: O(1) dictionary lookup
        """
        skill_info = self._skills.get(name)
        return skill_info.function if skill_info else None
    
    def list_skills(self) -> List[str]:
        """
        Get all registered skill names.
        
        Returns:
            Sorted list of skill identifiers
        """
        return sorted(self._skills.keys())
    
    def get_skill_info(self, name: str) -> SkillInfo | None:
        """
        Get detailed metadata about a skill.
        
        Useful for generating documentation or CLI help.
        """
        return self._skills.get(name)
    
    def reload_skill(self, name: str) -> bool:
        """
        Reload a single skill from disk (for development).
        
        Returns:
            True if reload successful, False otherwise
        """
        skill_info = self._skills.get(name)
        if not skill_info:
            logger.warning(f"Cannot reload unknown skill: {name}")
            return False
        
        try:
            module = self._load_module(skill_info.module_path)
            self._register_module_skills(module)
            logger.info(f"✓ Reloaded skill: {name}")
            return True
        except Exception as e:
            logger.error(f"✗ Failed to reload {name}: {e}")
            self._load_errors[name] = e
            return False
    
    def get_load_errors(self) -> Dict[str, Exception]:
        """
        Get skills that failed to load during discovery.
        
        Useful for debugging configuration issues.
        """
        return self._load_errors.copy()
    
    # ========================================================================
    # Discovery Implementation (Private)
    # ========================================================================
    
    def _discover_all_skills(self) -> None:
        """
        Walk skills directory and register all valid skills.
        
        Convention:
        - Python files (*.py) in skills_dir
        - Ignore files starting with underscore
        - Must contain function named self.naming_convention
        - Function must match AgentSkill protocol signature
        """
        logger.info(f"🔍 Discovering skills in: {self.skills_dir}")
        
        skill_files = list(self.skills_dir.glob("*.py"))
        
        if not skill_files:
            logger.warning(f"⚠ No skill files found in {self.skills_dir}")
            return
        
        for skill_file in skill_files:
            # Skip private modules
            if skill_file.stem.startswith("_"):
                logger.debug(f"⊝ Skipping private module: {skill_file.name}")
                continue
            
            try:
                module = self._load_module(skill_file)
                self._register_module_skills(module)
                
            except Exception as e:
                logger.error(f"✗ Failed to load {skill_file.name}: {e}")
                self._load_errors[skill_file.stem] = e
        
        logger.info(
            f"✓ Registered {len(self._skills)} skills, "
            f"{len(self._load_errors)} errors"
        )
    
    def _load_module(self, path: Path) -> ModuleType:
        """
        Dynamically import a Python module from filesystem path.
        
        Uses importlib to avoid sys.path pollution.
        
        Args:
            path: Absolute path to .py file
            
        Returns:
            Loaded module object
            
        Raises:
            ImportError: If module cannot be loaded
        """
        module_name = path.stem
        
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Could not load module spec from {path}")
        
        module = importlib.util.module_from_spec(spec)
        
        # Execute module code
        spec.loader.exec_module(module)
        
        # Store reference to prevent garbage collection
        # (Important for modules with side effects)
        module.__file__ = str(path)
        
        return module
    
    def _register_module_skills(self, module: ModuleType) -> None:
        """
        Inspect module and register all valid skill functions.
        
        Validation:
        1. Function name matches convention
        2. Signature matches AgentSkill protocol
        3. Not already registered (prevents duplicates)
        
        Args:
            module: Imported Python module to inspect
        """
        module_path = Path(module.__file__)
        
        # Get all functions in module
        functions = inspect.getmembers(module, inspect.isfunction)
        
        found_skill = False
        for func_name, func in functions:
            if func_name != self.naming_convention:
                continue
            
            # Validate signature
            if not self._validate_skill_signature(func, module_path):
                continue
            
            # Register skill
            skill_name = module_path.stem
            skill_info = SkillInfo(
                name=skill_name,
                module_path=module_path,
                function=func,
                signature=inspect.signature(func),
                docstring=inspect.getdoc(func)
            )
            
            self._skills[skill_name] = skill_info
            logger.info(f"✓ Registered: {skill_name}")
            found_skill = True
        
        if not found_skill:
            logger.warning(
                f"⚠ No '{self.naming_convention}' function found in "
                f"{module_path.name}"
            )
    
    def _validate_skill_signature(
        self, 
        func: Callable,
        module_path: Path
    ) -> bool:
        """
        Validate function matches AgentSkill protocol.
        
        Fail-fast principle: Catch configuration errors at startup,
        not during execution.
        
        Args:
            func: Function to validate
            module_path: Path for error reporting
            
        Returns:
            True if valid, False otherwise (with logged warnings)
        """
        if not is_valid_skill_signature(func):
            logger.warning(
                f"⚠ Invalid signature in {module_path.name}::{func.__name__}\n"
                f"   Expected: execute(context: AgentContext) -> AgentResult"
            )
            return False
        
        # Additional checks (optional but recommended)
        sig = inspect.signature(func)
        
        # Check return annotation
        if sig.return_annotation is inspect.Signature.empty:
            logger.info(
                f"ℹ Missing return type hint in {module_path.name}::{func.__name__}\n"
                f"   Consider adding: -> AgentResult"
            )
        
        # Check parameter annotation
        param = list(sig.parameters.values())[0]
        if param.annotation is inspect.Parameter.empty:
            logger.info(
                f"ℹ Missing parameter type hint in {module_path.name}::{func.__name__}\n"
                f"   Consider adding: context: AgentContext"
            )
        
        return True


# ============================================================================
# Factory Functions
# ============================================================================

def create_registry(
    skills_dir: Path | str = "./skills",
    **kwargs
) -> SkillRegistry:
    """
    Convenience factory for creating skill registries.
    
    Usage:
        registry = create_registry("./my_skills")
        skill = registry.get_skill("analyze_data")
    """
    return SkillRegistry(skills_dir, **kwargs)
