from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Hello World"}

@app.get("/tasks")
def read_tasks():
  return {"tasks": ["task1", "task2", "task3"]}