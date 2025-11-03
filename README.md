# FastAPI Calculator

A simple calculator API built with FastAPI that provides basic arithmetic operations.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- RESTful API endpoints
- Swagger UI documentation
- Comprehensive test suite (unit, integration, and E2E tests)
- GitHub Actions CI pipeline
- Logging support

## Project Structure

```
fastapi-calculator/
├─ app/
│  ├─ __init__.py
│  ├─ main.py               # FastAPI app (endpoints)
│  ├─ operations.py         # add/sub/mul/div (pure functions)
│  ├─ logger.py             # logging configuration
├─ tests/
│  ├─ unit/
│  │  └─ test_operations.py
│  ├─ integration/
│  │  └─ test_api.py
│  └─ e2e/
│     └─ test_ui_e2e.py     # Playwright tests
├─ requirements.txt
├─ .github/
│  └─ workflows/
│     └─ ci.yml             # GitHub Actions
├─ README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fastapi-calculator.git
cd fastapi-calculator
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000
Swagger UI documentation is available at http://localhost:8000/docs

## API Endpoints

- GET `/`: Welcome message
- GET `/calculate/{operation}?x={number}&y={number}`: Perform calculation
  - Supported operations: add, subtract, multiply, divide
  - Parameters x and y should be numbers

## Testing

Run different test suites:

```bash
# Unit tests
pytest tests/unit/

# Integration tests
pytest tests/integration/

# E2E tests (requires running server)
pytest tests/e2e/

# All tests
pytest
```

## CI/CD

The project includes a GitHub Actions workflow that:
1. Runs on push to main and pull requests
2. Sets up Python environment
3. Installs dependencies
4. Runs all test suites
5. Verifies the application builds successfully

## License

MIT