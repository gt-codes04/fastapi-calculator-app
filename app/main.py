from fastapi import FastAPI, HTTPException
from .operations import add, subtract, multiply, divide

app = FastAPI(
    title="FastAPI Calculator",
    description="A simple calculator API built with FastAPI",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Calculator! Use /docs to see the API documentation."}

@app.get("/calculate/{operation}")
async def calculate(operation: str, x: float, y: float):
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    
    if operation not in operations:
        raise HTTPException(
            status_code=400, 
            detail=f"Operation '{operation}' not supported. Use one of: {', '.join(operations.keys())}"
        )
    
    try:
        result = operations[operation](x, y)
        return {"operation": operation, "x": x, "y": y, "result": result}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")