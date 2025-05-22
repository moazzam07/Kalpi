# Kalpi

## Overview
Kalpi is a Financial Screener API built with FastAPI. It allows you to manage and screen stocks and screening criteria via a RESTful API.

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Kalpi
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

- The API will be available at: http://127.0.0.1:8000/
- Interactive API docs (Swagger UI) are available at: http://127.0.0.1:8000/docs

## Project Structure
- `main.py`: Application entry point
- `routes/`: Contains API route definitions
- `utils.py`, `db.py`, `schemas.py`: Utility, database, and schema definitions


## System Architecture

```
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  FastAPI Server  |------>|  MongoDB         |------>|  API Routes      |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
        |                          |                          |
        v                          v                          v
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  Utils           |------>|  Schemas         |------>|  Main            |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
```

### Components:
- **FastAPI Server**: The main application server.
- **MongoDB**: Database for storing stocks and screening criteria.
- **API Routes**: Defined in the `routes/` directory.
- **Utils**: Utility functions for database operations.
- **Schemas**: Data models defined using Pydantic.
- **Main**: Entry point of the application.
