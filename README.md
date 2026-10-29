# 🏢 NRW Data Center Business Intelligence Platform

### AI-Powered Geospatial Business Intelligence for Data Center Site Selection and Infrastructure Analysis

The NRW Data Center Business Intelligence Platform is an AI-powered decision support system that combines geospatial analysis, infrastructure intelligence, renewable energy data, market intelligence, and conversational AI into a single interactive dashboard.

Built with **Python**, **PostgreSQL/PostGIS**, **GeoPandas**, **PyDeck**, **Streamlit**, and **OpenAI**, the platform enables users to evaluate data center locations through interactive GIS visualization, site scoring, and AI-assisted insights.

---

## Table of Contents

- [Overview](#overview)
- [Dashboard Preview](#dashboard-preview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [How It Works](#how-it-works)
- [Dashboard Modules](#dashboard-modules)
- [AI Advisor](#ai-advisor)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Dashboard](#running-the-dashboard)
- [Project Status](#current-project-status)
- [Roadmap](#roadmap)
- [Vision](#vision)

![Python]
![PostgreSQL]
![PostGIS]
![Streamlit]
![OpenAI]
![Status]

## Overview

Selecting an optimal location for a modern data center requires much more than available land.

Power infrastructure, renewable energy, electrical grid capacity, market activity, and surrounding infrastructure all influence the long-term viability of a site.

The NRW Data Center Business Intelligence Platform integrates multiple public infrastructure datasets into a unified PostgreSQL/PostGIS database and provides an interactive AI-powered dashboard for analyzing, comparing, and evaluating potential data center locations.

The platform combines:

- Geospatial Intelligence
- Infrastructure Analysis
- Site Scoring
- Market Intelligence
- AI-assisted Decision Support

# Key Features

## GIS Intelligence

✔ Interactive GIS Infrastructure Map

✔ Data Center Visualization

✔ High Voltage Substations

✔ Transformers

✔ Transmission Lines

✔ Renewable Energy Assets

---

## Business Intelligence

✔ KPI Dashboard

✔ Site Intelligence

✔ Site Score

✔ Market Intelligence

✔ News Intelligence

✔ Spatial Infrastructure Analysis

---

## Artificial Intelligence

✔ AI Advisor

✔ Natural Language Queries

✔ Executive Infrastructure Summaries

✔ Context-aware Responses

✔ Retrieval-Augmented Generation (RAG)

---

## Spatial Intelligence

✔ Power Readiness Analysis

✔ Renewable Energy Analysis

✔ Infrastructure Distance Calculations

✔ Land Value Integration

✔ Site Ranking

# System Architecture

mermaid
flowchart TD

A[External Data Sources]

B[ETL Pipelines]

C[PostgreSQL + PostGIS]

D[Repository Layer]

E[Business Services]

F[Interactive Dashboard]

G[Site Intelligence]

H[News Intelligence]

I[AI Advisor]

J[Executive Decision Support]

A --> B
B --> C
C --> D
D --> E

E --> F
E --> G
E --> H

F --> I
G --> I
H --> I

I --> J



┌──────────────────────┐
│ External Data Sources│
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    ETL Pipelines     │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ PostgreSQL + PostGIS │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Repository Layer     │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Business Services    │
└──────────┬───────────┘
           ▼
      ┌────┴────┐
      ▼         ▼
┌──────────┐ ┌──────────┐
│ GIS Map  │ │ News BI  │
└────┬─────┘ └────┬─────┘
     │            │
     └────┬───────┘
          ▼
┌──────────────────────┐
│ Site Intelligence    │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ AI Advisor           │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ OpenAI GPT           │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Executive Insights   │
└──────────────────────┘

                  

# Dashboard Modules

## Interactive GIS Map

Visualizes:

- Data Centers
- High Voltage Substations
- Transformers
- Renewable Energy Assets
- High Voltage Transmission Lines

---

## KPI Dashboard

Provides executive metrics for infrastructure assets, facilities, and renewable energy resources.

---

## Site Intelligence

Displays infrastructure proximity, renewable energy availability, land valuation, and technical site characteristics for the selected facility.

---

## Site Score

Calculates a unified infrastructure readiness score using spatial analysis and business intelligence metrics.

---

## News Intelligence

Aggregates recent industry news and links relevant articles to companies and facilities.

---

## AI Advisor

Provides conversational access to infrastructure intelligence using natural language.


# AI Advisor

The AI Advisor enables users to explore infrastructure intelligence using natural language.

Current capabilities

- Site Summaries
- Infrastructure Analysis
- Grid Readiness Evaluation
- Renewable Energy Analysis
- Executive Recommendations
- News Summaries

Upcoming

- Intent Detection
- Tool Routing
- Context Awareness
- LangGraph Agents
- Agentic RAG


# Technology Stack

## Backend

- Python
- SQLAlchemy
- PostgreSQL
- PostGIS

## GIS

- GeoPandas
- Shapely
- PyDeck

## Dashboard

- Streamlit

## AI

- OpenAI
- Retrieval-Augmented Generation (RAG)

## Data Processing

- Pandas
- JSON
- GeoJSON

nrw-dc-bi/
│
├── app/
│   ├── services/
│   ├── repositories/
│   ├── database/
│   ├── spatial/
│   ├── intelligence/
│   └── ai/
│
├── ui/
│
├── data/
│
├── scripts/
│
├── tests/
│
└── README.md


# Installation

## Prerequisites

- Python 3.12+
- PostgreSQL 17 + PostGIS
- uv (Python package manager)

Install uv if you don't already have it:

bash
pip install uv


or

bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"


---

## Clone the Repository

bash
git clone <repository-url>

cd nrw-dc-bi


---

## Create a Virtual Environment

bash
uv venv


Activate it:

### Windows

bash
.venv\Scripts\activate


### Linux / macOS

bash
source .venv/bin/activate


---

## Install Dependencies

bash
uv sync


If you're not using a uv.lock yet, then instead use:

bash
uv pip install -r requirements.txt


---

## Configure Environment

bash
cp .env.example .env


Update the database connection and OpenAI API key.

---

## Run Database Migrations

bash
alembic upgrade head


---

## Start the Dashboard

bash
streamlit run ui/app.py


The application will be available at:


http://localhost:8501


## Requirements

- Python 3.12+
- PostgreSQL 17
- PostGIS
- Git
- uv

# Running the Dashboard

bash
streamlit run ui/app.py

# Current Project Status

## Completed

- Data Collection
- ETL Pipelines
- GIS Dashboard
- Interactive Map
- Site Intelligence
- Site Score
- News Intelligence
- AI Advisor
- Infrastructure Layers

## In Progress

- Context-aware AI
- Intent Detection
- Tool Routing
- LangGraph Integration

## Planned

- Multi-Agent AI
- Predictive Site Recommendations
- Investment Forecasting
- Voice Interface


# Roadmap

## Completed

- ETL Platform
- GIS Visualization
- Business Intelligence Dashboard
- AI Advisor
- News Intelligence

## Next

- Intent Detection
- Context-aware Responses
- Agentic RAG
- LangGraph Workflows

## Future

- Predictive Site Ranking
- Multi-Agent Decision Support
- Voice-enabled AI Advisor


# Vision

The long-term vision is to build an AI-powered decision support platform for data center planning and infrastructure investment.

By combining geospatial intelligence, power infrastructure, renewable energy, land valuation, market intelligence, and conversational AI, the platform enables users to evaluate and compare potential data center locations through natural language interaction.

The project is designed to evolve into a comprehensive executive decision-support system that assists planners, investors, and infrastructure specialists in identifying optimal data center locations.

## Netherlands Cadastre ETL

### Purpose

This implementation retrieves Dutch cadastral parcel features from the PDOK Kadastrale Kaart Web Feature Service (WFS), validates and standardizes the spatial data, and prepares it for loading into an isolated PostGIS staging schema.


### Architecture

PDOK Kadastrale Kaart WFS
        |
        v
PDOK scraper
        |
        v
Spatial transformer
        |
        v
Cadastre loader
        |
        v
PostgreSQL/PostGIS
iris_staging.cadastre_netherlands

### Source configuration

- Service: PDOK Kadastrale Kaart WFS
- WFS version: 2.0.0
- Feature type: kadastralekaart:Perceel
- Response format: GeoJSON/JSON
- Source CRS: EPSG:28992 (Dutch RD New)
- Target CRS: EPSG:4326 (WGS 84)
- Country code: "NL"

### Project files

- app/scrapers/pdok/pdok_scraper.py: retrieves one or more WFS pages.
- app/transformers/pdok_transformer.py: validates IDs and geometry, converts Polygon to MultiPolygon, and reprojects geometry.
- app/loaders/pdok_loader.py: applies staging safety checks and loads new records.
- app/runners/pdok_runner.py: connects extraction, transformation, and loading.
- app/database/models/cadastre.py: SQLAlchemy/PostGIS table definition.
- alembic/versions/add_cadastre_staging.py: database schema migration.
- scripts/check_pdok.py: lightweight automated spatial checks.
- tests/test_pdok_transformer.py: transformer test cases.
- .env.example: example local configuration without secrets.

### Safety controls

- The target schema is fixed as iris_staging.
- The loader rejects a database URL containing iris_core.
- Local Docker/PostGIS resources are used for validation.
- .env is excluded from Git and must not be committed.
- Production credentials and production resources must not be used.

### Environment configuration

Copy .env.example to .env and set local development values.

env
POSTGRES_DB=iris
POSTGRES_USER=iris
POSTGRES_PASSWORD=iris
DATABASE_URL=postgresql+psycopg2://iris:iris@localhost:5433/iris
PDOK_WFS_URL=https://service.pdok.nl/kadaster/brk-kadastrale-kaart/wfs/v5_0
PDOK_FEATURE_TYPE=kadastralekaart:Perceel


Do not commit .env.

### Start Docker services

bash
docker compose up -d


Check service status:

bash
docker compose ps


Confirm PostGIS is available:

bash
docker exec -it nrw-postgis psql -U iris -d iris -c "SELECT PostGIS_Version();"


### Database migration

The intended reproducible database setup is:

bash
alembic upgrade head


The migration creates:

text
iris_staging.cadastre_netherlands


The table contains:

- source_id: unique PDOK feature identifier and primary key.
- country_code: two-character country code (NL).
- geometry: PostGIS MULTIPOLYGON with SRID 4326.

### Automated spatial check

The lightweight automated check validates:

- Polygon to MultiPolygon conversion.
- Reprojection to EPSG:4326.
- Country code NL.
- Rejection of missing geometry.

Run it in an isolated Python container:

bash
docker run --rm -v "%cd%:/app" -w /app python:3.12-slim sh -c "pip install -q geopandas shapely pyproj && python -m scripts.check_pdok"


Expected result:

text
PDOK checks passed


### Live-source validation

A bounded live validation can request five parcel features and transform them without loading the whole national dataset.

Expected checks:

- Fetched: 5
- Transformed: 5
- CRS is EPSG:4326
- Geometry type is MultiPolygon
- Source IDs are retained

Do not use the full runner for an unrestricted national extraction without first defining an appropriate area, page limit, or bulk-download strategy.

### Database validation queries

sql
SELECT COUNT(*)
FROM iris_staging.cadastre_netherlands;

SELECT country_code, COUNT(*)
FROM iris_staging.cadastre_netherlands
GROUP BY country_code;

SELECT ST_GeometryType(geometry), ST_SRID(geometry), COUNT(*)
FROM iris_staging.cadastre_netherlands
GROUP BY 1, 2;

SELECT COUNT(*)
FROM iris_staging.cadastre_netherlands
WHERE NOT ST_IsValid(geometry);

SELECT source_id, COUNT(*)
FROM iris_staging.cadastre_netherlands
GROUP BY source_id
HAVING COUNT(*) > 1;


### Assumptions

- kadastralekaart:Perceel is the required parcel feature type.
- PDOK parcel coordinates are supplied in EPSG:28992.
- The target system requires MultiPolygon geometry in EPSG:4326.
- Features without an ID, missing geometry, empty geometry, invalid geometry, or unsupported geometry types are rejected.
- source_id is used for traceability and duplicate prevention.
- Local Docker/PostGIS is the isolated staging resource.

### Limitations

- A full national WFS extraction can be memory-intensive and may be subject to service limits. A bounded query, streamed processing, or the dedicated PDOK bulk-download service should be considered for larger runs.
- The submitted loader reads existing IDs into memory. A database-native upsert using INSERT ... ON CONFLICT is preferable at larger scale.
- The transformer currently retains all PDOK properties, while the migration defines only source_id, country_code, and geometry. Before a full database load, either select those three columns in the loader or extend the table schema for the required attributes.
- The live source extraction/transformation and PostGIS database behavior were validated separately. A bounded live end-to-end integration test should be added.
- The migration file is included, but migration execution should be validated in the same containerized application environment used by reviewers.

### Recommended next improvements

1. Align transformed columns with the target migration.
2. Replace the Python ID lookup with a PostgreSQL upsert.
3. Add mocked pagination and HTTP-error tests.
4. Add a bounded live end-to-end integration test.
5. Add run-level quality metrics for fetched, accepted, rejected, duplicate, and loaded records.