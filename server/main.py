from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()

class Task(BaseModel):
    id: int
    name: str
    description: str
    completed: bool
    tags: List[str] = []
    priority: int = 1
    due_date: str = None
    status: str = "pending"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/tasks/")
async def create_task(task: Task, db: Annotated[Session, Depends(get_db)]):
   db_task = models.Task(
       name=task.name,
       description=task.description,
       completed=task.completed,
       tags=",".join(task.tags),
       priority=task.priority,
       due_date=task.due_date,
       status=task.status
   )
   db.add(db_task)
   db.commit()
   db.refresh(db_task)
   return db_task

@app.get("/tasks/", response_model=List[Task])
async def read_tasks(db: Annotated[Session, Depends(get_db)], skip: int = 0, limit: int = 0):
    tasks = db.query(models.Task).all()
    return tasks
