# Career-Ops Backend

## Overview

Career-Ops is a job aggregation backend that discovers company career pages, extracts job listings, and stores them in a database for search and retrieval.

## Current Features

* Admin job ingestion endpoint
* Browser Use powered job discovery
* SQLite database storage
* Job search API
* FastAPI Swagger documentation

## API Endpoints

### Sync Company

POST /admin/sync-company

Request:

```json
{
  "company_url": "https://company.com"
}
```

### Search Jobs

GET /jobs/search?keyword=engineer

Returns matching jobs stored in the database.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create .env:

```env
BROWSER_USE_API_KEY=your_key
```

Run:

```bash
python create_tables.py
uvicorn app:app --reload
```

Swagger:

```
http://127.0.0.1:8000/docs
```
