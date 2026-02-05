# 🐘 PostgreSQL18-DuckDB-SQLite3 Integration with LLM-SQL Architecture

## 🚀 Deployment & Operations Guide

[Back to TOC](#-table-of-contents)

### Deployment Architecture Overview

```mermaid
graph TB
    subgraph PREP ["📋    Pre-Deployment    Preparation"]
        P1[Environment Setup]
        P2[Directory Structure]
        P3[Configuration Files]
        P4[SSL Certificates]
    end
    
    subgraph BUILD ["🔨    Build    Phase"]
        B1[Docker Images]
        B2[Database Schemas]
        B3[Network Configuration]
        B4[Volume Initialization]
    end
    
    subgraph DEPLOY ["🚀    Deployment    Phase"]
        D1[PostgreSQL Service]
        D2[DuckDB Service]
        D3[API Service]
        D4[NGINX Proxy]
        D5[LLM Gateway]
    end
    
    subgraph VERIFY ["✅    Verification    Phase"]
        V1[Health Checks]
        V2[Connectivity Tests]
        V3[Sample Queries]
        V4[Load Testing]
    end
    
    subgraph MONITOR ["📊    Monitoring    Phase"]
        M1[Prometheus Setup]
        M2[Grafana Dashboards]
        M3[Log Aggregation]
        M4[Alerting Rules]
    end
    
    %% Preparation flows - Blue
    P1 --> P2
    P2 --> P3
    P3 --> P4
    
    %% Build flows - Purple
    P4 --> B1
    B1 --> B2
    B2 --> B3
    B3 --> B4
    
    %% Deployment flows - Green
    B4 --> D1
    D1 --> D2
    D2 --> D3
    D3 --> D4
    D4 --> D5
    
    %% Verification flows - Orange
    D5 --> V1
    V1 --> V2
    V2 --> V3
    V3 --> V4
    
    %% Monitoring flows - Indigo
    V4 --> M1
    M1 --> M2
    M2 --> M3
    M3 --> M4
    
    %% Apply linkStyle
    linkStyle 0,1,2 stroke:#1976d2,stroke-width:3px
    linkStyle 3,4,5,6 stroke:#7b1fa2,stroke-width:3px
    linkStyle 7,8,9,10,11 stroke:#388e3c,stroke-width:3px
    linkStyle 12,13,14,15 stroke:#f57c00,stroke-width:3px
    linkStyle 16,17,18,19 stroke:#3f51b5,stroke-width:4px
    
    %% Define node classes
    classDef prepStyle fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef buildStyle fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef deployStyle fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    classDef verifyStyle fill:#fff8e1,stroke:#f57c00,stroke-width:2px
    classDef monitorStyle fill:#e8eaf6,stroke:#3f51b5,stroke-width:3px
    
    %% Apply classes
    class P1,P2,P3,P4 prepStyle
    class B1,B2,B3,B4 buildStyle
    class D1,D2,D3,D4,D5 deployStyle
    class V1,V2,V3,V4 verifyStyle
    class M1,M2,M3,M4 monitorStyle
    
    %% Style subgraphs
    style PREP fill:#e8f4fd,stroke:#1976d2,stroke-width:3px,color:#000
    style BUILD fill:#f8f0ff,stroke:#7b1fa2,stroke-width:3px,color:#000
    style DEPLOY fill:#f0f8f0,stroke:#388e3c,stroke-width:3px,color:#000
    style VERIFY fill:#fff4e6,stroke:#f57c00,stroke-width:3px,color:#000
    style MONITOR fill:#e8eaf6,stroke:#3f51b5,stroke-width:3px,color:#000
```

---

### Step 1: Pre-Deployment Preparation

#### 1.1 System Requirements

**Hardware Requirements:**

| Component | Minimum | Recommended | Production |
|-----------|---------|-------------|------------|
| CPU Cores | 8 | 16 | 32+ |
| RAM | 16GB | 32GB | 64GB+ |
| Storage | 100GB SSD | 500GB NVMe | 1TB+ NVMe RAID |
| Network | 1Gbps | 10Gbps | 10Gbps+ |
| GPU | None | RTX 4090 | RTX 5090+ |

**Software Requirements:**

```bash
# Check Docker version
docker --version
# Required: Docker Engine 24.0+

# Check Docker Compose version
docker compose version
# Required: Docker Compose v2.20+

# Check NVIDIA Docker (for GPU support)
nvidia-smi
docker run --rm --gpus all nvidia/cuda:12.0-base nvidia-smi
# Required for LLM Gateway

# Check system resources
free -h
df -h
lscpu
```

#### 1.2 Create Directory Structure

```bash
#!/bin/bash
# setup-directories.sh - Create project directory structure

set -euo pipefail

PROJECT_ROOT="/opt/llm-sql-integration"
echo "🏗️  Creating project structure at: $PROJECT_ROOT"

# Create main directories
mkdir -p "$PROJECT_ROOT"/{volumes,init-scripts,nginx,shared-data,logs,backups}

# Create volume directories
mkdir -p "$PROJECT_ROOT"/volumes/{postgres,duckdb,mysql,ollama}

# Create init script directories
mkdir -p "$PROJECT_ROOT"/init-scripts/{postgres,mysql}

# Create nginx directories
mkdir -p "$PROJECT_ROOT"/nginx/{conf.d,ssl}

# Create service directories
mkdir -p "$PROJECT_ROOT"/{duckdb-service,api-service}
mkdir -p "$PROJECT_ROOT"/duckdb-service/{src,tests}
mkdir -p "$PROJECT_ROOT"/api-service/{src,tests}

# Create log directories
mkdir -p "$PROJECT_ROOT"/logs/{duckdb,api,nginx}

# Create backup directories
mkdir -p "$PROJECT_ROOT"/backups/{postgres,mysql,duckdb}

# Create query directories
mkdir -p "$PROJECT_ROOT"/duckdb-queries

# Set permissions
chmod -R 755 "$PROJECT_ROOT"/volumes
chmod -R 755 "$PROJECT_ROOT"/init-scripts
chmod -R 755 "$PROJECT_ROOT"/logs
chmod -R 755 "$PROJECT_ROOT"/backups

echo "✅ Directory structure created successfully"
tree -L 2 "$PROJECT_ROOT"
```

#### 1.3 Environment Configuration

Create `.env` file with production-ready secrets:

```bash
# .env - Environment Configuration
# ============================================================================
# SECURITY WARNING: Keep this file secure and never commit to version control
# ============================================================================

# PostgreSQL Configuration
POSTGRES_PASSWORD=$(openssl rand -base64 32)
POSTGRES_USER=pgadmin
POSTGRES_DB=llm_analytics
POSTGRES_SSLMODE=prefer

# MySQL Configuration (Optional)
MYSQL_ROOT_PASSWORD=$(openssl rand -base64 32)
MYSQL_USER=analyst
MYSQL_PASSWORD=$(openssl rand -base64 32)
MYSQL_HOST=mysql
MYSQL_PORT=3306
MYSQL_DB=legacy_analytics

# DuckDB Configuration
DUCKDB_THREADS=16
DUCKDB_MEMORY_LIMIT=32GB
DUCKDB_MAX_MEMORY=32GB

# Application Configuration
APP_NAME="LLM-SQL Integration"
APP_VERSION="1.0.0"
API_PREFIX=/api/v1
LOG_LEVEL=INFO
SECRET_KEY=$(openssl rand -hex 32)

# CORS Configuration
CORS_ORIGINS=https://yourdomain.com,https://api.yourdomain.com

# Build Configuration
BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ')
VCS_REF=$(git rev-parse --short HEAD 2>/dev/null || echo "dev")

# Network Configuration
SUBNET=172.28.0.0/16
GATEWAY=172.28.0.1

# Resource Limits
POSTGRES_MAX_CONNECTIONS=200
MYSQL_MAX_CONNECTIONS=200
```

**Generate and secure .env file:**

```bash
#!/bin/bash
# generate-env.sh - Generate secure .env file

cat > .env << 'EOF'
# PostgreSQL
POSTGRES_PASSWORD=$(openssl rand -base64 32)
POSTGRES_USER=pgadmin
POSTGRES_DB=llm_analytics

# MySQL
MYSQL_ROOT_PASSWORD=$(openssl rand -base64 32)
MYSQL_USER=analyst
MYSQL_PASSWORD=$(openssl rand -base64 32)

# Application
SECRET_KEY=$(openssl rand -hex 32)
LOG_LEVEL=INFO

# DuckDB
DUCKDB_THREADS=16
DUCKDB_MEMORY_LIMIT=32GB
EOF

# Set restrictive permissions
chmod 600 .env
chown $USER:$USER .env

echo "✅ .env file generated with secure passwords"
echo "⚠️  IMPORTANT: Back up this file securely!"
```

#### 1.4 SSL Certificate Setup

```bash
#!/bin/bash
# setup-ssl.sh - Generate self-signed SSL certificates for development

SSL_DIR="./nginx/ssl"
mkdir -p "$SSL_DIR"

# Generate private key
openssl genrsa -out "$SSL_DIR/server.key" 4096

# Generate CSR
openssl req -new -key "$SSL_DIR/server.key" \
    -out "$SSL_DIR/server.csr" \
    -subj "/C=US/ST=NewYork/L=Queens/O=CUNY/OU=ComputerScience/CN=localhost"

# Generate self-signed certificate (valid 365 days)
openssl x509 -req -days 365 \
    -in "$SSL_DIR/server.csr" \
    -signkey "$SSL_DIR/server.key" \
    -out "$SSL_DIR/server.crt"

# Generate DH parameters for enhanced security
openssl dhparam -out "$SSL_DIR/dhparam.pem" 2048

# Set permissions
chmod 600 "$SSL_DIR/server.key"
chmod 644 "$SSL_DIR/server.crt"
chmod 644 "$SSL_DIR/dhparam.pem"

echo "✅ SSL certificates generated"
echo "📄 Certificate: $SSL_DIR/server.crt"
echo "🔑 Private Key: $SSL_DIR/server.key"
echo "⚠️  For production, use Let's Encrypt or proper CA-signed certificates"
```

---

### Step 2: Database Initialization Scripts

#### 2.1 PostgreSQL Initialization

Create `init-scripts/postgres/01-extensions.sql`:

```sql
-- ============================================================================
-- PostgreSQL 18 Initialization Script
-- Extensions: pgvector, pg_duckdb
-- ============================================================================

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_duckdb;

-- Additional useful extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- ============================================================================
-- Schema Creation
-- ============================================================================

-- Embeddings schema for vector storage
CREATE SCHEMA IF NOT EXISTS embeddings;

-- Analytics schema for query logging
CREATE SCHEMA IF NOT EXISTS analytics;

-- Application schema for metadata
CREATE SCHEMA IF NOT EXISTS app_metadata;

-- ============================================================================
-- Vector Embeddings Tables
-- ============================================================================

CREATE TABLE IF NOT EXISTS embeddings.document_vectors (
    id SERIAL PRIMARY KEY,
    document_id INTEGER NOT NULL,
    chunk_text TEXT NOT NULL,
    embedding vector(1536) NOT NULL,  -- OpenAI ada-002 / text-embedding-3-small
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_metadata CHECK (jsonb_typeof(metadata) = 'object')
);

-- Create indexes for vector similarity search
CREATE INDEX IF NOT EXISTS idx_document_vectors_embedding 
ON embeddings.document_vectors 
USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);

-- GIN index for metadata queries
CREATE INDEX IF NOT EXISTS idx_document_vectors_metadata 
ON embeddings.document_vectors USING GIN (metadata);

-- B-tree index for document_id lookups
CREATE INDEX IF NOT EXISTS idx_document_vectors_document_id 
ON embeddings.document_vectors (document_id);

-- ============================================================================
-- Query Logging Tables
-- ============================================================================

CREATE TABLE IF NOT EXISTS analytics.query_logs (
    log_id SERIAL PRIMARY KEY,
    correlation_id UUID DEFAULT uuid_generate_v4(),
    user_query TEXT NOT NULL,
    generated_sql TEXT,
    execution_time_ms INTEGER CHECK (execution_time_ms >= 0),
    result_rows INTEGER CHECK (result_rows >= 0),
    llm_model VARCHAR(100),
    status VARCHAR(20) DEFAULT 'success' CHECK (status IN ('success', 'error', 'timeout')),
    error_message TEXT,
    query_hash VARCHAR(64),  -- SHA256 hash for deduplication
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    client_ip INET,
    user_agent TEXT
);

-- Indexes for query logs
CREATE INDEX IF NOT EXISTS idx_query_logs_created_at 
ON analytics.query_logs (created_at DESC);

CREATE INDEX IF NOT EXISTS idx_query_logs_status 
ON analytics.query_logs (status) WHERE status != 'success';

CREATE INDEX IF NOT EXISTS idx_query_logs_correlation_id 
ON analytics.query_logs (correlation_id);

CREATE INDEX IF NOT EXISTS idx_query_logs_query_hash 
ON analytics.query_logs (query_hash);

-- ============================================================================
-- Database Attachment Tracking
-- ============================================================================

CREATE TABLE IF NOT EXISTS app_metadata.database_attachments (
    attachment_id SERIAL PRIMARY KEY,
    alias VARCHAR(50) UNIQUE NOT NULL,
    db_type VARCHAR(20) NOT NULL CHECK (db_type IN ('postgres', 'mysql', 'sqlite')),
    connection_string TEXT NOT NULL,
    attached_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    detached_at TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    metadata JSONB DEFAULT '{}'::jsonb
);

CREATE INDEX IF NOT EXISTS idx_attachments_active 
ON app_metadata.database_attachments (is_active) WHERE is_active = TRUE;

-- ============================================================================
-- Triggers for Updated Timestamps
-- ============================================================================

CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_document_vectors_updated_at
    BEFORE UPDATE ON embeddings.document_vectors
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- Materialized View for Query Analytics
-- ============================================================================

CREATE MATERIALIZED VIEW IF NOT EXISTS analytics.query_stats_hourly AS
SELECT 
    DATE_TRUNC('hour', created_at) as hour,
    COUNT(*) as total_queries,
    COUNT(*) FILTER (WHERE status = 'success') as successful_queries,
    COUNT(*) FILTER (WHERE status = 'error') as failed_queries,
    AVG(execution_time_ms) as avg_execution_time_ms,
    PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY execution_time_ms) as p50_execution_time_ms,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY execution_time_ms) as p95_execution_time_ms,
    PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY execution_time_ms) as p99_execution_time_ms,
    AVG(result_rows) as avg_result_rows
FROM analytics.query_logs
GROUP BY DATE_TRUNC('hour', created_at);

-- Create index on materialized view
CREATE INDEX IF NOT EXISTS idx_query_stats_hourly_hour 
ON analytics.query_stats_hourly (hour DESC);

-- ============================================================================
-- Grant Permissions
-- ============================================================================

GRANT USAGE ON SCHEMA embeddings TO pgadmin;
GRANT USAGE ON SCHEMA analytics TO pgadmin;
GRANT USAGE ON SCHEMA app_metadata TO pgadmin;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA embeddings TO pgadmin;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA analytics TO pgadmin;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA app_metadata TO pgadmin;

GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA embeddings TO pgadmin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA analytics TO pgadmin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA app_metadata TO pgadmin;

GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA embeddings TO pgadmin;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA analytics TO pgadmin;

-- ============================================================================
-- Sample Data (Optional - for testing)
-- ============================================================================

-- Insert sample query logs
INSERT INTO analytics.query_logs (user_query, generated_sql, execution_time_ms, result_rows, llm_model, status)
VALUES 
    ('Show me recent users', 'SELECT * FROM users ORDER BY created_at DESC LIMIT 10', 45, 10, 'claude-sonnet-4', 'success'),
    ('Count active sessions', 'SELECT COUNT(*) FROM sessions WHERE active = true', 12, 1, 'claude-sonnet-4', 'success'),
    ('Top products by revenue', 'SELECT product_name, SUM(revenue) FROM sales GROUP BY product_name ORDER BY 2 DESC LIMIT 5', 234, 5, 'claude-sonnet-4', 'success')
ON CONFLICT DO NOTHING;

-- Refresh materialized view
REFRESH MATERIALIZED VIEW analytics.query_stats_hourly;

-- ============================================================================
-- PostgreSQL Configuration Recommendations
-- ============================================================================

-- Display current settings (for reference)
DO $$
BEGIN
    RAISE NOTICE 'PostgreSQL Version: %', version();
    RAISE NOTICE 'Max Connections: %', current_setting('max_connections');
    RAISE NOTICE 'Shared Buffers: %', current_setting('shared_buffers');
    RAISE NOTICE 'Effective Cache Size: %', current_setting('effective_cache_size');
END $$;
```

#### 2.2 MySQL Initialization (Optional)

Create `init-scripts/mysql/01-schema.sql`:

```sql
-- ============================================================================
-- MySQL 8.4 Initialization Script
-- Legacy Database Schema
-- ============================================================================

USE legacy_analytics;

-- ============================================================================
-- Legacy Tables
-- ============================================================================

CREATE TABLE IF NOT EXISTS legacy_customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS legacy_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_total DECIMAL(10, 2) NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES legacy_customers(customer_id),
    INDEX idx_customer_id (customer_id),
    INDEX idx_order_date (order_date),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- Sample Data
-- ============================================================================

INSERT INTO legacy_customers (customer_name, email) VALUES
    ('Alice Johnson', 'alice@example.com'),
    ('Bob Smith', 'bob@example.com'),
    ('Carol White', 'carol@example.com')
ON DUPLICATE KEY UPDATE customer_name=VALUES(customer_name);

INSERT INTO legacy_orders (customer_id, order_total, order_date, status) VALUES
    (1, 150.00, '2024-01-15', 'completed'),
    (1, 200.00, '2024-02-01', 'completed'),
    (2, 75.50, '2024-01-20', 'completed'),
    (3, 300.00, '2024-02-03', 'pending');
```

---

### Step 3: Build and Deploy Services

#### 3.1 Pre-flight Checks

```bash
#!/bin/bash
# preflight-check.sh - Verify system readiness

set -euo pipefail

echo "🔍 Running pre-flight checks..."

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker Engine 24.0+"
    exit 1
fi
echo "✅ Docker: $(docker --version)"

# Check Docker Compose
if ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose not found. Please install Docker Compose v2.20+"
    exit 1
fi
echo "✅ Docker Compose: $(docker compose version)"

# Check available disk space (minimum 100GB)
available_space=$(df -BG . | tail -1 | awk '{print $4}' | sed 's/G//')
if [ "$available_space" -lt 100 ]; then
    echo "⚠️  Warning: Less than 100GB available disk space ($available_space GB)"
else
    echo "✅ Disk space: ${available_space}GB available"
fi

# Check available memory (minimum 16GB)
available_memory=$(free -g | awk '/^Mem:/{print $2}')
if [ "$available_memory" -lt 16 ]; then
    echo "⚠️  Warning: Less than 16GB RAM available ($available_memory GB)"
else
    echo "✅ Memory: ${available_memory}GB available"
fi

# Check .env file
if [ ! -f .env ]; then
    echo "❌ .env file not found. Run generate-env.sh first"
    exit 1
fi
echo "✅ .env file exists"

# Check directory structure
required_dirs=(
    "volumes/postgres"
    "volumes/duckdb"
    "init-scripts/postgres"
    "nginx/ssl"
    "duckdb-service/src"
    "api-service/src"
)

for dir in "${required_dirs[@]}"; do
    if [ ! -d "$dir" ]; then
        echo "❌ Missing directory: $dir"
        exit 1
    fi
done
echo "✅ Directory structure verified"

# Check NVIDIA GPU (optional)
if command -v nvidia-smi &> /dev/null; then
    echo "✅ NVIDIA GPU detected: $(nvidia-smi --query-gpu=name --format=csv,noheader | head -1)"
else
    echo "⚠️  No NVIDIA GPU detected (optional for LLM)"
fi

echo ""
echo "✅ Pre-flight checks passed!"
echo "🚀 Ready to deploy"
```

#### 3.2 Build Services

```bash
#!/bin/bash
# build-services.sh - Build all Docker images

set -euo pipefail

echo "🔨 Building Docker images..."

# Source environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Build DuckDB service
echo "📦 Building DuckDB Query Service..."
docker compose build --no-cache duckdb-server

# Build API service
echo "📦 Building API Service..."
docker compose build --no-cache api-server

# Pull base images
echo "📥 Pulling base images..."
docker compose pull postgres18 mysql llm-gateway nginx

echo "✅ All images built successfully"

# Display images
echo ""
echo "📋 Built images:"
docker images | grep -E "duckdb-service|api-service|postgres|mysql|ollama|nginx"
```

#### 3.3 Deploy Stack

```bash
#!/bin/bash
# deploy-stack.sh - Deploy the complete stack

set -euo pipefail

echo "🚀 Deploying LLM-SQL Integration Stack..."

# Determine profile
PROFILE="${1:-default}"

case $PROFILE in
    "with-mysql")
        echo "📊 Deploying with MySQL support"
        docker compose --profile with-mysql up -d
        ;;
    "default")
        echo "📊 Deploying default stack (PostgreSQL + DuckDB)"
        docker compose up -d
        ;;
    *)
        echo "❌ Unknown profile: $PROFILE"
        echo "Usage: $0 [default|with-mysql]"
        exit 1
        ;;
esac

echo ""
echo "⏳ Waiting for services to be healthy..."
sleep 10

# Check service health
echo ""
echo "🏥 Health check status:"
docker compose ps

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📍 Service endpoints:"
echo "   - API:         http://localhost:8000/api/v1/docs"
echo "   - DuckDB:      http://localhost:8001/health"
echo "   - PostgreSQL:  localhost:5432"
echo "   - Metrics:     http://localhost:8000/metrics"
echo "   - NGINX:       http://localhost"
```

---

### Step 4: Verification & Testing

#### 4.1 Service Health Verification

```bash
#!/bin/bash
# verify-deployment.sh - Comprehensive deployment verification

set -euo pipefail

echo "✅ Verifying deployment..."

# Color codes for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

check_service() {
    local service=$1
    local url=$2
    local expected_code=${3:-200}
    
    echo -n "Checking $service... "
    
    if response=$(curl -s -o /dev/null -w "%{http_code}" "$url" 2>/dev/null); then
        if [ "$response" -eq "$expected_code" ]; then
            echo -e "${GREEN}✓ OK${NC} (HTTP $response)"
            return 0
        else
            echo -e "${RED}✗ FAIL${NC} (HTTP $response, expected $expected_code)"
            return 1
        fi
    else
        echo -e "${RED}✗ FAIL${NC} (unreachable)"
        return 1
    fi
}

# PostgreSQL check
echo -n "Checking PostgreSQL... "
if docker exec postgres18-vector pg_isready -U pgadmin -d llm_analytics &>/dev/null; then
    echo -e "${GREEN}✓ OK${NC}"
else
    echo -e "${RED}✗ FAIL${NC}"
fi

# DuckDB service check
check_service "DuckDB Service" "http://localhost:8001/health"

# API service check
check_service "API Service" "http://localhost:8000/api/v1/health"

# NGINX check
check_service "NGINX Proxy" "http://localhost/health"

# Ollama check (if available)
if docker compose ps | grep -q llm-gateway; then
    check_service "LLM Gateway" "http://localhost:11434/api/tags"
fi

echo ""
echo "🔗 Testing database connectivity..."

# Test PostgreSQL connection via DuckDB
echo -n "PostgreSQL attachment... "
if curl -s -X POST http://localhost:8001/query \
    -H "Content-Type: application/json" \
    -d '{"sql":"SELECT 1 FROM pg.information_schema.tables LIMIT 1","database":"duckdb"}' | grep -q "row_count"; then
    echo -e "${GREEN}✓ OK${NC}"
else
    echo -e "${RED}✗ FAIL${NC}"
fi

# Test SQLite attachment
echo -n "SQLite attachment... "
if curl -s -X POST http://localhost:8001/query \
    -H "Content-Type: application/json" \
    -d '{"sql":"SELECT 1","database":"duckdb"}' | grep -q "row_count"; then
    echo -e "${GREEN}✓ OK${NC}"
else
    echo -e "${RED}✗ FAIL${NC}"
fi

echo ""
echo "📊 Running sample queries..."

# Query 1: Count query logs
echo -n "Sample query 1 (count records)... "
if curl -s -X POST http://localhost:8001/query \
    -H "Content-Type: application/json" \
    -d '{"sql":"SELECT COUNT(*) as total FROM pg.analytics.query_logs","database":"duckdb"}' \
    | grep -q '"row_count":1'; then
    echo -e "${GREEN}✓ OK${NC}"
else
    echo -e "${RED}✗ FAIL${NC}"
fi

# Query 2: Aggregate query
echo -n "Sample query 2 (aggregation)... "
if curl -s -X POST http://localhost:8001/query \
    -H "Content-Type: application/json" \
    -d '{"sql":"SELECT status, COUNT(*) as count FROM pg.analytics.query_logs GROUP BY status","database":"duckdb"}' \
    | grep -q '"columns"'; then
    echo -e "${GREEN}✓ OK${NC}"
else
    echo -e "${RED}✗ FAIL${NC}"
fi

echo ""
echo "✅ Verification complete!"
```

#### 4.2 Sample Query Tests

Create `tests/sample-queries.sh`:

```bash
#!/bin/bash
# sample-queries.sh - Execute sample queries for testing

BASE_URL="http://localhost:8001"

echo "🧪 Running sample queries..."

# Test 1: Simple SELECT
echo ""
echo "Test 1: Simple SELECT query"
curl -X POST "$BASE_URL/query" \
    -H "Content-Type: application/json" \
    -d '{
        "sql": "SELECT 1 as test_column",
        "database": "duckdb"
    }' | jq

# Test 2: Query PostgreSQL through DuckDB
echo ""
echo "Test 2: Query PostgreSQL query logs"
curl -X POST "$BASE_URL/query" \
    -H "Content-Type: application/json" \
    -d '{
        "sql": "SELECT user_query, execution_time_ms, status FROM pg.analytics.query_logs ORDER BY created_at DESC LIMIT 5",
        "database": "duckdb"
    }' | jq

# Test 3: Aggregate query
echo ""
echo "Test 3: Aggregate statistics"
curl -X POST "$BASE_URL/query" \
    -H "Content-Type: application/json" \
    -d '{
        "sql": "SELECT status, COUNT(*) as count, AVG(execution_time_ms) as avg_time FROM pg.analytics.query_logs GROUP BY status",
        "database": "duckdb"
    }' | jq

# Test 4: List attached databases
echo ""
echo "Test 4: List attached databases"
curl -X GET "$BASE_URL/attach" | jq

# Test 5: Cross-database query (if MySQL attached)
echo ""
echo "Test 5: Cross-database JOIN (PostgreSQL + SQLite)"
curl -X POST "$BASE_URL/query" \
    -H "Content-Type: application/json" \
    -d '{
        "sql": "SELECT pg.analytics.query_logs.user_query, COUNT(*) as frequency FROM pg.analytics.query_logs GROUP BY user_query ORDER BY frequency DESC LIMIT 10",
        "database": "duckdb"
    }' | jq
```

#### 4.3 Load Testing

Create `tests/load-test.sh`:

```bash
#!/bin/bash
# load-test.sh - Basic load testing with Apache Bench

set -euo pipefail

echo "📊 Running load tests..."

# Check if ab (Apache Bench) is installed
if ! command -v ab &> /dev/null; then
    echo "❌ Apache Bench (ab) not found. Install with: apt-get install apache2-utils"
    exit 1
fi

API_URL="http://localhost:8001/query"
HEALTH_URL="http://localhost:8001/health"

# Test 1: Health endpoint (warm up)
echo ""
echo "Test 1: Health endpoint baseline (100 requests, 10 concurrent)"
ab -n 100 -c 10 "$HEALTH_URL"

# Test 2: Simple query endpoint
echo ""
echo "Test 2: Simple query (50 requests, 5 concurrent)"
ab -n 50 -c 5 -p - -T application/json "$API_URL" <<'EOF'
{"sql":"SELECT 1 as test","database":"duckdb"}
EOF

# Test 3: Complex query endpoint
echo ""
echo "Test 3: Complex query (20 requests, 2 concurrent)"
ab -n 20 -c 2 -p - -T application/json "$API_URL" <<'EOF'
{"sql":"SELECT status, COUNT(*) as count FROM pg.analytics.query_logs GROUP BY status","database":"duckdb"}
EOF

echo ""
echo "✅ Load tests complete!"
echo "💡 Review the results above for performance metrics"
```

[Back to TOC](#-table-of-contents)

---

### Step 5: Monitoring Setup

#### 5.1 Prometheus Configuration

Create `prometheus/prometheus.yml`:

```yaml
# Prometheus Configuration
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: 'llm-sql-integration'
    environment: 'production'

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          # - alertmanager:9093

# Rule files
rule_files:
  - 'alerts/*.yml'

# Scrape configurations
scrape_configs:
  # DuckDB Service metrics
  - job_name: 'duckdb-service'
    static_configs:
      - targets: ['duckdb-server:8001']
        labels:
          service: 'duckdb'
          component: 'query-engine'
    metrics_path: '/metrics'

  # API Service metrics
  - job_name: 'api-service'
    static_configs:
      - targets: ['api-server:8000']
        labels:
          service: 'api'
          component: 'application'
    metrics_path: '/metrics'

  # PostgreSQL metrics (via postgres_exporter)
  - job_name: 'postgres'
    static_configs:
      - targets: ['postgres-exporter:9187']
        labels:
          service: 'postgres'
          component: 'database'

  # Node exporter for system metrics
  - job_name: 'node'
    static_configs:
      - targets: ['node-exporter:9100']
        labels:
          component: 'system'
```

#### 5.2 Alert Rules

Create `prometheus/alerts/query-service.yml`:

```yaml
# Alert rules for DuckDB Query Service
groups:
  - name: query_service_alerts
    interval: 30s
    rules:
      # High error rate
      - alert: HighQueryErrorRate
        expr: |
          rate(duckdb_queries_total{status="error"}[5m]) 
          / 
          rate(duckdb_queries_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
          component: duckdb-service
        annotations:
          summary: "High query error rate detected"
          description: "Error rate is {{ $value | humanizePercentage }} (threshold: 5%)"

      # Slow query performance
      - alert: SlowQueryPerformance
        expr: |
          histogram_quantile(0.95, 
            rate(duckdb_query_duration_seconds_bucket[5m])
          ) > 10
        for: 5m
        labels:
          severity: warning
          component: duckdb-service
        annotations:
          summary: "Slow query performance detected"
          description: "P95 query latency is {{ $value }}s (threshold: 10s)"

      # Service down
      - alert: QueryServiceDown
        expr: up{job="duckdb-service"} == 0
        for: 1m
        labels:
          severity: critical
          component: duckdb-service
        annotations:
          summary: "DuckDB Query Service is down"
          description: "The DuckDB query service has been down for more than 1 minute"

      # High memory usage
      - alert: HighMemoryUsage
        expr: |
          duckdb_memory_usage_bytes 
          / 
          (16 * 1024 * 1024 * 1024) > 0.9
        for: 5m
        labels:
          severity: warning
          component: duckdb-service
        annotations:
          summary: "High memory usage detected"
          description: "Memory usage is {{ $value | humanizePercentage }} of limit"
```

#### 5.3 Grafana Dashboard

Create `grafana/dashboards/llm-sql-dashboard.json`:

```json
{
  "dashboard": {
    "title": "LLM-SQL Integration Dashboard",
    "tags": ["duckdb", "postgresql", "llm"],
    "timezone": "browser",
    "panels": [
      {
        "id": 1,
        "title": "Query Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(duckdb_queries_total[5m])",
            "legendFormat": "{{database}} - {{status}}"
          }
        ]
      },
      {
        "id": 2,
        "title": "Query Latency (P95)",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(duckdb_query_duration_seconds_bucket[5m]))",
            "legendFormat": "{{database}}"
          }
        ]
      },
      {
        "id": 3,
        "title": "Attached Databases",
        "type": "stat",
        "targets": [
          {
            "expr": "duckdb_attachments_total"
          }
        ]
      },
      {
        "id": 4,
        "title": "Error Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(duckdb_errors_total[5m])",
            "legendFormat": "{{error_type}}"
          }
        ]
      }
    ]
  }
}
```

#### 5.4 Add Monitoring to Docker Compose

Create `docker-compose.monitoring.yml`:

```yaml
version: '3.8'

services:
  # Prometheus
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    hostname: prometheus
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - ./prometheus/alerts:/etc/prometheus/alerts:ro
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
      - '--web.enable-lifecycle'
    ports:
      - "9090:9090"
    networks:
      - llm-network
    restart: unless-stopped

  # Grafana
  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    hostname: grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD:-admin}
      - GF_INSTALL_PLUGINS=grafana-clock-panel
    volumes:
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards:ro
      - ./grafana/datasources:/etc/grafana/provisioning/datasources:ro
      - grafana_data:/var/lib/grafana
    ports:
      - "3000:3000"
    networks:
      - llm-network
    depends_on:
      - prometheus
    restart: unless-stopped

  # PostgreSQL Exporter
  postgres-exporter:
    image: prometheuscommunity/postgres-exporter:latest
    container_name: postgres-exporter
    hostname: postgres-exporter
    environment:
      DATA_SOURCE_NAME: "postgresql://pgadmin:${POSTGRES_PASSWORD}@postgres18:5432/llm_analytics?sslmode=disable"
    ports:
      - "9187:9187"
    networks:
      - llm-network
    depends_on:
      - postgres18
    restart: unless-stopped

  # Node Exporter (system metrics)
  node-exporter:
    image: prom/node-exporter:latest
    container_name: node-exporter
    hostname: node-exporter
    command:
      - '--path.procfs=/host/proc'
      - '--path.sysfs=/host/sys'
      - '--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)'
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    ports:
      - "9100:9100"
    networks:
      - llm-network
    restart: unless-stopped

volumes:
  prometheus_data:
    driver: local
  grafana_data:
    driver: local

networks:
  llm-network:
    external: true
```

**Deploy monitoring stack:**

```bash
#!/bin/bash
# deploy-monitoring.sh - Deploy monitoring stack

echo "📊 Deploying monitoring stack..."

# Deploy monitoring services
docker compose -f docker-compose.yml -f docker-compose.monitoring.yml up -d

echo "✅ Monitoring deployed!"
echo ""
echo "📍 Monitoring endpoints:"
echo "   - Prometheus: http://localhost:9090"
echo "   - Grafana:    http://localhost:3000 (admin/admin)"
echo "   - Node Exp:   http://localhost:9100/metrics"
```

[Back to TOC](#-table-of-contents)

---

### Step 6: Operational Procedures

#### 6.1 Backup Procedures

```bash
#!/bin/bash
# backup.sh - Backup all databases

set -euo pipefail

BACKUP_DIR="./backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "💾 Starting backup at $TIMESTAMP..."

# Backup PostgreSQL
echo "Backing up PostgreSQL..."
docker exec postgres18-vector pg_dump -U pgadmin llm_analytics | gzip > "$BACKUP_DIR/postgres/llm_analytics_$TIMESTAMP.sql.gz"

# Backup DuckDB
echo "Backing up DuckDB..."
docker exec duckdb-query-engine cp /data/analytics.duckdb /data/analytics_$TIMESTAMP.duckdb
docker cp duckdb-query-engine:/data/analytics_$TIMESTAMP.duckdb "$BACKUP_DIR/duckdb/"

# Backup MySQL (if exists)
if docker ps | grep -q mysql-legacy; then
    echo "Backing up MySQL..."
    docker exec mysql-legacy mysqldump -u root -p${MYSQL_ROOT_PASSWORD} legacy_analytics | gzip > "$BACKUP_DIR/mysql/legacy_analytics_$TIMESTAMP.sql.gz"
fi

echo "✅ Backup complete! Files in $BACKUP_DIR"
```

#### 6.2 Restore Procedures

```bash
#!/bin/bash
# restore.sh - Restore from backup

set -euo pipefail

BACKUP_FILE=$1

if [ -z "$BACKUP_FILE" ]; then
    echo "Usage: $0 <backup_file>"
    exit 1
fi

echo "⚠️  WARNING: This will overwrite existing data!"
read -p "Continue? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Restore cancelled"
    exit 0
fi

# Restore PostgreSQL
if [[ $BACKUP_FILE == *"postgres"* ]]; then
    echo "Restoring PostgreSQL..."
    gunzip -c "$BACKUP_FILE" | docker exec -i postgres18-vector psql -U pgadmin llm_analytics
fi

# Restore DuckDB
if [[ $BACKUP_FILE == *"duckdb"* ]]; then
    echo "Restoring DuckDB..."
    docker cp "$BACKUP_FILE" duckdb-query-engine:/data/analytics.duckdb
fi

echo "✅ Restore complete!"
```

#### 6.3 Log Management

```bash
#!/bin/bash
# manage-logs.sh - Log rotation and cleanup

set -euo pipefail

LOG_DIR="./logs"
RETENTION_DAYS=30

echo "🗂️  Managing logs..."

# Compress logs older than 7 days
find "$LOG_DIR" -name "*.log" -mtime +7 -exec gzip {} \;

# Delete compressed logs older than retention period
find "$LOG_DIR" -name "*.log.gz" -mtime +$RETENTION_DAYS -delete

# Docker logs cleanup
docker system prune -f --filter "until=720h"

echo "✅ Log management complete"
```

[Back to TOC](#-table-of-contents)

---

**This completes Part 4: Deployment & Operations Guide!**

The deployment guide now includes:
✅ Complete pre-deployment preparation  
✅ Database initialization scripts  
✅ Build and deployment procedures  
✅ Comprehensive verification tests  
✅ Monitoring setup with Prometheus/Grafana  
✅ Operational procedures (backup, restore, logs)  

