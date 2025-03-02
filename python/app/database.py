from sqlmodel import SQLModel, Session, create_engine
import os

# Define the database URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todos.db")

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

def get_db():
    """Provide a database session."""
    with Session(engine) as session:
        yield session
