from sqlmodel import SQLModel, Field

class Todo(SQLModel, table=True):
    """Todo model for SQLModel ORM."""
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str = ""
    completed: bool = False
