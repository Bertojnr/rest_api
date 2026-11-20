# CRUD REST API using FastAPI

A CRUD REST API using a simple in memory database, represented by a Python list, to explore all CRUD actions

## 🚀 Features
* **GET Routes**: Fetch items with path and query parameters.
* **POST/PATCH Routes**: Handle structured JSON payloads with strict Pydantic validation.
* **Interactive Docs**: Auto-generated Swagger UI (`/docs`).

## 🛠️ Tech Stack
* Python 3.x
* FastAPI
* Pydantic
* Uvicorn

## ⚙️ Getting Started Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/your-repo-name.git](https://github.com/YourUsername/your-repo-name.git)
   cd bookly

## Create and activate a virtual environment:
   python -m venv venv
# On Windows (Git Bash):
source venv/Scripts/activate

## Install dependencies:
pip install fastapi uvicorn pydantic

## Run the server
uvicorn main:app --reload

## Explore the docs:
Open your browser and navigate to http://127.0.0.1:8000/docs