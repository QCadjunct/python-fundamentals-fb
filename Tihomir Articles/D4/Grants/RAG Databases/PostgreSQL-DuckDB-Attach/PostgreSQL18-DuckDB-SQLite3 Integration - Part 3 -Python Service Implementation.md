# 🐘 PostgreSQL18-DuckDB-SQLite3 Integration with LLM-SQL Architecture

## 🐍 Python Service Implementation - Part 3

[Back to TOC](#-table-of-contents)

### Structured Logging Utility (src/utils/logging.py)

```python
"""
Structured logging configuration using structlog.

Implements consistent, structured logging with correlation IDs
and context propagation for distributed tracing.
"""

import logging
import sys
from typing import Any

import structlog
from structlog.types import EventDict, Processor


def add_correlation_id(logger: logging.Logger, method_name: str, event_dict: EventDict) -> EventDict:
    """
    Add correlation ID to log events.
    
    Args:
        logger: Logger instance
        method_name: Log method name
        event_dict: Event dictionary
        
    Returns:
        Modified event dictionary with correlation_id
    """
    # Try to get correlation_id from context
    correlation_id = event_dict.get("correlation_id")
    if correlation_id:
        event_dict["correlation_id"] = correlation_id
    return event_dict


def add_service_context(logger: logging.Logger, method_name: str, event_dict: EventDict) -> EventDict:
    """
    Add service context to all log events.
    
    Args:
        logger: Logger instance
        method_name: Log method name
        event_dict: Event dictionary
        
    Returns:
        Modified event dictionary with service context
    """
    event_dict.setdefault("service", "duckdb-query-service")
    event_dict.setdefault("version", "1.0.0")
    return event_dict


def configure_logging(log_level: str = "INFO", log_format: str = "json") -> None:
    """
    Configure structured logging for the application.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_format: Log format (json or text)
    """
    # Configure processors based on format
    if log_format == "json":
        processors: list[Processor] = [
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            add_correlation_id,
            add_service_context,
            structlog.processors.JSONRenderer(),
        ]
    else:
        processors = [
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            add_correlation_id,
            add_service_context,
            structlog.dev.ConsoleRenderer(),
        ]

    # Configure structlog
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    # Configure standard logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, log_level.upper()),
    )


def get_logger(name: str) -> structlog.stdlib.BoundLogger:
    """
    Get a configured logger instance.
    
    Args:
        name: Logger name (typically __name__)
        
    Returns:
        Configured structlog logger
    """
    return structlog.get_logger(name)
```

### Prometheus Metrics (src/utils/metrics.py)

```python
"""
Prometheus metrics for monitoring.

Implements application performance monitoring with standardized metrics
following Prometheus best practices.
"""

from prometheus_client import Counter, Gauge, Histogram, Info

# Application info
app_info = Info("duckdb_service", "DuckDB Query Service Information")

# Query metrics
query_total = Counter(
    "duckdb_queries_total",
    "Total number of queries executed",
    ["database", "status"],
)

query_duration_seconds = Histogram(
    "duckdb_query_duration_seconds",
    "Query execution duration in seconds",
    ["database"],
    buckets=(0.01, 0.05, 0.1, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0, 60.0),
)

query_rows_returned = Histogram(
    "duckdb_query_rows_returned",
    "Number of rows returned by queries",
    ["database"],
    buckets=(1, 10, 100, 1000, 10000, 100000, 1000000),
)

# Attachment metrics
attachments_total = Gauge(
    "duckdb_attachments_total",
    "Total number of attached databases",
)

attachment_operations = Counter(
    "duckdb_attachment_operations_total",
    "Total attachment operations",
    ["operation", "db_type", "status"],
)

# Connection metrics
active_connections = Gauge(
    "duckdb_active_connections",
    "Number of active database connections",
)

connection_errors = Counter(
    "duckdb_connection_errors_total",
    "Total connection errors",
    ["error_type"],
)

# Resource metrics
memory_usage_bytes = Gauge(
    "duckdb_memory_usage_bytes",
    "Current memory usage in bytes",
)

# Error metrics
errors_total = Counter(
    "duckdb_errors_total",
    "Total errors by type",
    ["error_type", "endpoint"],
)


def init_metrics(version: str, python_version: str) -> None:
    """
    Initialize application metrics.
    
    Args:
        version: Application version
        python_version: Python version
    """
    app_info.info({
        "version": version,
        "python_version": python_version,
    })
```

### FastAPI Query Router (src/routers/query.py)

```python
"""
Query execution endpoints.

Implements RESTful API for SQL query execution with comprehensive
error handling and validation.
"""

import time
import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.responses import JSONResponse
import structlog

from src.config import Settings, get_settings
from src.models.requests import QueryRequest, BatchQueryRequest
from src.models.responses import QueryResult, BatchQueryResult, ErrorResponse
from src.services.duckdb_manager import DuckDBManager, get_duckdb_manager
from src.services.duckdb_manager import DuckDBConnectionError, DuckDBQueryError
from src.utils.metrics import (
    query_total,
    query_duration_seconds,
    query_rows_returned,
    errors_total,
)

logger = structlog.get_logger(__name__)

router = APIRouter(prefix="/query", tags=["Query Execution"])


def get_correlation_id(
    x_correlation_id: Annotated[str | None, Header()] = None
) -> str:
    """
    Get or generate correlation ID for request tracing.
    
    Args:
        x_correlation_id: Correlation ID from header
        
    Returns:
        Correlation ID (existing or newly generated)
    """
    return x_correlation_id or str(uuid.uuid4())


@router.post(
    "/",
    response_model=QueryResult,
    status_code=200,
    summary="Execute SQL Query",
    description="Execute a SQL query against DuckDB or attached databases",
    responses={
        200: {
            "description": "Query executed successfully",
            "model": QueryResult,
        },
        400: {
            "description": "Invalid query or parameters",
            "model": ErrorResponse,
        },
        500: {
            "description": "Query execution error",
            "model": ErrorResponse,
        },
    },
)
async def execute_query(
    request: QueryRequest,
    manager: Annotated[DuckDBManager, Depends(get_duckdb_manager)],
    settings: Annotated[Settings, Depends(get_settings)],
    correlation_id: Annotated[str, Depends(get_correlation_id)],
) -> QueryResult:
    """
    Execute SQL query with validation and metrics collection.
    
    Args:
        request: Query request with SQL and parameters
        manager: DuckDB manager instance
        settings: Application settings
        correlation_id: Request correlation ID
        
    Returns:
        Query execution result
        
    Raises:
        HTTPException: On validation or execution errors
    """
    log = logger.bind(
        correlation_id=correlation_id,
        database=request.database,
        sql_length=len(request.sql),
    )

    log.info("query_received")

    start_time = time.perf_counter()

    try:
        # Execute query with metrics
        columns, rows, execution_time_ms = manager.execute_query_with_metrics(
            sql=request.sql,
            parameters=request.parameters,
        )

        # Apply row limit if specified
        truncated = False
        if request.max_rows and len(rows) > request.max_rows:
            rows = rows[: request.max_rows]
            truncated = True
            log.warning("results_truncated", original_rows=len(rows), max_rows=request.max_rows)

        # Record metrics
        query_total.labels(database=request.database, status="success").inc()
        query_duration_seconds.labels(database=request.database).observe(
            execution_time_ms / 1000
        )
        query_rows_returned.labels(database=request.database).observe(len(rows))

        log.info(
            "query_executed_successfully",
            row_count=len(rows),
            execution_time_ms=execution_time_ms,
            truncated=truncated,
        )

        return QueryResult(
            columns=columns,
            rows=rows,
            row_count=len(rows),
            execution_time_ms=execution_time_ms,
            database=request.database,
            truncated=truncated,
        )

    except DuckDBConnectionError as e:
        query_total.labels(database=request.database, status="connection_error").inc()
        errors_total.labels(error_type="connection_error", endpoint="/query").inc()
        
        log.error("connection_error", error=str(e))
        
        raise HTTPException(
            status_code=500,
            detail={
                "error": "ConnectionError",
                "message": "Database connection failed",
                "detail": str(e),
                "correlation_id": correlation_id,
            },
        ) from e

    except DuckDBQueryError as e:
        query_total.labels(database=request.database, status="query_error").inc()
        errors_total.labels(error_type="query_error", endpoint="/query").inc()
        
        log.error("query_execution_error", error=str(e))
        
        raise HTTPException(
            status_code=400,
            detail={
                "error": "QueryExecutionError",
                "message": "Query execution failed",
                "detail": str(e),
                "correlation_id": correlation_id,
            },
        ) from e

    except Exception as e:
        query_total.labels(database=request.database, status="internal_error").inc()
        errors_total.labels(error_type="internal_error", endpoint="/query").inc()
        
        log.error("unexpected_error", error=str(e), exc_info=True)
        
        raise HTTPException(
            status_code=500,
            detail={
                "error": "InternalServerError",
                "message": "An unexpected error occurred",
                "detail": str(e),
                "correlation_id": correlation_id,
            },
        ) from e


@router.post(
    "/batch",
    response_model=BatchQueryResult,
    status_code=200,
    summary="Execute Batch Queries",
    description="Execute multiple SQL queries in sequence or transaction",
)
async def execute_batch_queries(
    request: BatchQueryRequest,
    manager: Annotated[DuckDBManager, Depends(get_duckdb_manager)],
    correlation_id: Annotated[str, Depends(get_correlation_id)],
) -> BatchQueryResult:
    """
    Execute batch of queries with optional transactional support.
    
    Args:
        request: Batch query request
        manager: DuckDB manager instance
        correlation_id: Request correlation ID
        
    Returns:
        Batch execution results
    """
    log = logger.bind(
        correlation_id=correlation_id,
        query_count=len(request.queries),
        transactional=request.transactional,
    )

    log.info("batch_query_received")

    results: list[QueryResult | ErrorResponse] = []
    successful = 0
    failed = 0
    total_start_time = time.perf_counter()

    # Begin transaction if requested
    if request.transactional:
        try:
            manager.execute("BEGIN TRANSACTION")
            log.debug("transaction_started")
        except Exception as e:
            log.error("transaction_start_failed", error=str(e))
            raise HTTPException(
                status_code=500,
                detail={
                    "error": "TransactionError",
                    "message": "Failed to start transaction",
                    "detail": str(e),
                },
            ) from e

    try:
        for idx, query_request in enumerate(request.queries):
            log.debug("executing_batch_query", index=idx)

            try:
                columns, rows, execution_time_ms = manager.execute_query_with_metrics(
                    sql=query_request.sql,
                    parameters=query_request.parameters,
                )

                result = QueryResult(
                    columns=columns,
                    rows=rows,
                    row_count=len(rows),
                    execution_time_ms=execution_time_ms,
                    database=query_request.database,
                )
                results.append(result)
                successful += 1

                log.debug("batch_query_success", index=idx, row_count=len(rows))

            except Exception as e:
                error_response = ErrorResponse(
                    error="QueryExecutionError",
                    message=f"Query {idx} failed",
                    detail=str(e),
                    correlation_id=correlation_id,
                )
                results.append(error_response)
                failed += 1

                log.warning("batch_query_failed", index=idx, error=str(e))

                if request.stop_on_error:
                    log.info("stopping_batch_on_error", failed_index=idx)
                    break

        # Commit transaction if all succeeded
        if request.transactional:
            if failed == 0:
                manager.execute("COMMIT")
                log.info("transaction_committed")
            else:
                manager.execute("ROLLBACK")
                log.warning("transaction_rolled_back", failed_queries=failed)

    except Exception as e:
        if request.transactional:
            try:
                manager.execute("ROLLBACK")
                log.error("transaction_rolled_back_on_error")
            except Exception:
                pass  # Best effort rollback

        log.error("batch_execution_failed", error=str(e), exc_info=True)
        raise

    total_execution_time_ms = (time.perf_counter() - total_start_time) * 1000

    log.info(
        "batch_execution_complete",
        total_queries=len(request.queries),
        successful=successful,
        failed=failed,
        total_time_ms=round(total_execution_time_ms, 2),
    )

    return BatchQueryResult(
        results=results,
        total_queries=len(request.queries),
        successful_queries=successful,
        failed_queries=failed,
        total_execution_time_ms=round(total_execution_time_ms, 2),
    )
```

### FastAPI Attachment Router (src/routers/attachment.py)

```python
"""
Database attachment endpoints.

Implements RESTful API for dynamic database attachment/detachment
with comprehensive validation and error handling.
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
import structlog

from src.config import Settings, get_settings
from src.models.requests import AttachDatabaseRequest, DetachDatabaseRequest
from src.models.responses import AttachmentStatus, DatabaseListResponse, DatabaseInfo
from src.services.duckdb_manager import DuckDBManager, get_duckdb_manager
from src.services.duckdb_manager import DuckDBQueryError
from src.utils.metrics import attachments_total, attachment_operations
from src.routers.query import get_correlation_id

logger = structlog.get_logger(__name__)

router = APIRouter(prefix="/attach", tags=["Database Attachment"])


@router.post(
    "/",
    response_model=AttachmentStatus,
    status_code=200,
    summary="Attach Database",
    description="Dynamically attach an external database to DuckDB",
)
async def attach_database(
    request: AttachDatabaseRequest,
    manager: Annotated[DuckDBManager, Depends(get_duckdb_manager)],
    settings: Annotated[Settings, Depends(get_settings)],
    correlation_id: Annotated[str, Depends(get_correlation_id)],
) -> AttachmentStatus:
    """
    Attach external database to DuckDB.
    
    Args:
        request: Attachment request with alias and connection details
        manager: DuckDB manager instance
        settings: Application settings
        correlation_id: Request correlation ID
        
    Returns:
        Attachment status
        
    Raises:
        HTTPException: On attachment errors
    """
    log = logger.bind(
        correlation_id=correlation_id,
        alias=request.alias,
        db_type=request.db_type,
    )

    log.info("attachment_requested")

    # Build connection string if not provided
    connection_string = request.connection_string
    if not connection_string:
        if request.db_type == "postgres":
            connection_string = settings.postgres.connection_string
        elif request.db_type == "mysql":
            connection_string = settings.mysql.connection_string
        elif request.db_type == "sqlite":
            raise HTTPException(
                status_code=400,
                detail={
                    "error": "ValidationError",
                    "message": "SQLite requires explicit connection_string (file path)",
                },
            )

    try:
        manager.attach(
            alias=request.alias,
            db_type=request.db_type,
            connection_string=connection_string,
        )

        # Update metrics
        attachments_total.inc()
        attachment_operations.labels(
            operation="attach",
            db_type=request.db_type,
            status="success",
        ).inc()

        log.info("database_attached_successfully")

        return AttachmentStatus(
            status="success",
            alias=request.alias,
            db_type=request.db_type,
            message=f"Successfully attached {request.db_type} database as '{request.alias}'",
        )

    except DuckDBQueryError as e:
        attachment_operations.labels(
            operation="attach",
            db_type=request.db_type,
            status="error",
        ).inc()

        log.error("attachment_failed", error=str(e))

        raise HTTPException(
            status_code=400,
            detail={
                "error": "AttachmentError",
                "message": "Failed to attach database",
                "detail": str(e),
                "correlation_id": correlation_id,
            },
        ) from e


@router.delete(
    "/{alias}",
    response_model=AttachmentStatus,
    status_code=200,
    summary="Detach Database",
    description="Detach a previously attached database",
)
async def detach_database(
    alias: str,
    manager: Annotated[DuckDBManager, Depends(get_duckdb_manager)],
    correlation_id: Annotated[str, Depends(get_correlation_id)],
) -> AttachmentStatus:
    """
    Detach database from DuckDB.
    
    Args:
        alias: Database alias to detach
        manager: DuckDB manager instance
        correlation_id: Request correlation ID
        
    Returns:
        Detachment status
        
    Raises:
        HTTPException: On detachment errors
    """
    log = logger.bind(correlation_id=correlation_id, alias=alias)

    log.info("detachment_requested")

    try:
        # Get database type before detaching
        attachments = manager.list_attachments()
        db_info = next((db for db in attachments if db["database_name"] == alias), None)
        
        if not db_info:
            raise HTTPException(
                status_code=404,
                detail={
                    "error": "NotFoundError",
                    "message": f"Database '{alias}' not found or not attached",
                },
            )

        db_type = db_info.get("database_type", "unknown")

        manager.detach(alias)

        # Update metrics
        attachments_total.dec()
        attachment_operations.labels(
            operation="detach",
            db_type=db_type,
            status="success",
        ).inc()

        log.info("database_detached_successfully")

        return AttachmentStatus(
            status="success",
            alias=alias,
            db_type=db_type,
            message=f"Successfully detached database '{alias}'",
        )

    except DuckDBQueryError as e:
        attachment_operations.labels(
            operation="detach",
            db_type="unknown",
            status="error",
        ).inc()

        log.error("detachment_failed", error=str(e))

        raise HTTPException(
            status_code=400,
            detail={
                "error": "DetachmentError",
                "message": "Failed to detach database",
                "detail": str(e),
                "correlation_id": correlation_id,
            },
        ) from e


@router.get(
    "/",
    response_model=DatabaseListResponse,
    status_code=200,
    summary="List Attached Databases",
    description="List all currently attached databases",
)
async def list_databases(
    manager: Annotated[DuckDBManager, Depends(get_duckdb_manager)],
    correlation_id: Annotated[str, Depends(get_correlation_id)],
) -> DatabaseListResponse:
    """
    List all attached databases.
    
    Args:
        manager: DuckDB manager instance
        correlation_id: Request correlation ID
        
    Returns:
        List of attached databases
    """
    log = logger.bind(correlation_id=correlation_id)

    log.debug("list_databases_requested")

    try:
        attachments = manager.list_attachments()

        databases = [
            DatabaseInfo(
                database_name=db["database_name"],
                database_oid=db["database_oid"],
                path=db["path"],
                database_type=db["database_type"],
                attached=db["attached"],
            )
            for db in attachments
        ]

        log.info("databases_listed", count=len(databases))

        return DatabaseListResponse(
            databases=databases,
            count=len(databases),
        )

    except Exception as e:
        log.error("list_databases_failed", error=str(e), exc_info=True)

        raise HTTPException(
            status_code=500,
            detail={
                "error": "InternalServerError",
                "message": "Failed to list databases",
                "detail": str(e),
                "correlation_id": correlation_id,
            },
        ) from e
```

### FastAPI Health Router (src/routers/health.py)

```python
"""
Health check endpoints.

Implements comprehensive health monitoring including
dependency checks and resource metrics.
"""

import sys
from typing import Annotated

from fastapi import APIRouter, Depends
import duckdb
import structlog

from src.config import Settings, get_settings
from src.models.responses import HealthResponse
from src.services.duckdb_manager import DuckDBManager, get_duckdb_manager

logger = structlog.get_logger(__name__)

router = APIRouter(prefix="/health", tags=["Health"])


@router.get(
    "/",
    response_model=HealthResponse,
    status_code=200,
    summary="Health Check",
    description="Check service health and dependencies",
)
async def health_check(
    manager: Annotated[DuckDBManager, Depends(get_duckdb_manager)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> HealthResponse:
    """
    Comprehensive health check.
    
    Args:
        manager: DuckDB manager instance
        settings: Application settings
        
    Returns:
        Health status with metrics
    """
    logger.debug("health_check_requested")

    # Check DuckDB connection
    is_connected = manager.is_connected()
    status = "healthy" if is_connected else "unhealthy"

    # Get attached databases count
    try:
        attachments = manager.list_attachments() if is_connected else []
        attached_count = len(attachments)
    except Exception:
        attached_count = 0
        status = "degraded"

    # Get uptime
    uptime = manager.get_uptime()

    logger.info(
        "health_check_complete",
        status=status,
        attached_databases=attached_count,
        uptime_seconds=round(uptime, 2),
    )

    return HealthResponse(
        status=status,
        duckdb_version=duckdb.__version__,
        attached_databases=attached_count,
        uptime_seconds=round(uptime, 2),
    )


@router.get(
    "/ready",
    status_code=200,
    summary="Readiness Check",
    description="Check if service is ready to accept requests",
)
async def readiness_check(
    manager: Annotated[DuckDBManager, Depends(get_duckdb_manager)],
) -> dict[str, str]:
    """
    Kubernetes-style readiness probe.
    
    Args:
        manager: DuckDB manager instance
        
    Returns:
        Readiness status
    """
    if not manager.is_connected():
        logger.warning("readiness_check_failed_not_connected")
        return {"status": "not_ready"}

    return {"status": "ready"}


@router.get(
    "/live",
    status_code=200,
    summary="Liveness Check",
    description="Check if service is alive",
)
async def liveness_check() -> dict[str, str]:
    """
    Kubernetes-style liveness probe.
    
    Returns:
        Liveness status
    """
    return {"status": "alive"}
```

### Main Application Entry (src/main.py)

```python
"""
FastAPI application entry point.

Implements application lifecycle, routing, middleware,
and exception handling following best practices.
"""

import sys
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from prometheus_client import make_asgi_app
import structlog

from src.config import get_settings
from src.routers import query, attachment, health
from src.services.duckdb_manager import duckdb_lifespan, get_duckdb_manager
from src.utils.logging import configure_logging
from src.utils.metrics import init_metrics

# Get settings
settings = get_settings()

# Configure logging
configure_logging(
    log_level=settings.app.log_level,
    log_format=settings.app.log_format,
)

logger = structlog.get_logger(__name__)


@asynccontextmanager
async def app_lifespan(app: FastAPI) -> AsyncIterator[None]:
    """
    Application lifecycle manager.
    
    Handles startup and shutdown operations including:
    - DuckDB initialization
    - Metrics initialization
    - Resource cleanup
    
    Args:
        app: FastAPI application instance
        
    Yields:
        None (application running)
    """
    # Startup
    logger.info(
        "application_starting",
        name=settings.app.name,
        version=settings.app.version,
        log_level=settings.app.log_level,
    )

    # Initialize metrics
    init_metrics(
        version=settings.app.version,
        python_version=f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
    )

    # Initialize DuckDB
    try:
        manager = get_duckdb_manager(settings)
        await manager.initialize()
        logger.info("duckdb_initialized_successfully")
    except Exception as e:
        logger.error("duckdb_initialization_failed", error=str(e), exc_info=True)
        raise

    logger.info("application_started")

    yield

    # Shutdown
    logger.info("application_shutting_down")

    try:
        manager = get_duckdb_manager(settings)
        manager.disconnect()
        logger.info("duckdb_connection_closed")
    except Exception as e:
        logger.error("shutdown_error", error=str(e))

    logger.info("application_stopped")


# Create FastAPI application
app = FastAPI(
    title=settings.app.name,
    version=settings.app.version,
    description="DuckDB unified query engine with multi-database attachments",
    docs_url=f"{settings.app.api_prefix}/docs",
    redoc_url=f"{settings.app.api_prefix}/redoc",
    openapi_url=f"{settings.app.api_prefix}/openapi.json",
    lifespan=app_lifespan,
)

# ==================================================================================
# Middleware Configuration
# ==================================================================================

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.app.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    Log all HTTP requests with correlation IDs.
    
    Args:
        request: HTTP request
        call_next: Next middleware in chain
        
    Returns:
        HTTP response
    """
    correlation_id = request.headers.get("x-correlation-id", "unknown")
    
    log = logger.bind(
        correlation_id=correlation_id,
        method=request.method,
        path=request.url.path,
        client=request.client.host if request.client else "unknown",
    )

    log.info("request_received")

    try:
        response = await call_next(request)
        
        log.info(
            "request_completed",
            status_code=response.status_code,
        )
        
        return response

    except Exception as e:
        log.error("request_failed", error=str(e), exc_info=True)
        raise


# ==================================================================================
# Exception Handlers
# ==================================================================================

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    """
    Handle Pydantic validation errors.
    
    Args:
        request: HTTP request
        exc: Validation exception
        
    Returns:
        JSON error response
    """
    correlation_id = request.headers.get("x-correlation-id", "unknown")
    
    logger.warning(
        "validation_error",
        correlation_id=correlation_id,
        errors=exc.errors(),
    )

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "ValidationError",
            "message": "Request validation failed",
            "detail": exc.errors(),
            "correlation_id": correlation_id,
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """
    Handle unexpected exceptions.
    
    Args:
        request: HTTP request
        exc: Exception
        
    Returns:
        JSON error response
    """
    correlation_id = request.headers.get("x-correlation-id", "unknown")
    
    logger.error(
        "unhandled_exception",
        correlation_id=correlation_id,
        error=str(exc),
        exc_info=True,
    )

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "InternalServerError",
            "message": "An unexpected error occurred",
            "detail": str(exc),
            "correlation_id": correlation_id,
        },
    )


# ==================================================================================
# Router Registration
# ==================================================================================

app.include_router(query.router, prefix=settings.app.api_prefix)
app.include_router(attachment.router, prefix=settings.app.api_prefix)
app.include_router(health.router, prefix=settings.app.api_prefix)

# Prometheus metrics endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


# ==================================================================================
# Root Endpoint
# ==================================================================================

@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    """
    Root endpoint providing API information.
    
    Returns:
        API metadata
    """
    return {
        "service": settings.app.name,
        "version": settings.app.version,
        "docs": f"{settings.app.api_prefix}/docs",
        "health": f"{settings.app.api_prefix}/health",
    }
```

### Application __init__.py Files

```python
# src/__init__.py
"""DuckDB Query Service - Python 3.14 with uv and Pydantic v2."""

__version__ = "1.0.0"
__author__ = "Peter Heller"
__email__ = "peter.heller@qc.cuny.edu"

# src/models/__init__.py
"""Pydantic v2 models for request/response validation."""

from src.models.requests import QueryRequest, AttachDatabaseRequest, BatchQueryRequest
from src.models.responses import (
    QueryResult,
    AttachmentStatus,
    DatabaseInfo,
    DatabaseListResponse,
    HealthResponse,
    ErrorResponse,
)

__all__ = [
    "QueryRequest",
    "AttachDatabaseRequest",
    "BatchQueryRequest",
    "QueryResult",
    "AttachmentStatus",
    "DatabaseInfo",
    "DatabaseListResponse",
    "HealthResponse",
    "ErrorResponse",
]

# src/services/__init__.py
"""Service layer implementing business logic."""

from src.services.duckdb_manager import DuckDBManager, get_duckdb_manager

__all__ = ["DuckDBManager", "get_duckdb_manager"]

# src/protocols/__init__.py
"""Protocol definitions for structural typing."""

from src.protocols.database import (
    QueryableProtocol,
    TransactionalProtocol,
    AttachableProtocol,
    ConnectionManageable,
    HealthCheckable,
)

__all__ = [
    "QueryableProtocol",
    "TransactionalProtocol",
    "AttachableProtocol",
    "ConnectionManageable",
    "HealthCheckable",
]

# src/routers/__init__.py
"""FastAPI routers for API endpoints."""

from src.routers import query, attachment, health

__all__ = ["query", "attachment", "health"]

# src/utils/__init__.py
"""Utility functions and helpers."""

from src.utils.logging import configure_logging, get_logger
from src.utils.metrics import init_metrics

__all__ = ["configure_logging", "get_logger", "init_metrics"]
```

[Back to TOC](#-table-of-contents)

---

**This completes Part 3 of the Python Service Implementation!**

The implementation now includes:
✅ Structured logging with correlation IDs  
✅ Prometheus metrics for monitoring  
✅ Complete FastAPI routers (query, attachment, health)  
✅ Comprehensive exception handling  
✅ Application lifecycle management  
✅ CORS middleware and request logging  

Would you like me to continue with:
- **Part 4**: Deployment & Operations Guide (step-by-step deployment, testing, monitoring setup)
- **Part 5**: Usage Examples & Patterns (real-world query examples, integration patterns)
- **Part 6**: Configuration & Tuning Reference (performance optimization, security hardening)