# 🐘 PostgreSQL18-DuckDB-SQLite3 Integration with LLM-SQL Architecture

**Complete Migration Guide with Bridged Architecture & D⁴ Methodology**

---

## 📋 Table of Contents

- [🎯 Executive Overview](#-executive-overview)
- [🏛️ Architectural Foundation](#️-architectural-foundation)
- [🗺️ System Architecture Diagram](#️-system-architecture-diagram)
- [🔄 Data Flow & Sequence Diagrams](#-data-flow--sequence-diagrams)
- [📦 Docker Infrastructure Configuration](#-docker-infrastructure-configuration)
- [🐍 Python Service Implementation - Part 1](#-python-service-implementation---part-1)
- [🐍 Python Service Implementation - Part 2](#-python-service-implementation---part-2)
- [🐍 Python Service Implementation - Part 3](#-python-service-implementation---part-3)
- [🚀 Deployment & Operations Guide](#-deployment--operations-guide)
- [📊 Usage Examples & Patterns](#-usage-examples--patterns)
- [🔧 Configuration & Tuning Reference](#-configuration--tuning-reference)
- [📈 Monitoring & Observability](#-monitoring--observability)

---

## 🎯 Executive Overview

[Back to TOC](#-table-of-contents)

### Purpose & Scope

This comprehensive guide details the migration from SQL Server to a PostgreSQL-centric architecture integrated with DuckDB as a unified query engine. The architecture embodies D⁴ (Domain-Driven Database Design) methodology, SOLID principles, and modern Python 3.14 best practices using Astral's `uv` package manager and `ruff` linter/formatter.

### Key Architectural Decisions

**Single Responsibility Principle (SRP)**  
Each database engine serves its optimal use case without overlap:

| Engine | Primary Responsibility | Use Cases |
|--------|----------------------|-----------|
| **PostgreSQL 18** | OLTP + Vector Search | Transactional data, pgvector embeddings, ACID compliance |
| **DuckDB** | Unified Analytics | Cross-database queries, OLAP workloads, data lake integration |
| **SQLite3** | Embedded Operations | Local caching, lightweight storage, edge computing |
| **MySQL 8.4** | Legacy Integration | Existing system compatibility, gradual migration path |

**KISS Principle (Keep It Simple, Stupid)**  
DuckDB's `ATTACH` feature eliminates complex ETL pipelines by providing zero-copy access to heterogeneous data sources. This reduces operational complexity while maintaining high performance.

### Technology Stack Matrix

```mermaid
graph TB
    subgraph FOUNDATION ["🏗️    Infrastructure    Foundation"]
        F1[Docker Compose v2.20+]
        F2[Ubuntu 24.04 LTS]
        F3[NVIDIA Container Toolkit]
    end
    
    subgraph DATABASES ["💾    Database    Layer"]
        D1[PostgreSQL 18<br/>pgvector + pg_duckdb]
        D2[DuckDB 0.10+<br/>Analytics Engine]
        D3[SQLite3 3.45+<br/>Embedded Cache]
        D4[MySQL 8.4<br/>Legacy Support]
    end
    
    subgraph PYTHON ["🐍    Python    3.14    Ecosystem"]
        P1[uv Package Manager]
        P2[Ruff Linter/Formatter]
        P3[Pydantic v2 Validation]
        P4[FastAPI 0.109+]
        P5[Structlog Logging]
    end
    
    subgraph SERVICES ["⚙️    Service    Layer"]
        S1[NGINX Alpine<br/>Reverse Proxy]
        S2[Ollama<br/>LLM Gateway]
        S3[Prometheus<br/>Metrics]
        S4[Grafana<br/>Visualization]
    end
    
    %% Foundation connections - Blue
    F1 --> D1
    F1 --> D2
    F1 --> D3
    F1 --> D4
    F2 --> F1
    F3 --> S2
    
    %% Database to Python - Purple
    D1 --> P4
    D2 --> P4
    D3 --> P4
    D4 --> P4
    
    %% Python ecosystem - Teal
    P1 --> P2
    P1 --> P3
    P1 --> P4
    P1 --> P5
    
    %% Services - Green
    S1 --> P4
    S2 --> P4
    P4 --> S3
    S3 --> S4
    
    %% Apply linkStyle
    linkStyle 0,1,2,3,4,5 stroke:#1976d2,stroke-width:3px
    linkStyle 6,7,8,9 stroke:#7b1fa2,stroke-width:3px
    linkStyle 10,11,12,13 stroke:#00695c,stroke-width:3px
    linkStyle 14,15,16,17 stroke:#388e3c,stroke-width:3px
    
    %% Define node classes
    classDef foundationStyle fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef databaseStyle fill:#e0f2f1,stroke:#00695c,stroke-width:2px
    classDef pythonStyle fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef serviceStyle fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    
    %% Apply classes
    class F1,F2,F3 foundationStyle
    class D1,D2,D3,D4 databaseStyle
    class P1,P2,P3,P4,P5 pythonStyle
    class S1,S2,S3,S4 serviceStyle
    
    %% Style subgraphs
    style FOUNDATION fill:#e8f4fd,stroke:#1976d2,stroke-width:3px,color:#000
    style DATABASES fill:#f0fffe,stroke:#00695c,stroke-width:3px,color:#000
    style PYTHON fill:#f8f0ff,stroke:#7b1fa2,stroke-width:3px,color:#000
    style SERVICES fill:#f0f8f0,stroke:#388e3c,stroke-width:3px,color:#000
```

### Architecture Benefits

✅ **Zero-ETL Architecture**: Direct database attachment eliminates data movement  
✅ **Type Safety**: Pydantic v2 provides runtime validation and IDE support  
✅ **Maintainability**: SOLID principles ensure clear separation of concerns  
✅ **Performance**: DuckDB's vectorized execution engine optimizes analytics  
✅ **Scalability**: Horizontal scaling via Docker Swarm or Kubernetes  
✅ **Observability**: Structured logging with correlation IDs and distributed tracing  

---

## 🏛️ Architectural Foundation

[Back to TOC](#-table-of-contents)

### D⁴ Methodology Integration

This architecture implements D⁴ (Domain-Driven Database Design) principles through:

1. **Business Glossary Domains (BGDs)**: PostgreSQL schemas map to business domains
2. **Fully Qualified Domain Names (FQDNs)**: Namespace hierarchy ensures semantic clarity
3. **Physical Data Model First**: Database schemas serve as source of truth
4. **Two-Value Predicate Logic**: NOT NULL constraints eliminate NULL ambiguity

### SOLID Principles Application

```mermaid
graph TB
    subgraph SRP ["🎯    Single    Responsibility    Principle"]
        S1[DuckDBManager:<br/>Connection Lifecycle]
        S2[AttachmentManager:<br/>Database Attachments]
        S3[QueryExecutor:<br/>SQL Execution]
    end
    
    subgraph OCP ["🔓    Open/Closed    Principle"]
        O1[DatabaseAdapter<br/>Protocol Interface]
        O2[PostgresAdapter<br/>Implementation]
        O3[MySQLAdapter<br/>Implementation]
    end
    
    subgraph LSP ["🔄    Liskov    Substitution    Principle"]
        L1[QueryableProtocol<br/>Abstract Interface]
        L2[All adapters<br/>interchangeable]
    end
    
    subgraph ISP ["🎭    Interface    Segregation    Principle"]
        I1[ReadableProtocol]
        I2[WritableProtocol]
        I3[AttachableProtocol]
    end
    
    subgraph DIP ["⬆️    Dependency    Inversion    Principle"]
        D1[High-level<br/>Business Logic]
        D2[Depends on<br/>Protocols]
        D3[Not concrete<br/>implementations]
    end
    
    %% SRP connections - Blue
    S1 --> S2
    S2 --> S3
    
    %% OCP connections - Purple
    O1 --> O2
    O1 --> O3
    
    %% LSP connections - Teal
    L1 --> L2
    
    %% ISP connections - Green
    I1 --> I2
    I2 --> I3
    
    %% DIP connections - Orange
    D1 --> D2
    D2 --> D3
    
    %% Apply linkStyle
    linkStyle 0,1 stroke:#1976d2,stroke-width:3px
    linkStyle 2,3 stroke:#7b1fa2,stroke-width:3px
    linkStyle 4 stroke:#00695c,stroke-width:3px
    linkStyle 5,6 stroke:#388e3c,stroke-width:3px
    linkStyle 7,8 stroke:#f57c00,stroke-width:3px
    
    %% Define node classes
    classDef srpStyle fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef ocpStyle fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef lspStyle fill:#e0f2f1,stroke:#00695c,stroke-width:2px
    classDef ispStyle fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    classDef dipStyle fill:#fff8e1,stroke:#f57c00,stroke-width:2px
    
    %% Apply classes
    class S1,S2,S3 srpStyle
    class O1,O2,O3 ocpStyle
    class L1,L2 lspStyle
    class I1,I2,I3 ispStyle
    class D1,D2,D3 dipStyle
    
    %% Style subgraphs
    style SRP fill:#e8f4fd,stroke:#1976d2,stroke-width:3px,color:#000
    style OCP fill:#f8f0ff,stroke:#7b1fa2,stroke-width:3px,color:#000
    style LSP fill:#f0fffe,stroke:#00695c,stroke-width:3px,color:#000
    style ISP fill:#f0f8f0,stroke:#388e3c,stroke-width:3px,color:#000
    style DIP fill:#fff4e6,stroke:#f57c00,stroke-width:3px,color:#000
```

### Bridged Architecture Pattern

The **Bridged Architecture** pattern uses Protocol-based structural typing to create loosely coupled, testable components:

```python
from typing import Protocol, Any, runtime_checkable

@runtime_checkable
class QueryableProtocol(Protocol):
    """Protocol defining queryable database interface."""
    
    def execute(self, sql: str, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        """Execute query and return results."""
        ...
    
    def execute_many(self, sql: str, param_list: list[dict[str, Any]]) -> int:
        """Execute batch operations."""
        ...

@runtime_checkable
class AttachableProtocol(Protocol):
    """Protocol for databases supporting attachment."""
    
    def attach(self, alias: str, connection_string: str) -> None:
        """Attach external database."""
        ...
    
    def detach(self, alias: str) -> None:
        """Detach database."""
        ...
```

---

## 🗺️ System Architecture Diagram

[Back to TOC](#-table-of-contents)

### High-Level Component Architecture

```mermaid
graph TB
    subgraph CLIENT ["🌐    Client    Applications"]
        C1[Web Browser]
        C2[Python SDK]
        C3[REST Clients]
        C4[CLI Tools]
    end
    
    subgraph GATEWAY ["🔀    API    Gateway    Layer"]
        G1[NGINX<br/>Reverse Proxy]
        G2[Rate Limiting]
        G3[SSL Termination]
        G4[Load Balancing]
    end
    
    subgraph APPLICATION ["🚀    Application    Layer"]
        A1[FastAPI Router]
        A2[Pydantic Validators]
        A3[Business Logic]
        A4[Error Handlers]
    end
    
    subgraph QUERY ["🦆    Query    Engine    Layer"]
        Q1[DuckDB Manager]
        Q2[Connection Pool]
        Q3[Query Optimizer]
        Q4[Attachment Manager]
    end
    
    subgraph STORAGE ["💾    Storage    Layer"]
        ST1[(PostgreSQL 18<br/>pgvector<br/>pg_duckdb)]
        ST2[(DuckDB<br/>Analytics DB)]
        ST3[(SQLite3<br/>Local Cache)]
        ST4[(MySQL 8.4<br/>Legacy)]
    end
    
    subgraph AI ["🤖    AI/ML    Services"]
        AI1[Ollama Gateway]
        AI2[Text-to-SQL]
        AI3[Embedding Generator]
        AI4[Query Explainer]
    end
    
    subgraph MONITORING ["📊    Observability"]
        M1[Prometheus]
        M2[Grafana]
        M3[Structlog]
        M4[Distributed Tracing]
    end
    
    %% Client to Gateway - Blue (ingestion)
    C1 --> G1
    C2 --> G1
    C3 --> G1
    C4 --> G1
    
    %% Gateway processing - Purple
    G1 --> G2
    G2 --> G3
    G3 --> G4
    G4 --> A1
    
    %% Application layer - Purple
    A1 --> A2
    A2 --> A3
    A3 --> A4
    A4 --> Q1
    
    %% Query engine - Teal
    Q1 --> Q2
    Q2 --> Q3
    Q3 --> Q4
    
    %% Storage connections - Green
    Q4 --> ST1
    Q4 --> ST2
    Q4 --> ST3
    Q4 -.-> ST4
    
    %% AI connections - Orange
    A3 --> AI1
    AI1 --> AI2
    AI1 --> AI3
    AI1 --> AI4
    AI2 --> Q1
    AI3 --> ST1
    
    %% Monitoring - Indigo (final output)
    A3 --> M3
    Q1 --> M1
    M1 --> M2
    M3 --> M4
    
    %% Apply linkStyle
    linkStyle 0,1,2,3 stroke:#1976d2,stroke-width:3px
    linkStyle 4,5,6,7,8,9,10,11 stroke:#7b1fa2,stroke-width:3px
    linkStyle 12,13,14 stroke:#00695c,stroke-width:3px
    linkStyle 15,16,17,18 stroke:#388e3c,stroke-width:3px
    linkStyle 19,20,21,22,23,24 stroke:#f57c00,stroke-width:3px
    linkStyle 25,26,27,28 stroke:#3f51b5,stroke-width:4px
    
    %% Define node classes
    classDef clientStyle fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef gatewayStyle fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    classDef appStyle fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef queryStyle fill:#e0f2f1,stroke:#00695c,stroke-width:2px
    classDef storageStyle fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
    classDef aiStyle fill:#fff8e1,stroke:#f57c00,stroke-width:2px
    classDef monitorStyle fill:#e8eaf6,stroke:#3f51b5,stroke-width:2px
    
    %% Apply classes
    class C1,C2,C3,C4 clientStyle
    class G1,G2,G3,G4 gatewayStyle
    class A1,A2,A3,A4 appStyle
    class Q1,Q2,Q3,Q4 queryStyle
    class ST1,ST2,ST3,ST4 storageStyle
    class AI1,AI2,AI3,AI4 aiStyle
    class M1,M2,M3,M4 monitorStyle
    
    %% Style subgraphs
    style CLIENT fill:#e8f4fd,stroke:#1976d2,stroke-width:3px,color:#000
    style GATEWAY fill:#f0f8f0,stroke:#388e3c,stroke-width:3px,color:#000
    style APPLICATION fill:#f8f0ff,stroke:#7b1fa2,stroke-width:3px,color:#000
    style QUERY fill:#f0fffe,stroke:#00695c,stroke-width:3px,color:#000
    style STORAGE fill:#e8f4fd,stroke:#1976d2,stroke-width:3px,color:#000
    style AI fill:#fff4e6,stroke:#f57c00,stroke-width:3px,color:#000
    style MONITORING fill:#e8eaf6,stroke:#3f51b5,stroke-width:3px,color:#000
```

### Data Flow Architecture

```mermaid
graph LR
    subgraph INGESTION ["📥    Data    Ingestion"]
        I1[CSV Files]
        I2[Parquet Files]
        I3[JSON Streams]
        I4[API Sources]
    end
    
    subgraph PROCESSING ["⚙️    DuckDB    Processing"]
        P1[Schema Discovery]
        P2[Type Inference]
        P3[Query Optimization]
        P4[Vectorized Execution]
    end
    
    subgraph STORAGE ["💾    Persistent    Storage"]
        S1[PostgreSQL<br/>Structured Data]
        S2[DuckDB<br/>Analytics]
        S3[Object Storage<br/>Raw Files]
    end
    
    subgraph SERVING ["📤    Data    Serving"]
        V1[REST API]
        V2[GraphQL]
        V3[gRPC]
        V4[WebSocket]
    end
    
    %% Ingestion flows - Blue
    I1 --> P1
    I2 --> P1
    I3 --> P2
    I4 --> P2
    
    %% Processing flows - Purple
    P1 --> P3
    P2 --> P3
    P3 --> P4
    
    %% Storage flows - Green
    P4 --> S1
    P4 --> S2
    P4 --> S3
    
    %% Serving flows - Indigo
    S1 --> V1
    S2 --> V2
    S3 --> V3
    S1 --> V4
    
    %% Apply linkStyle
    linkStyle 0,1,2,3 stroke:#1976d2,stroke-width:3px
    linkStyle 4,5,6 stroke:#7b1fa2,stroke-width:3px
    linkStyle 7,8,9 stroke:#388e3c,stroke-width:3px
    linkStyle 10,11,12,13 stroke:#3f51b5,stroke-width:4px
    
    %% Define node classes
    classDef ingestStyle fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef processStyle fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef storageStyle fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    classDef servingStyle fill:#e8eaf6,stroke:#3f51b5,stroke-width:3px
    
    %% Apply classes
    class I1,I2,I3,I4 ingestStyle
    class P1,P2,P3,P4 processStyle
    class S1,S2,S3 storageStyle
    class V1,V2,V3,V4 servingStyle
    
    %% Style subgraphs
    style INGESTION fill:#e8f4fd,stroke:#1976d2,stroke-width:3px,color:#000
    style PROCESSING fill:#f8f0ff,stroke:#7b1fa2,stroke-width:3px,color:#000
    style STORAGE fill:#f0f8f0,stroke:#388e3c,stroke-width:3px,color:#000
    style SERVING fill:#e8eaf6,stroke:#3f51b5,stroke-width:3px,color:#000
```

---

## 🔄 Data Flow & Sequence Diagrams

[Back to TOC](#-table-of-contents)

### Query Execution Flow

```mermaid
sequenceDiagram
    participant C as 🌐 Client
    participant N as 🔀 NGINX
    participant A as 🚀 FastAPI
    participant V as ✅ Pydantic
    participant D as 🦆 DuckDB
    participant PG as 🐘 PostgreSQL
    participant L as 📊 Logger

    Note over C,L: Standard SQL Query Execution Flow

    C->>+N: POST /api/v1/query<br/>{sql, database, params}
    N->>N: 🔒 Rate limit check
    N->>N: 🔍 Request validation
    N->>+A: Forward validated request
    
    A->>+V: Validate QueryRequest
    V->>V: 🛡️ SQL injection check
    V->>V: 📏 Length validation
    V->>V: 🎯 Type coercion
    V-->>-A: Validated model
    
    A->>+L: Log query start<br/>(correlation_id)
    L-->>-A: Logged
    
    A->>+D: execute_query(sql, params)
    
    alt Target: PostgreSQL
        D->>D: 🔍 Parse SQL
        D->>D: 🎯 Route to pg attachment
        D->>+PG: Execute via ATTACH
        PG->>PG: 🔐 Permission check
        PG->>PG: ⚡ Query execution
        PG-->>-D: Result set
    else Target: DuckDB Native
        D->>D: 🚀 Vectorized execution
        D-->>D: Result set
    end
    
    D->>D: 📊 Collect metrics<br/>(rows, time)
    D-->>-A: QueryResult
    
    A->>+V: Serialize response
    V-->>-A: JSON response
    
    A->>+L: Log query complete<br/>(metrics)
    L-->>-A: Logged
    
    A-->>-N: 200 OK + results
    N-->>-C: Response

    Note over C,L: Total latency: request validation + execution + serialization
```

### LLM-Enhanced Query Flow

```mermaid
sequenceDiagram
    participant C as 🌐 Client
    participant A as 🚀 FastAPI
    participant LLM as 🤖 Ollama
    participant D as 🦆 DuckDB
    participant PG as 🐘 PostgreSQL
    participant L as 📊 Logger

    Note over C,L: Natural Language to SQL Flow

    C->>+A: POST /api/v1/llm-query<br/>{natural_language_query}
    
    A->>+L: Log NL query start
    L-->>-A: correlation_id
    
    A->>+LLM: Generate SQL prompt:<br/>"Convert to SQL: {query}"
    LLM->>LLM: 🧠 LLM inference
    LLM->>LLM: 📝 SQL generation
    LLM-->>-A: Generated SQL + confidence
    
    alt Confidence < 0.7
        A->>+LLM: Request clarification
        LLM-->>-A: Clarifying questions
        A-->>C: 400 Bad Request<br/>{clarification_needed}
    else Confidence >= 0.7
        A->>+D: execute_query(generated_sql)
        
        D->>+PG: Execute query
        PG->>PG: ⚡ Query execution
        PG-->>-D: Results
        
        D-->>-A: QueryResult
        
        A->>+LLM: Explain results:<br/>"Summarize {results}"
        LLM->>LLM: 📊 Generate explanation
        LLM-->>-A: Natural language summary
        
        A->>+L: Log success<br/>(NL query, SQL, results)
        L-->>-A: Logged
        
        A-->>-C: 200 OK<br/>{sql, results, explanation}
    end

    Note over C,L: LLM adds intelligence layer:<br/>NL→SQL + Result explanation
```

### Database Attachment Flow

```mermaid
sequenceDiagram
    participant C as 🌐 Client
    participant A as 🚀 FastAPI
    participant V as ✅ Pydantic
    participant DM as 🦆 DuckDBManager
    participant AM as 🔌 AttachmentManager
    participant EXT as 📦 DuckDB<br/>Extensions
    participant MY as 💾 MySQL

    Note over C,MY: Dynamic Database Attachment Process

    C->>+A: POST /api/v1/attach<br/>{alias, db_type, conn_string}
    
    A->>+V: Validate AttachDatabaseRequest
    V->>V: 🔍 Check alias format
    V->>V: 🚫 Reject reserved names
    V->>V: ✅ Validate db_type enum
    V-->>-A: Validated model
    
    A->>+DM: attach_database(alias, type, conn)
    
    DM->>+AM: check_attachment_exists(alias)
    AM-->>-DM: not_exists
    
    DM->>+EXT: Load extension:<br/>LOAD mysql
    EXT->>EXT: 📦 Install if needed
    EXT->>EXT: 🔓 Load into memory
    EXT-->>-DM: Extension loaded
    
    DM->>+MY: Test connection
    MY->>MY: 🔐 Authenticate
    MY->>MY: 🔍 Verify database exists
    MY-->>-DM: Connection OK
    
    DM->>DM: ATTACH '{conn_string}'<br/>AS {alias} (TYPE MYSQL)
    
    DM->>+AM: register_attachment(alias, metadata)
    AM->>AM: 💾 Store in registry
    AM-->>-DM: Registered
    
    DM-->>-A: AttachmentStatus(success)
    
    A-->>-C: 200 OK<br/>{status, alias, message}

    Note over C,MY: Attachment persists for session<br/>Zero-copy access to MySQL data
```

### Cross-Database Query Flow

```mermaid
sequenceDiagram
    participant C as 🌐 Client
    participant D as 🦆 DuckDB
    participant PG as 🐘 PostgreSQL
    participant MY as 💾 MySQL
    participant SQ as 💿 SQLite

    Note over C,SQ: Federated Query Across Multiple Databases

    C->>+D: SELECT pg.users.name,<br/>mysql.orders.total,<br/>sqlite.cache.score<br/>FROM pg.users<br/>JOIN mysql.orders<br/>JOIN sqlite.cache

    D->>D: 🧠 Parse federated query
    D->>D: 🎯 Optimize join strategy
    D->>D: 📊 Estimate cardinalities
    
    par Parallel Data Fetch
        D->>+PG: SELECT id, name<br/>FROM users<br/>WHERE active = true
        PG->>PG: 🔍 Index scan
        PG-->>-D: 1000 rows
    and
        D->>+MY: SELECT user_id, total<br/>FROM orders<br/>WHERE date > '2024-01-01'
        MY->>MY: 🔍 Index scan
        MY-->>-D: 1500 rows
    and
        D->>+SQ: SELECT user_id, score<br/>FROM cache
        SQ->>SQ: 📊 Full scan
        SQ-->>-D: 800 rows
    end
    
    D->>D: 🔗 Hash join (users ⋈ orders)
    D->>D: 🔗 Merge join (result ⋈ cache)
    D->>D: 📊 Apply filters & aggregations
    D->>D: 🎨 Format result set
    
    D-->>-C: Combined result (750 rows)

    Note over C,SQ: DuckDB acts as query coordinator<br/>Pushes predicates to source databases<br/>Minimizes data transfer
```

### Vector Similarity Search Flow

```mermaid
sequenceDiagram
    participant C as 🌐 Client
    participant A as 🚀 FastAPI
    participant LLM as 🤖 Ollama
    participant PG as 🐘 PostgreSQL<br/>(pgvector)
    participant IVF as 🗂️ IVFFlat<br/>Index

    Note over C,IVF: Semantic Search with Vector Embeddings

    C->>+A: POST /api/v1/search<br/>{query: "machine learning"}
    
    A->>+LLM: Generate embedding:<br/>"machine learning"
    LLM->>LLM: 🧠 Encode to 1536-dim vector
    LLM-->>-A: [0.123, 0.456, ..., 0.789]
    
    A->>+PG: SELECT id, chunk_text,<br/>1 - (embedding <=> $1) AS similarity<br/>FROM embeddings.document_vectors<br/>ORDER BY embedding <=> $1<br/>LIMIT 10
    
    PG->>+IVF: Vector similarity search
    IVF->>IVF: 🔍 Find nearest cluster
    IVF->>IVF: 📊 Scan cluster vectors
    IVF->>IVF: 📐 Calculate cosine distances
    IVF-->>-PG: Top 10 matches
    
    PG->>PG: 📊 Fetch metadata
    PG->>PG: 🎯 Apply filters
    PG-->>-A: Result set with similarities
    
    A->>A: 🎨 Enrich with context
    A-->>-C: 200 OK<br/>{results, similarities}

    Note over C,IVF: IVFFlat index provides<br/>approximate nearest neighbor (ANN)<br/>search with ~95% recall
```

[Back to TOC](#-table-of-contents)

---

## 📦 Docker Infrastructure Configuration

[Back to TOC](#-table-of-contents)

### Complete Docker Compose Stack

```yaml
version: '3.8'

# ==============================================================================
# POSTGRESQL 18 WITH PGVECTOR AND PG_DUCKDB
# ==============================================================================
services:
  postgres18:
    image: pgvector/pgvector:pg18
    container_name: postgres18-vector
    hostname: postgres18
    
    environment:
      # Core configuration
      POSTGRES_USER: pgadmin
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: llm_analytics
      POSTGRES_INITDB_ARGS: "-E UTF8 --locale=C"
      
      # Extensions
      SHARED_PRELOAD_LIBRARIES: 'pg_duckdb,vector'
      
      # Performance tuning
      POSTGRES_SHARED_BUFFERS: '2GB'
      POSTGRES_EFFECTIVE_CACHE_SIZE: '6GB'
      POSTGRES_WORK_MEM: '128MB'
      POSTGRES_MAINTENANCE_WORK_MEM: '512MB'
      POSTGRES_MAX_CONNECTIONS: 200
      POSTGRES_MAX_WAL_SIZE: '2GB'
      POSTGRES_MIN_WAL_SIZE: '1GB'
      
      # Logging
      POSTGRES_LOG_STATEMENT: 'mod'
      POSTGRES_LOG_DURATION: 'on'
      POSTGRES_LOG_MIN_DURATION_STATEMENT: 1000
    
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-scripts/postgres:/docker-entrypoint-initdb.d:ro
      - ./shared-data:/shared-data
      - ./backups/postgres:/backups
    
    ports:
      - "5432:5432"
    
    networks:
      llm-network:
        ipv4_address: 172.28.0.10
    
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U pgadmin -d llm_analytics"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    
    deploy:
      resources:
        limits:
          cpus: '4.0'
          memory: 8G
        reservations:
          cpus: '2.0'
          memory: 4G
    
    restart: unless-stopped
    
    labels:
      com.docker.compose.project: "llm-sql-integration"
      service.role: "database"
      service.type: "postgresql"

  # ==============================================================================
  # DUCKDB QUERY ENGINE (PYTHON 3.14 + UV + RUFF)
  # ==============================================================================
  duckdb-server:
    build:
      context: ./duckdb-service
      dockerfile: Dockerfile
      args:
        PYTHON_VERSION: "3.14"
        UV_VERSION: "latest"
        BUILD_DATE: ${BUILD_DATE:-2024-02-04}
        VCS_REF: ${VCS_REF:-dev}
      target: production
    
    container_name: duckdb-query-engine
    hostname: duckdb
    
    environment:
      # PostgreSQL connection
      POSTGRES_HOST: postgres18
      POSTGRES_PORT: 5432
      POSTGRES_USER: pgadmin
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: llm_analytics
      POSTGRES_SSLMODE: prefer
      
      # MySQL connection (optional)
      MYSQL_HOST: ${MYSQL_HOST:-mysql}
      MYSQL_PORT: ${MYSQL_PORT:-3306}
      MYSQL_USER: ${MYSQL_USER:-root}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      MYSQL_DB: ${MYSQL_DB:-legacy_analytics}
      
      # DuckDB configuration
      DUCKDB_DATABASE_PATH: /data/analytics.duckdb
      DUCKDB_THREADS: ${DUCKDB_THREADS:-8}
      DUCKDB_MEMORY_LIMIT: ${DUCKDB_MEMORY_LIMIT:-16GB}
      DUCKDB_MAX_MEMORY: ${DUCKDB_MAX_MEMORY:-16GB}
      DUCKDB_TEMP_DIRECTORY: /tmp/duckdb
      DUCKDB_ACCESS_MODE: READ_WRITE
      
      # Application configuration
      APP_NAME: "DuckDB Query Service"
      APP_VERSION: "1.0.0"
      API_PREFIX: "/api/v1"
      WORKERS: 4
      
      # Python environment
      PYTHONUNBUFFERED: 1
      PYTHONDONTWRITEBYTECODE: 1
      PYTHONPATH: /app/src
      UV_SYSTEM_PYTHON: 1
      
      # Logging
      LOG_LEVEL: ${LOG_LEVEL:-INFO}
      LOG_FORMAT: json
      LOG_OUTPUT: stdout
    
    volumes:
      - duckdb_data:/data
      - ./shared-data:/shared-data
      - ./duckdb-queries:/queries:ro
      - ./logs/duckdb:/app/logs
    
    ports:
      - "8001:8001"
    
    networks:
      llm-network:
        ipv4_address: 172.28.0.20
    
    depends_on:
      postgres18:
        condition: service_healthy
    
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8001/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 20s
    
    deploy:
      resources:
        limits:
          cpus: '8.0'
          memory: 16G
        reservations:
          cpus: '4.0'
          memory: 8G
    
    restart: unless-stopped
    
    labels:
      service.role: "query-engine"
      service.type: "duckdb"

  # ==============================================================================
  # MYSQL 8.4 (OPTIONAL LEGACY INTEGRATION)
  # ==============================================================================
  mysql:
    image: mysql:8.4
    container_name: mysql-legacy
    hostname: mysql
    
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: legacy_analytics
      MYSQL_USER: ${MYSQL_USER:-analyst}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      
      # Performance tuning
      MYSQL_INNODB_BUFFER_POOL_SIZE: '2G'
      MYSQL_MAX_CONNECTIONS: 200
      MYSQL_QUERY_CACHE_SIZE: 0
      MYSQL_INNODB_FLUSH_LOG_AT_TRX_COMMIT: 2
    
    volumes:
      - mysql_data:/var/lib/mysql
      - ./init-scripts/mysql:/docker-entrypoint-initdb.d:ro
      - ./backups/mysql:/backups
    
    ports:
      - "3306:3306"
    
    networks:
      llm-network:
        ipv4_address: 172.28.0.30
    
    profiles:
      - with-mysql
    
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u", "root", "-p${MYSQL_ROOT_PASSWORD}"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 4G
    
    restart: unless-stopped

  # ==============================================================================
  # OLLAMA LLM GATEWAY (GPU-ENABLED)
  # ==============================================================================
  llm-gateway:
    image: ollama/ollama:latest
    container_name: llm-gateway
    hostname: llm-gateway
    
    environment:
      OLLAMA_HOST: "0.0.0.0:11434"
      OLLAMA_MODELS: "/models"
      OLLAMA_KEEP_ALIVE: "5m"
      OLLAMA_NUM_PARALLEL: 2
      OLLAMA_MAX_LOADED_MODELS: 3
      OLLAMA_FLASH_ATTENTION: true
    
    volumes:
      - ollama_models:/models
      - ./shared-data:/shared-data
    
    ports:
      - "11434:11434"
    
    networks:
      llm-network:
        ipv4_address: 172.28.0.40
    
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    
    restart: unless-stopped
    
    labels:
      service.role: "ai-inference"
      service.type: "ollama"

  # ==============================================================================
  # FASTAPI APPLICATION LAYER (PYTHON 3.14 + UV + PYDANTIC V2)
  # ==============================================================================
  api-server:
    build:
      context: ./api-service
      dockerfile: Dockerfile
      args:
        PYTHON_VERSION: "3.14"
        UV_VERSION: "latest"
      target: production
    
    container_name: llm-sql-api
    hostname: api-server
    
    environment:
      # Service URLs
      DUCKDB_URL: "http://duckdb-server:8001"
      LLM_URL: "http://llm-gateway:11434"
      POSTGRES_URL: "postgresql://pgadmin:${POSTGRES_PASSWORD}@postgres18:5432/llm_analytics"
      
      # Application config
      APP_NAME: "LLM-SQL API"
      APP_VERSION: "1.0.0"
      API_PREFIX: "/api/v1"
      CORS_ORIGINS: ${CORS_ORIGINS:-*}
      
      # Security
      SECRET_KEY: ${SECRET_KEY}
      ACCESS_TOKEN_EXPIRE_MINUTES: 30
      
      # Python environment
      PYTHONUNBUFFERED: 1
      PYTHONDONTWRITEBYTECODE: 1
      LOG_LEVEL: ${LOG_LEVEL:-INFO}
    
    volumes:
      - ./api-service:/app
      - ./shared-data:/shared-data
      - ./logs/api:/app/logs
    
    ports:
      - "8000:8000"
    
    networks:
      llm-network:
        ipv4_address: 172.28.0.50
    
    depends_on:
      duckdb-server:
        condition: service_healthy
      llm-gateway:
        condition: service_started
      postgres18:
        condition: service_healthy
    
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 20s
    
    deploy:
      resources:
        limits:
          cpus: '4.0'
          memory: 4G
    
    restart: unless-stopped

  # ==============================================================================
  # NGINX REVERSE PROXY
  # ==============================================================================
  nginx:
    image: nginx:alpine
    container_name: llm-sql-proxy
    hostname: nginx
    
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - nginx_logs:/var/log/nginx
      - ./nginx/ssl:/etc/nginx/ssl:ro
    
    ports:
      - "80:80"
      - "443:443"
    
    networks:
      llm-network:
        ipv4_address: 172.28.0.60
    
    depends_on:
      - duckdb-server
      - llm-gateway
      - api-server
    
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
    
    restart: unless-stopped

# ==============================================================================
# DOCKER VOLUMES
# ==============================================================================
volumes:
  postgres_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: ${PWD}/volumes/postgres
  
  duckdb_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: ${PWD}/volumes/duckdb
  
  mysql_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: ${PWD}/volumes/mysql
  
  ollama_models:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: ${PWD}/volumes/ollama
  
  nginx_logs:
    driver: local

# ==============================================================================
# DOCKER NETWORKS
# ==============================================================================
networks:
  llm-network:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.28.0.0/16
          gateway: 172.28.0.1
    driver_opts:
      com.docker.network.bridge.name: br-llm-sql
      com.docker.network.driver.mtu: 1500
    enable_ipv6: false
```

[Back to TOC](#-table-of-contents)

---

## 🐍 Python Service Implementation - Part 1

[Back to TOC](#-table-of-contents)

### Directory Structure & Project Setup

```
duckdb-service/
├── Dockerfile                  # Multi-stage build with uv
├── pyproject.toml             # uv dependency management
├── uv.lock                    # Lockfile for reproducibility
├── ruff.toml                  # Ruff configuration
├── .python-version            # Python 3.14 specification
├── src/
│   ├── __init__.py
│   ├── main.py               # FastAPI application entry
│   ├── config.py             # Pydantic Settings
│   ├── models/
│   │   ├── __init__.py
│   │   ├── requests.py       # Request models
│   │   └── responses.py      # Response models
│   ├── services/
│   │   ├── __init__.py
│   │   ├── duckdb_manager.py        # Connection management
│   │   ├── attachment_manager.py    # Database attachments
│   │   └── query_executor.py        # Query execution
│   ├── protocols/
│   │   ├── __init__.py
│   │   └── database.py       # Protocol interfaces
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── query.py          # Query endpoints
│   │   ├── attachment.py     # Attachment endpoints
│   │   └── health.py         # Health checks
│   └── utils/
│       ├── __init__.py
│       ├── logging.py        # Structured logging
│       └── metrics.py        # Prometheus metrics
└── tests/
    ├── __init__.py
    ├── conftest.py           # Pytest fixtures
    ├── test_duckdb.py
    └── test_api.py
```

### Dockerfile with Multi-Stage Build

```dockerfile
# syntax=docker/dockerfile:1.4

# ==============================================================================
# STAGE 1: Base Python 3.14 with uv
# ==============================================================================
FROM python:3.14-slim AS base

# Metadata
LABEL maintainer="peter.heller@qc.cuny.edu"
LABEL description="DuckDB Query Service with Python 3.14, uv, and Ruff"
LABEL version="1.0.0"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app/src \
    UV_SYSTEM_PYTHON=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_CACHE_DIR=/root/.cache/uv \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install uv from official source
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# ==============================================================================
# STAGE 2: Development dependencies
# ==============================================================================
FROM base AS development

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install all dependencies including dev
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system -r pyproject.toml --all-extras

# Copy application code
COPY src/ ./src/
COPY tests/ ./tests/
COPY ruff.toml ./

# Run linting and tests
RUN ruff check src/ && \
    ruff format --check src/

# ==============================================================================
# STAGE 3: Production build
# ==============================================================================
FROM base AS production

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install production dependencies only
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system -r pyproject.toml

# Copy application code only (no tests)
COPY src/ ./src/

# Create non-root user
RUN useradd -m -u 1000 duckdb && \
    chown -R duckdb:duckdb /app

USER duckdb

# Expose port
EXPOSE 8001

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
    CMD curl -f http://localhost:8001/health || exit 1

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--workers", "4", "--log-level", "info"]
```

### pyproject.toml with uv

```toml
[project]
name = "duckdb-query-service"
version = "1.0.0"
description = "DuckDB unified query engine with multi-database attachments"
authors = [{name = "Peter Heller", email = "peter.heller@qc.cuny.edu"}]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.14"
keywords = ["duckdb", "postgresql", "analytics", "fastapi", "pydantic"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.14",
    "Topic :: Database",
]

dependencies = [
    "fastapi>=0.109.0",
    "uvicorn[standard]>=0.27.0",
    "duckdb>=0.10.0",
    "psycopg2-binary>=2.9.9",
    "pymysql>=1.1.0",
    "pydantic>=2.6.0",
    "pydantic-settings>=2.1.0",
    "python-dotenv>=1.0.0",
    "structlog>=24.1.0",
    "httpx>=0.26.0",
    "prometheus-client>=0.19.0",
    "python-json-logger>=2.0.7",
]

[project.optional-dependencies]
dev = [
    "ruff>=0.1.14",
    "pytest>=8.0.0",
    "pytest-asyncio>=0.23.0",
    "pytest-cov>=4.1.0",
    "mypy>=1.8.0",
    "types-psycopg2",
]

[project.urls]
Homepage = "https://github.com/ph3ll3r/duckdb-query-service"
Repository = "https://github.com/ph3ll3r/duckdb-query-service"
Documentation = "https://github.com/ph3ll3r/duckdb-query-service/docs"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src"]

[tool.uv]
dev-dependencies = [
    "ruff>=0.1.14",
    "pytest>=8.0.0",
    "pytest-asyncio>=0.23.0",
    "pytest-cov>=4.1.0",
    "mypy>=1.8.0",
]
```

### ruff.toml Configuration

```toml
# Ruff configuration for Python 3.14
target-version = "py314"
line-length = 100
indent-width = 4

# Enable comprehensive rule sets
select = [
    "E",     # pycodestyle errors
    "W",     # pycodestyle warnings
    "F",     # Pyflakes
    "I",     # isort
    "B",     # flake8-bugbear
    "C4",    # flake8-comprehensions
    "UP",    # pyupgrade
    "ARG",   # flake8-unused-arguments
    "SIM",   # flake8-simplify
    "TCH",   # flake8-type-checking
    "PTH",   # flake8-use-pathlib
    "ERA",   # eradicate
    "PL",    # Pylint
    "RUF",   # Ruff-specific rules
    "PERF",  # Perflint
    "FURB",  # refurb
]

ignore = [
    "E501",   # line too long (handled by formatter)
    "B008",   # do not perform function calls in argument defaults
    "PLR0913", # too many arguments
    "PLR2004", # magic value comparison
]

# Exclude patterns
exclude = [
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
    "venv",
    ".venv",
]

[lint.per-file-ignores]
"__init__.py" = ["F401"]  # Allow unused imports
"tests/*" = ["S101", "PLR2004"]  # Allow assert and magic values in tests

[lint.isort]
known-first-party = ["src"]
section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]

[lint.flake8-type-checking]
runtime-evaluated-base-classes = ["pydantic.BaseModel", "pydantic_settings.BaseSettings"]

[format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"

[lint.pydocstyle]
convention = "google"
```

### Configuration Management (src/config.py)

```python
"""
Application configuration using Pydantic Settings v2.

This module implements the configuration layer following D⁴ methodology,
ensuring type-safe, validated, and environment-aware settings management.
"""

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field, PostgresDsn, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    """
    PostgreSQL database configuration.
    
    Implements SRP: Manages only PostgreSQL connection parameters.
    """

    host: str = Field(
        default="postgres18",
        description="PostgreSQL host",
        json_schema_extra={"env": "POSTGRES_HOST"},
    )
    port: int = Field(
        default=5432,
        ge=1,
        le=65535,
        description="PostgreSQL port",
    )
    user: str = Field(
        default="pgadmin",
        min_length=1,
        description="PostgreSQL user",
    )
    password: str = Field(
        description="PostgreSQL password",
        json_schema_extra={"secret": True},
    )
    database: str = Field(
        default="llm_analytics",
        min_length=1,
        description="PostgreSQL database name",
    )
    sslmode: Literal["disable", "allow", "prefer", "require", "verify-ca", "verify-full"] = Field(
        default="prefer",
        description="PostgreSQL SSL mode",
    )

    model_config = SettingsConfigDict(
        env_prefix="POSTGRES_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def connection_string(self) -> str:
        """
        Build PostgreSQL connection string for DuckDB attachment.
        
        Returns:
            Formatted connection string compatible with DuckDB ATTACH.
        """
        return (
            f"dbname={self.database} "
            f"user={self.user} "
            f"password={self.password} "
            f"host={self.host} "
            f"port={self.port} "
            f"sslmode={self.sslmode}"
        )

    @property
    def dsn(self) -> str:
        """
        Build PostgreSQL DSN for direct connections.
        
        Returns:
            PostgreSQL DSN string.
        """
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class MySQLConfig(BaseSettings):
    """
    MySQL database configuration (optional).
    
    Implements OCP: Can be extended without modifying existing code.
    """

    host: str = Field(default="mysql", description="MySQL host")
    port: int = Field(default=3306, ge=1, le=65535, description="MySQL port")
    user: str = Field(default="root", min_length=1, description="MySQL user")
    password: str = Field(default="", description="MySQL password")
    database: str = Field(default="legacy_analytics", description="MySQL database name")

    model_config = SettingsConfigDict(
        env_prefix="MYSQL_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def connection_string(self) -> str:
        """
        Build MySQL connection string for DuckDB attachment.
        
        Returns:
            Formatted connection string.
        """
        return (
            f"host={self.host} "
            f"user={self.user} "
            f"password={self.password} "
            f"port={self.port} "
            f"database={self.database}"
        )


class DuckDBConfig(BaseSettings):
    """
    DuckDB engine configuration.
    
    Implements ISP: Focused interface for DuckDB-specific settings.
    """

    database_path: Path = Field(
        default=Path("/data/analytics.duckdb"),
        description="DuckDB file path",
    )
    threads: int = Field(
        default=8,
        ge=1,
        le=64,
        description="Number of threads",
    )
    memory_limit: str = Field(
        default="16GB",
        pattern=r"^\d+[KMGT]B$",
        description="Memory limit (e.g., 16GB, 512MB)",
    )
    temp_directory: Path = Field(
        default=Path("/tmp/duckdb"),
        description="Temporary directory",
    )
    access_mode: Literal["READ_ONLY", "READ_WRITE"] = Field(
        default="READ_WRITE",
        description="Database access mode",
    )

    model_config = SettingsConfigDict(
        env_prefix="DUCKDB_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @field_validator("database_path", "temp_directory")
    @classmethod
    def validate_path(cls, v: Path) -> Path:
        """Ensure parent directory exists."""
        v.parent.mkdir(parents=True, exist_ok=True)
        return v


class AppConfig(BaseSettings):
    """
    Application-level configuration.
    
    Implements DIP: High-level configuration depends on abstractions.
    """

    name: str = Field(default="DuckDB Query Service", description="Application name")
    version: str = Field(default="1.0.0", description="Application version")
    api_prefix: str = Field(default="/api/v1", description="API route prefix")
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO",
        description="Logging level",
    )
    log_format: Literal["json", "text"] = Field(
        default="json",
        description="Log output format",
    )
    workers: int = Field(
        default=4,
        ge=1,
        le=32,
        description="Number of uvicorn workers",
    )
    cors_origins: list[str] = Field(
        default=["*"],
        description="CORS allowed origins",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


class Settings(BaseSettings):
    """
    Main settings aggregator implementing composition.
    
    Follows D⁴ methodology: Clear domain boundaries with aggregated configuration.
    """

    app: AppConfig = Field(default_factory=AppConfig)
    postgres: DatabaseConfig = Field(default_factory=DatabaseConfig)
    mysql: MySQLConfig = Field(default_factory=MySQLConfig)
    duckdb: DuckDBConfig = Field(default_factory=DuckDBConfig)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @model_validator(mode="after")
    def validate_settings(self) -> "Settings":
        """Cross-field validation."""
        # Ensure DuckDB can create database file
        if not self.duckdb.database_path.parent.exists():
            self.duckdb.database_path.parent.mkdir(parents=True, exist_ok=True)
        
        return self


@lru_cache
def get_settings() -> Settings:
    """
    Get cached settings instance (Singleton pattern).
    
    Returns:
        Singleton Settings instance.
    """
    return Settings()
```

[Back to TOC](#-table-of-contents)

---

I'll continue with Part 2 in the next section. Would you like me to proceed with:
- Protocol definitions (database.py)
- Pydantic request/response models
- DuckDB manager service
- Attachment manager service