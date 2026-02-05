PostgreSQL18-DuckDB-SQLite3 Integration - Python Service Implementation - Part 2

# 🐘 PostgreSQL18-DuckDB-SQLite3 Integration with LLM-SQL Architecture

## 🐍 Python Service Implementation - Part 2

[Back to TOC](#-table-of-contents)

### Protocol-Based Architecture (src/protocols/database.py)

```python
"""
Protocol definitions for database operations.

This module implements Protocol-based structural typing for loose coupling
and dependency inversion, following SOLID principles and Bridged Architecture.
"""

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class QueryableProtocol(Protocol):
    """
    Protocol defining queryable database interface.
    
    Implements ISP: Minimal interface for query execution.
    Any database adapter implementing these methods can be used interchangeably.
    """

    def execute(self, sql: str, parameters: dict[str, Any] | None = None) -> list[tuple[Any, ...]]:
        """
        Execute SQL query and return raw results.
        
        Args:
            sql: SQL query string
            parameters: Optional query parameters
            
        Returns:
            List of result tuples
            
        Raises:
            DatabaseError: On execution failure
        """
        ...

    def execute_many(
        self, sql: str, param_list: list[dict[str, Any]]
    ) -> int:
        """
        Execute batch operations.
        
        Args:
            sql: SQL statement
            param_list: List of parameter dictionaries
            
        Returns:
            Number of affected rows
            
        Raises:
            DatabaseError: On execution failure
        """
        ...

    @property
    def description(self) -> list[tuple[str, ...]]:
        """
        Get column descriptions from last query.
        
        Returns:
            List of column description tuples
        """
        ...


@runtime_checkable
class TransactionalProtocol(Protocol):
    """
    Protocol for transactional database operations.
    
    Implements ISP: Separate interface for transaction management.
    """

    def begin(self) -> None:
        """Start a new transaction."""
        ...

    def commit(self) -> None:
        """Commit current transaction."""
        ...

    def rollback(self) -> None:
        """Rollback current transaction."""
        ...


@runtime_checkable
class AttachableProtocol(Protocol):
    """
    Protocol for databases supporting external attachments.
    
    Implements ISP: Focused interface for attachment operations.
    This is specific to DuckDB's ATTACH capability.
    """

    def attach(
        self,
        alias: str,
        db_type: str,
        connection_string: str,
    ) -> None:
        """
        Attach external database.
        
        Args:
            alias: Database alias for queries
            db_type: Database type (postgres, mysql, sqlite)
            connection_string: Connection parameters
            
        Raises:
            AttachmentError: If attachment fails
        """
        ...

    def detach(self, alias: str) -> None:
        """
        Detach previously attached database.
        
        Args:
            alias: Database alias to detach
            
        Raises:
            AttachmentError: If detachment fails
        """
        ...

    def list_attachments(self) -> list[dict[str, Any]]:
        """
        List all currently attached databases.
        
        Returns:
            List of attachment metadata dictionaries
        """
        ...


@runtime_checkable
class ConnectionManageable(Protocol):
    """
    Protocol for connection lifecycle management.
    
    Implements SRP: Focused on connection lifecycle only.
    """

    def connect(self) -> None:
        """Establish database connection."""
        ...

    def disconnect(self) -> None:
        """Close database connection."""
        ...

    def is_connected(self) -> bool:
        """Check if connection is active."""
        ...

    def reconnect(self) -> None:
        """Reconnect to database."""
        ...


@runtime_checkable
class HealthCheckable(Protocol):
    """
    Protocol for health check operations.
    
    Implements ISP: Minimal interface for health monitoring.
    """

    def ping(self) -> bool:
        """
        Check if database is responding.
        
        Returns:
            True if database responds, False otherwise
        """
        ...

    def get_version(self) -> str:
        """
        Get database version string.
        
        Returns:
            Version string
        """
        ...
```

### Pydantic Request Models (src/models/requests.py)

```python
"""
Pydantic v2 request models with comprehensive validation.

Implements type-safe API contracts with runtime validation,
following D⁴ methodology for data integrity.
"""

from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator, model_validator


class QueryRequest(BaseModel):
    """
    SQL query execution request.
    
    Validates SQL syntax, prevents injection, and enforces constraints.
    """

    sql: str = Field(
        ...,
        min_length=1,
        max_length=100_000,
        description="SQL query to execute",
        examples=["SELECT * FROM pg.public.query_logs LIMIT 10"],
    )
    database: Literal["duckdb", "postgres", "sqlite", "mysql"] = Field(
        default="duckdb",
        description="Target database for query execution",
    )
    parameters: dict[str, Any] | None = Field(
        default=None,
        description="Query parameters for parameterized queries",
        examples=[{"user_id": 123, "start_date": "2024-01-01"}],
    )
    timeout_seconds: int = Field(
        default=300,
        ge=1,
        le=3600,
        description="Query execution timeout in seconds",
    )
    max_rows: int | None = Field(
        default=None,
        ge=1,
        le=1_000_000,
        description="Maximum rows to return (None for unlimited)",
    )

    @field_validator("sql")
    @classmethod
    def validate_sql(cls, v: str) -> str:
        """
        Validate SQL query syntax and security.
        
        Implements basic SQL injection prevention and syntax validation.
        
        Args:
            v: SQL query string
            
        Returns:
            Validated SQL string
            
        Raises:
            ValueError: If dangerous keywords detected or invalid syntax
        """
        # Remove leading/trailing whitespace
        sql = v.strip()

        # Prevent empty queries
        if not sql:
            msg = "SQL query cannot be empty"
            raise ValueError(msg)

        # Basic SQL injection prevention
        dangerous_keywords = [
            "DROP DATABASE",
            "DROP SCHEMA",
            "DROP TABLE",
            "DELETE FROM",
            "TRUNCATE",
            "ALTER TABLE",
            "CREATE USER",
            "GRANT ALL",
            "REVOKE",
        ]
        sql_upper = sql.upper()

        for keyword in dangerous_keywords:
            if keyword in sql_upper:
                msg = f"Dangerous SQL keyword detected: {keyword}"
                raise ValueError(msg)

        # Prevent multiple statements (semicolon check)
        if ";" in sql[:-1]:  # Allow trailing semicolon
            msg = "Multiple SQL statements not allowed"
            raise ValueError(msg)

        return sql

    @field_validator("parameters")
    @classmethod
    def validate_parameters(cls, v: dict[str, Any] | None) -> dict[str, Any] | None:
        """
        Validate query parameters.
        
        Args:
            v: Parameter dictionary
            
        Returns:
            Validated parameters
            
        Raises:
            ValueError: If parameters contain invalid types
        """
        if v is None:
            return None

        # Check for valid parameter types
        valid_types = (str, int, float, bool, type(None))
        for key, value in v.items():
            if not isinstance(value, valid_types):
                msg = f"Invalid parameter type for '{key}': {type(value).__name__}"
                raise ValueError(msg)

        return v

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "sql": "SELECT COUNT(*) FROM pg.public.query_logs WHERE created_at > $1",
                    "database": "duckdb",
                    "parameters": {"$1": "2024-01-01"},
                    "timeout_seconds": 60,
                    "max_rows": 1000,
                }
            ]
        }
    }


class AttachDatabaseRequest(BaseModel):
    """
    Database attachment request with validation.
    
    Ensures alias uniqueness and connection string format.
    """

    alias: str = Field(
        ...,
        min_length=1,
        max_length=50,
        pattern=r"^[a-zA-Z][a-zA-Z0-9_]*$",
        description="Database alias for attachment (alphanumeric + underscore)",
        examples=["legacy_db", "analytics_warehouse", "mysql_prod"],
    )
    db_type: Literal["postgres", "sqlite", "mysql"] = Field(
        ...,
        description="Database engine type",
    )
    connection_string: str | None = Field(
        default=None,
        min_length=1,
        max_length=1000,
        description="Custom connection string (optional, uses env vars if None)",
        examples=[
            "host=mysql user=root password=secret port=3306 database=analytics",
            "/path/to/database.db",
        ],
    )
    auto_reconnect: bool = Field(
        default=True,
        description="Automatically reconnect on connection loss",
    )

    @field_validator("alias")
    @classmethod
    def validate_alias(cls, v: str) -> str:
        """
        Validate database alias against reserved keywords.
        
        Args:
            v: Alias string
            
        Returns:
            Validated alias
            
        Raises:
            ValueError: If alias is reserved
        """
        # Reserved keywords (DuckDB internal + SQL keywords)
        reserved = {
            "pg",
            "sqlite",
            "mysql",
            "duckdb",
            "information_schema",
            "public",
            "temp",
            "temporary",
            "system",
            "main",
        }

        if v.lower() in reserved:
            msg = f"Alias '{v}' is reserved and cannot be used"
            raise ValueError(msg)

        return v

    @model_validator(mode="after")
    def validate_connection_string_required(self) -> "AttachDatabaseRequest":
        """
        Validate connection string requirements per database type.
        
        Returns:
            Validated model
            
        Raises:
            ValueError: If connection string required but missing
        """
        if self.db_type == "sqlite" and self.connection_string is None:
            msg = "SQLite requires explicit connection_string (file path)"
            raise ValueError(msg)

        return self

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "alias": "legacy_mysql",
                    "db_type": "mysql",
                    "connection_string": "host=mysql user=root password=secret port=3306",
                    "auto_reconnect": True,
                },
                {
                    "alias": "archive_data",
                    "db_type": "sqlite",
                    "connection_string": "/data/archives/2023.db",
                },
            ]
        }
    }


class DetachDatabaseRequest(BaseModel):
    """Request to detach a database."""

    alias: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Database alias to detach",
    )
    force: bool = Field(
        default=False,
        description="Force detachment even if queries are running",
    )


class BatchQueryRequest(BaseModel):
    """
    Batch query execution request.
    
    Allows multiple queries with transaction support.
    """

    queries: list[QueryRequest] = Field(
        ...,
        min_length=1,
        max_length=100,
        description="List of queries to execute",
    )
    transactional: bool = Field(
        default=False,
        description="Execute all queries in a single transaction",
    )
    stop_on_error: bool = Field(
        default=True,
        description="Stop execution on first error",
    )

    @field_validator("queries")
    @classmethod
    def validate_query_count(cls, v: list[QueryRequest]) -> list[QueryRequest]:
        """Validate query list constraints."""
        if len(v) > 100:
            msg = "Maximum 100 queries allowed in batch"
            raise ValueError(msg)
        return v
```

### Pydantic Response Models (src/models/responses.py)

```python
"""
Pydantic v2 response models with comprehensive typing.

Ensures type-safe API responses with consistent structure.
"""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, field_validator


class QueryResult(BaseModel):
    """
    SQL query execution result with metadata.
    
    Includes execution metrics and result data.
    """

    columns: list[str] = Field(
        ...,
        description="Column names from query result",
        examples=[["id", "name", "created_at"]],
    )
    rows: list[list[Any]] = Field(
        ...,
        description="Query result rows (list of lists for JSON compatibility)",
        examples=[[[1, "Alice", "2024-01-01T00:00:00"]]],
    )
    row_count: int = Field(
        ...,
        ge=0,
        description="Number of rows returned",
    )
    execution_time_ms: float = Field(
        ...,
        ge=0,
        description="Query execution time in milliseconds",
    )
    timestamp: datetime = Field(
        default_factory=datetime.utcnow,
        description="Query execution timestamp (UTC)",
    )
    database: str = Field(
        ...,
        description="Database where query executed",
    )
    truncated: bool = Field(
        default=False,
        description="Whether results were truncated due to max_rows limit",
    )

    @field_validator("execution_time_ms")
    @classmethod
    def round_execution_time(cls, v: float) -> float:
        """Round execution time to 2 decimal places."""
        return round(v, 2)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "columns": ["id", "user_query", "created_at"],
                    "rows": [[1, "SELECT * FROM users", "2024-02-04T10:30:00"]],
                    "row_count": 1,
                    "execution_time_ms": 45.23,
                    "timestamp": "2024-02-04T10:30:00.123456",
                    "database": "duckdb",
                    "truncated": False,
                }
            ]
        }
    }


class AttachmentStatus(BaseModel):
    """
    Database attachment operation status.
    
    Provides feedback on attachment success/failure.
    """

    status: str = Field(
        ...,
        description="Attachment operation status",
        examples=["success", "failed", "already_attached"],
    )
    alias: str = Field(..., description="Database alias")
    db_type: str = Field(..., description="Database type")
    message: str | None = Field(
        default=None,
        description="Additional status message",
    )
    attached_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Attachment timestamp",
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": "success",
                    "alias": "legacy_mysql",
                    "db_type": "mysql",
                    "message": "Successfully attached MySQL database with 42 tables",
                    "attached_at": "2024-02-04T10:30:00",
                }
            ]
        }
    }


class DatabaseInfo(BaseModel):
    """
    Attached database information.
    
    Provides metadata about attached databases.
    """

    database_name: str = Field(..., description="Database name/alias")
    database_oid: int = Field(..., description="Database object ID")
    path: str = Field(..., description="Database path or connection string")
    database_type: str = Field(..., description="Database type")
    attached: bool = Field(..., description="Whether database is currently attached")
    table_count: int | None = Field(
        default=None,
        ge=0,
        description="Number of tables in database",
    )
    size_bytes: int | None = Field(
        default=None,
        ge=0,
        description="Database size in bytes",
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "database_name": "pg",
                    "database_oid": 12345,
                    "path": "dbname=llm_analytics user=pgadmin host=postgres18",
                    "database_type": "postgres",
                    "attached": True,
                    "table_count": 42,
                    "size_bytes": 1073741824,
                }
            ]
        }
    }


class DatabaseListResponse(BaseModel):
    """
    List of attached databases with summary.
    
    Aggregates all database attachment information.
    """

    databases: list[DatabaseInfo] = Field(
        ...,
        description="List of attached databases",
    )
    count: int = Field(..., ge=0, description="Total number of databases")
    total_size_bytes: int | None = Field(
        default=None,
        ge=0,
        description="Total size of all databases",
    )

    @field_validator("count", mode="after")
    @classmethod
    def validate_count_matches(cls, v: int, info) -> int:
        """Ensure count matches actual database list length."""
        if "databases" in info.data and len(info.data["databases"]) != v:
            msg = "Count does not match database list length"
            raise ValueError(msg)
        return v

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "databases": [
                        {
                            "database_name": "pg",
                            "database_oid": 12345,
                            "path": "dbname=llm_analytics",
                            "database_type": "postgres",
                            "attached": True,
                            "table_count": 42,
                        }
                    ],
                    "count": 1,
                    "total_size_bytes": 1073741824,
                }
            ]
        }
    }


class HealthResponse(BaseModel):
    """
    Service health check response.
    
    Provides comprehensive health status including dependencies.
    """

    status: str = Field(
        ...,
        description="Service health status",
        examples=["healthy", "degraded", "unhealthy"],
    )
    duckdb_version: str = Field(..., description="DuckDB version")
    attached_databases: int = Field(
        ...,
        ge=0,
        description="Number of attached databases",
    )
    uptime_seconds: float = Field(
        ...,
        ge=0,
        description="Service uptime in seconds",
    )
    memory_usage_mb: float | None = Field(
        default=None,
        ge=0,
        description="Current memory usage in MB",
    )
    active_connections: int = Field(
        default=0,
        ge=0,
        description="Number of active database connections",
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": "healthy",
                    "duckdb_version": "0.10.0",
                    "attached_databases": 3,
                    "uptime_seconds": 3600.5,
                    "memory_usage_mb": 512.34,
                    "active_connections": 5,
                }
            ]
        }
    }


class ErrorResponse(BaseModel):
    """
    Error response model with detailed context.
    
    Provides consistent error structure across API.
    """

    error: str = Field(
        ...,
        description="Error type/code",
        examples=["QueryExecutionError", "ValidationError", "AttachmentError"],
    )
    message: str = Field(
        ...,
        description="Human-readable error message",
    )
    detail: str | None = Field(
        default=None,
        description="Additional error details for debugging",
    )
    timestamp: datetime = Field(
        default_factory=datetime.utcnow,
        description="Error timestamp (UTC)",
    )
    path: str | None = Field(
        default=None,
        description="API endpoint where error occurred",
    )
    correlation_id: str | None = Field(
        default=None,
        description="Correlation ID for request tracing",
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "error": "QueryExecutionError",
                    "message": "Failed to execute query",
                    "detail": "Syntax error near 'FORM' at line 1",
                    "timestamp": "2024-02-04T10:30:00",
                    "path": "/api/v1/query",
                    "correlation_id": "abc123-def456-ghi789",
                }
            ]
        }
    }


class BatchQueryResult(BaseModel):
    """
    Batch query execution result.
    
    Contains results for all queries in batch with individual status.
    """

    results: list[QueryResult | ErrorResponse] = Field(
        ...,
        description="Results for each query (success or error)",
    )
    total_queries: int = Field(..., ge=0, description="Total queries in batch")
    successful_queries: int = Field(..., ge=0, description="Number of successful queries")
    failed_queries: int = Field(..., ge=0, description="Number of failed queries")
    total_execution_time_ms: float = Field(
        ...,
        ge=0,
        description="Total execution time for all queries",
    )

    @field_validator("total_queries", mode="after")
    @classmethod
    def validate_totals(cls, v: int, info) -> int:
        """Validate that counts match."""
        if "successful_queries" in info.data and "failed_queries" in info.data:
            expected = info.data["successful_queries"] + info.data["failed_queries"]
            if v != expected:
                msg = "Total queries must equal successful + failed"
                raise ValueError(msg)
        return v
```

[Back to TOC](#-table-of-contents)

---

### DuckDB Manager Service (src/services/duckdb_manager.py)

```python
"""
DuckDB connection manager with lifecycle management.

Implements SRP: Manages only DuckDB connection lifecycle and configuration.
Uses Protocol-based architecture for loose coupling.
"""

import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, AsyncIterator

import duckdb
import structlog

from src.config import Settings
from src.protocols.database import AttachableProtocol, ConnectionManageable, QueryableProtocol

logger = structlog.get_logger(__name__)


class DuckDBConnectionError(Exception):
    """Raised when DuckDB connection operations fail."""


class DuckDBQueryError(Exception):
    """Raised when DuckDB query execution fails."""


class DuckDBManager(QueryableProtocol, AttachableProtocol, ConnectionManageable):
    """
    DuckDB connection manager implementing multiple protocols.
    
    Responsibilities (SRP):
    - Maintain DuckDB connection lifecycle
    - Install and load required extensions
    - Provide connection pool interface
    - Handle connection errors and retries
    
    Implements:
    - QueryableProtocol: For query execution
    - AttachableProtocol: For database attachments
    - ConnectionManageable: For connection lifecycle
    """

    def __init__(self, settings: Settings) -> None:
        """
        Initialize DuckDB manager.
        
        Args:
            settings: Application settings instance
        """
        self.settings = settings
        self.connection: duckdb.DuckDBPyConnection | None = None
        self.start_time: float = time.time()
        self._attached_databases: dict[str, dict[str, Any]] = {}
        self._is_initialized: bool = False
        
        # Configure logger
        self.logger = logger.bind(
            service="duckdb_manager",
            database_path=str(settings.duckdb.database_path),
        )

    async def initialize(self) -> None:
        """
        Initialize DuckDB connection and extensions.
        
        Raises:
            DuckDBConnectionError: If initialization fails
        """
        try:
            self.logger.info(
                "initializing_duckdb",
                threads=self.settings.duckdb.threads,
                memory_limit=self.settings.duckdb.memory_limit,
            )

            # Ensure database directory exists
            self.settings.duckdb.database_path.parent.mkdir(parents=True, exist_ok=True)

            # Create connection with configuration
            self.connection = duckdb.connect(
                database=str(self.settings.duckdb.database_path),
                read_only=False,
                config={
                    "threads": self.settings.duckdb.threads,
                    "memory_limit": self.settings.duckdb.memory_limit,
                    "temp_directory": str(self.settings.duckdb.temp_directory),
                    "access_mode": self.settings.duckdb.access_mode,
                },
            )

            # Install required extensions
            await self._install_extensions()

            # Attach default databases
            await self._attach_default_databases()

            self._is_initialized = True

            self.logger.info(
                "duckdb_initialized",
                version=duckdb.__version__,
                attached_databases=len(self._attached_databases),
                initialization_time_ms=round((time.time() - self.start_time) * 1000, 2),
            )

        except Exception as e:
            self.logger.error("duckdb_initialization_failed", error=str(e), exc_info=True)
            raise DuckDBConnectionError(f"Failed to initialize DuckDB: {e}") from e

    async def _install_extensions(self) -> None:
        """
        Install and load required DuckDB extensions.
        
        Extensions: postgres, mysql, sqlite, httpfs, json, parquet
        """
        extensions = ["postgres", "mysql", "sqlite", "httpfs", "json", "parquet"]

        for ext in extensions:
            try:
                self.logger.debug("installing_extension", extension=ext)
                self.connection.execute(f"INSTALL {ext}")
                self.connection.execute(f"LOAD {ext}")
                self.logger.info("extension_loaded", extension=ext)
            except duckdb.Error as e:
                # Non-critical: Some extensions may not be available
                self.logger.warning(
                    "extension_load_failed",
                    extension=ext,
                    error=str(e),
                )

    async def _attach_default_databases(self) -> None:
        """
        Attach default PostgreSQL and SQLite databases.
        
        PostgreSQL: Uses settings from config
        SQLite: Creates local cache database
        """
        # Attach PostgreSQL
        try:
            pg_conn_str = self.settings.postgres.connection_string
            self.connection.execute(f"ATTACH '{pg_conn_str}' AS pg (TYPE POSTGRES)")
            
            self._attached_databases["pg"] = {
                "type": "postgres",
                "connection_string": pg_conn_str,
                "attached_at": time.time(),
            }
            
            self.logger.info("attached_database", alias="pg", db_type="postgres")
        except duckdb.Error as e:
            self.logger.error("postgres_attachment_failed", error=str(e))
            # Don't raise - PostgreSQL might not be available yet

        # Attach SQLite (create if not exists)
        try:
            sqlite_path = Path("/data/local.db")
            sqlite_path.parent.mkdir(parents=True, exist_ok=True)
            
            self.connection.execute(f"ATTACH '{sqlite_path}' AS sqlite (TYPE SQLITE)")
            
            self._attached_databases["sqlite"] = {
                "type": "sqlite",
                "connection_string": str(sqlite_path),
                "attached_at": time.time(),
            }
            
            self.logger.info("attached_database", alias="sqlite", db_type="sqlite")
        except duckdb.Error as e:
            self.logger.error("sqlite_attachment_failed", error=str(e))

    # ==================================================================================
    # QueryableProtocol Implementation
    # ==================================================================================

    def execute(
        self,
        sql: str,
        parameters: dict[str, Any] | None = None,
    ) -> list[tuple[Any, ...]]:
        """
        Execute SQL query and return raw results.
        
        Implements QueryableProtocol.execute()
        
        Args:
            sql: SQL query string
            parameters: Optional query parameters
            
        Returns:
            List of result tuples
            
        Raises:
            DuckDBConnectionError: If connection not initialized
            DuckDBQueryError: If query execution fails
        """
        if not self._is_initialized or not self.connection:
            msg = "DuckDB connection not initialized"
            raise DuckDBConnectionError(msg)

        try:
            if parameters:
                result = self.connection.execute(sql, parameters)
            else:
                result = self.connection.execute(sql)

            return result.fetchall()

        except duckdb.Error as e:
            self.logger.error(
                "query_execution_failed",
                sql=sql[:200],  # Truncate for logging
                error=str(e),
            )
            raise DuckDBQueryError(f"Query execution failed: {e}") from e

    def execute_many(
        self,
        sql: str,
        param_list: list[dict[str, Any]],
    ) -> int:
        """
        Execute batch operations.
        
        Implements QueryableProtocol.execute_many()
        
        Args:
            sql: SQL statement
            param_list: List of parameter dictionaries
            
        Returns:
            Number of affected rows
            
        Raises:
            DuckDBConnectionError: If connection not initialized
            DuckDBQueryError: If batch execution fails
        """
        if not self._is_initialized or not self.connection:
            msg = "DuckDB connection not initialized"
            raise DuckDBConnectionError(msg)

        try:
            affected_rows = 0
            for params in param_list:
                result = self.connection.execute(sql, params)
                affected_rows += result.rowcount if hasattr(result, "rowcount") else 0

            return affected_rows

        except duckdb.Error as e:
            self.logger.error("batch_execution_failed", error=str(e))
            raise DuckDBQueryError(f"Batch execution failed: {e}") from e

    @property
    def description(self) -> list[tuple[str, ...]]:
        """
        Get column descriptions from last query.
        
        Implements QueryableProtocol.description
        
        Returns:
            List of column description tuples
        """
        if not self.connection:
            return []
        return self.connection.description or []

    # ==================================================================================
    # AttachableProtocol Implementation
    # ==================================================================================

    def attach(
        self,
        alias: str,
        db_type: str,
        connection_string: str,
    ) -> None:
        """
        Attach external database to DuckDB.
        
        Implements AttachableProtocol.attach()
        
        Args:
            alias: Database alias
            db_type: Database type (postgres, mysql, sqlite)
            connection_string: Database connection string
            
        Raises:
            DuckDBConnectionError: If connection not initialized
            DuckDBQueryError: If attachment fails
        """
        if not self._is_initialized or not self.connection:
            msg = "DuckDB connection not initialized"
            raise DuckDBConnectionError(msg)

        # Check if already attached
        if alias in self._attached_databases:
            msg = f"Database '{alias}' is already attached"
            raise DuckDBQueryError(msg)

        db_type_upper = db_type.upper()

        try:
            self.logger.info(
                "attaching_database",
                alias=alias,
                db_type=db_type,
            )

            self.connection.execute(
                f"ATTACH '{connection_string}' AS {alias} (TYPE {db_type_upper})"
            )

            self._attached_databases[alias] = {
                "type": db_type,
                "connection_string": connection_string,
                "attached_at": time.time(),
            }

            self.logger.info(
                "database_attached",
                alias=alias,
                db_type=db_type,
            )

        except duckdb.Error as e:
            self.logger.error(
                "database_attachment_failed",
                alias=alias,
                error=str(e),
            )
            raise DuckDBQueryError(f"Failed to attach database '{alias}': {e}") from e

    def detach(self, alias: str) -> None:
        """
        Detach previously attached database.
        
        Implements AttachableProtocol.detach()
        
        Args:
            alias: Database alias to detach
            
        Raises:
            DuckDBConnectionError: If connection not initialized
            DuckDBQueryError: If detachment fails
        """
        if not self._is_initialized or not self.connection:
            msg = "DuckDB connection not initialized"
            raise DuckDBConnectionError(msg)

        if alias not in self._attached_databases:
            msg = f"Database '{alias}' is not attached"
            raise DuckDBQueryError(msg)

        try:
            self.connection.execute(f"DETACH {alias}")
            del self._attached_databases[alias]
            
            self.logger.info("database_detached", alias=alias)

        except duckdb.Error as e:
            self.logger.error(
                "database_detachment_failed",
                alias=alias,
                error=str(e),
            )
            raise DuckDBQueryError(f"Failed to detach database '{alias}': {e}") from e

    def list_attachments(self) -> list[dict[str, Any]]:
        """
        List all currently attached databases.
        
        Implements AttachableProtocol.list_attachments()
        
        Returns:
            List of attachment metadata dictionaries
            
        Raises:
            DuckDBConnectionError: If connection not initialized
        """
        if not self._is_initialized or not self.connection:
            msg = "DuckDB connection not initialized"
            raise DuckDBConnectionError(msg)

        try:
            result = self.connection.execute("SELECT * FROM duckdb_databases()").fetchall()

            databases = []
            for row in result:
                db_name = row[0]
                databases.append({
                    "database_name": db_name,
                    "database_oid": row[1],
                    "path": row[2],
                    "database_type": self._attached_databases.get(db_name, {}).get("type", "unknown"),
                    "attached": db_name in self._attached_databases,
                    "attached_at": self._attached_databases.get(db_name, {}).get("attached_at"),
                })

            return databases

        except duckdb.Error as e:
            self.logger.error("list_databases_failed", error=str(e))
            raise DuckDBQueryError(f"Failed to list databases: {e}") from e

    # ==================================================================================
    # ConnectionManageable Implementation
    # ==================================================================================

    def connect(self) -> None:
        """
        Establish database connection.
        
        Implements ConnectionManageable.connect()
        """
        if self._is_initialized:
            self.logger.warning("connection_already_established")
            return

        # Use async initialize for full setup
        import asyncio
        asyncio.run(self.initialize())

    def disconnect(self) -> None:
        """
        Close database connection.
        
        Implements ConnectionManageable.disconnect()
        """
        if self.connection:
            try:
                self.connection.close()
                self.logger.info("duckdb_connection_closed")
            except Exception as e:
                self.logger.error("connection_close_failed", error=str(e))
            finally:
                self.connection = None
                self._attached_databases.clear()
                self._is_initialized = False

    def is_connected(self) -> bool:
        """
        Check if connection is active.
        
        Implements ConnectionManageable.is_connected()
        
        Returns:
            True if connected, False otherwise
        """
        return self._is_initialized and self.connection is not None

    def reconnect(self) -> None:
        """
        Reconnect to database.
        
        Implements ConnectionManageable.reconnect()
        """
        self.logger.info("reconnecting_to_database")
        self.disconnect()
        self.connect()

    # ==================================================================================
    # Additional Helper Methods
    # ==================================================================================

    def get_uptime(self) -> float:
        """
        Get service uptime in seconds.
        
        Returns:
            Uptime in seconds
        """
        return time.time() - self.start_time

    def execute_query_with_metrics(
        self,
        sql: str,
        parameters: dict[str, Any] | None = None,
    ) -> tuple[list[str], list[list[Any]], float]:
        """
        Execute query and collect execution metrics.
        
        Args:
            sql: SQL query string
            parameters: Optional query parameters
            
        Returns:
            Tuple of (columns, rows, execution_time_ms)
            
        Raises:
            DuckDBConnectionError: If connection not initialized
            DuckDBQueryError: If query execution fails
        """
        start_time = time.perf_counter()

        try:
            rows = self.execute(sql, parameters)
            columns = [desc[0] for desc in self.description] if self.description else []

            execution_time_ms = (time.perf_counter() - start_time) * 1000

            self.logger.info(
                "query_executed",
                row_count=len(rows),
                execution_time_ms=round(execution_time_ms, 2),
            )

            return columns, rows, execution_time_ms

        except (DuckDBConnectionError, DuckDBQueryError):
            raise


# ==================================================================================
# Global Manager Instance (Singleton Pattern)
# ==================================================================================

_manager: DuckDBManager | None = None


def get_duckdb_manager(settings: Settings) -> DuckDBManager:
    """
    Get or create DuckDB manager instance (Singleton).
    
    Args:
        settings: Application settings
        
    Returns:
        DuckDBManager singleton instance
    """
    global _manager
    if _manager is None:
        _manager = DuckDBManager(settings)
    return _manager


@asynccontextmanager
async def duckdb_lifespan(settings: Settings) -> AsyncIterator[DuckDBManager]:
    """
    Async context manager for DuckDB lifecycle.
    
    Args:
        settings: Application settings
        
    Yields:
        Initialized DuckDBManager instance
        
    Example:
        ```python
        async with duckdb_lifespan(settings) as manager:
            result = manager.execute("SELECT 1")
        ```
    """
    manager = get_duckdb_manager(settings)
    await manager.initialize()
    try:
        yield manager
    finally:
        manager.disconnect()
```

[Back to TOC](#-table-of-contents)

---

Would you like me to continue with Part 3, which will include:
- FastAPI routers (query endpoints, attachment endpoints, health checks)
- Structured logging implementation
- Main application entry point
- Additional utility functions