from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Addition API"}

# @app.get("/add")
# def add_numbers(a: int, b: int):
#     return {"result": a + b}

@app.post("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}