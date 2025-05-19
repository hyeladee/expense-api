# expense-api

A simple **Expense Manager** web application and API built with **FastAPI**, **SQLAlchemy**, **Jinja2**, and **SQLite**. It allows you to create and manage expense categories and record expenses, with a clean web interface and a RESTful JSON API.

## Features

* 🔒 **Backend API** powered by FastAPI with Swagger UI available at `/docs`
* 🗂️ **Categories**: Add, list, and manage expense categories (with optional budgets)
* 💸 **Expenses**: Create and view expenses linked to categories, recording amount, date, and description
* 🖥️ **Web UI**: Interactive single-page interface using Jinja2 templates, Bootstrap, and vanilla JS
* 📦 **Persistence** with SQLite (`expenses.db`) via SQLAlchemy ORM
* 🚀 **Auto-generated schemas** and validation with Pydantic

## Requirements

* Python 3.12+
* Pipenv (optional) or pip

## Installation

1. **Clone** the repository:

   ```bash
   git clone https://github.com/hyeladee/expense-api.git
   cd expense-api
   ```

2. **Create** and **activate** a virtual environment:

   ```bash
   python -m venv .venv          # create venv
   source .venv/bin/activate     # macOS/Linux
   .\.venv\Scripts\activate    # Windows
   ```

3. **Install** dependencies:

   * Using **Pipenv**:

     ```bash
     pipenv install
     pipenv shell
     ```
   * Or with **pip**:

     ```bash
     pip install -r requirements.txt
     ```

## Usage

1. **Run** the application:

   ```bash
   uvicorn app.main:app --reload
   ```
2. Open your browser and go to:

   * **Web UI**: `http://127.0.0.1:8000/`
   * **API docs**: `http://127.0.0.1:8000/docs`

## API Endpoints

All JSON endpoints are prefixed with `/api`:

* **GET** `/api/categories/` — List all categories

* **POST** `/api/categories/` — Create a new category

  ```json
  {
    "name": "Groceries",
    "budget": 250.00     // optional
  }
  ```

* **GET** `/api/expenses/` — List all expenses

* **POST** `/api/expenses/` — Create a new expense

  ```json
  {
    "amount": 15.75,
    "description": "Lunch",
    "date": "2025-05-19T12:34:56",   // optional, defaults to now
    "category_id": 1
  }
  ```

## Project Structure

```
expense-api/
├── app/
│   ├── main.py           # FastAPI app setup
│   ├── database.py       # SQLAlchemy engine & session
│   ├── models.py         # ORM models: Category, Expense
│   ├── schemas.py        # Pydantic models for validation
│   ├── crud.py           # Database interaction functions
│   ├── routers/api.py    # API route definitions
│   ├── static/           # CSS, JS assets
│   └── templates/        # Jinja2 HTML templates
├── expenses.db           # SQLite database (auto-created)
├── requirements.txt      # pip dependencies
├── Pipfile & Pipfile.lock# Pipenv dependencies
├── .gitignore
└── LICENSE
```

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

*Built with \:heart: and FastAPI*
