from sqlmodel import SQLModel
from typing import Optional

class TodoBase(SQLModel):
    title: str
    description: Optional[str] = ""
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: int

class TodoUpdate(TodoBase):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
