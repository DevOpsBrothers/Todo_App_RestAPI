import ssl
import sys
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, select
from app.models import Todo
from app.database import get_db, engine

# Ensure SSL module is available
try:
    ssl.create_default_context()
except AttributeError:
    print("SSL module is not available. Please check your Python installation.", file=sys.stderr)
    sys.exit(1)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    """Initialize the database on startup."""
    SQLModel.metadata.create_all(engine)

@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo, db: Session = Depends(get_db)):
    """Create a new Todo item."""
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

@app.get("/todos/", response_model=list[Todo])
def read_todos(db: Session = Depends(get_db)):
    """Retrieve all Todo items."""
    return db.exec(select(Todo)).all()
