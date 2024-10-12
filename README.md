# FastAPI Project

This is a sample API project built with FastAPI.

## Features

- **High Performance**: Built on top of Starlette and Pydantic.
- **Automatic Docs**: Swagger and ReDoc for auto-generated API documentation.
- **Type Safety**: Use of Python type hints for request validation.
- **Asynchronous Support**: First-class `async` support for high concurrency.
- **Dependency Injection**: Modular and easy-to-test code with dependency injection.

## Getting Started

### Prerequisites

- Python 3.6+
- `uvicorn` for running the ASGI server

### Installation

1. Clone the repository:

```bash
    git clone https://github.com/sidhyaashu/FAST_API.git
    cd FAST_API
```
2. Create Virtual Enviroment:

```bash
    py -3 -m venv <env-name>
```
3. Activate venve:
```bash
    <env-name>\Scripts\activate.bat
```


4. Install dependencies:
```bash
    pip install -r requirements.txt
```

### Running the Application

Run the app using `uvicorn`:

```bash
uvicorn main:app --reload
```

# After compelete the all 5 stages move to src.app.server

```bash
uvicorn src.app.server:app --reload
```
