from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from . import operations
from .logger import configure_logging
import logging

configure_logging()
log = logging.getLogger("app")

app = FastAPI(title="Calculator API")

@app.get("/add")
async def add_numbers(a: float, b: float):
    log.info(f"Adding {a} and {b}")
    result = operations.add(a, b)
    return {"result": result}

@app.get("/sub")
async def subtract_numbers(a: float, b: float):
    log.info(f"Subtracting {b} from {a}")
    result = operations.sub(a, b)
    return {"result": result}

@app.get("/mul")
async def multiply_numbers(a: float, b: float):
    log.info(f"Multiplying {a} and {b}")
    result = operations.mul(a, b)
    return {"result": result}

@app.get("/div")
async def divide_numbers(a: float, b: float):
    log.info(f"Dividing {a} by {b}")
    try:
        result = operations.div(a, b)
        return {"result": result}
    except ZeroDivisionError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
      <head><meta charset="utf-8"><title>Calculator</title></head>
      <body style="font-family: Arial; padding: 20px;">
        <h1>Calculator</h1>
        <input id="a" placeholder="a"/>
        <input id="b" placeholder="b"/>

        <button id="add">Add</button>
        <button id="sub">Subtract</button>
        <button id="mul">Multiply</button>
        <button id="div">Divide</button>

        <div id="out" style="margin-top:15px; font-size:20px;"></div>

        <script>
          async function call(op){
            const a = document.getElementById('a').value;
            const b = document.getElementById('b').value;
            const res = await fetch(`/${op}?a=${a}&b=${b}`);
            const json = await res.json();
            document.getElementById('out').innerText = json.result ?? json.detail;
          }
          document.getElementById('add').onclick = () => call('add');
          document.getElementById('sub').onclick = () => call('sub');
          document.getElementById('mul').onclick = () => call('mul');
          document.getElementById('div').onclick = () => call('div');
        </script>
      </body>
    </html>
    """
