#  ___________________
#  Import LIBRARIES
from fastapi import FastAPI  # , Depends
from sqlalchemy import Engine
from sqlmodel import SQLModel, create_engine, Session, select
from contextlib import (
    asynccontextmanager,
)  # Needed to start a command when FastAPI is started-up
from typing import AsyncGenerator

#  Import FILES
from models.models import Item
#  ___________________


#  Database adimn
sqlite_file_name: str = "database.db"
sqlite_url: str = f"sqlite:///{sqlite_file_name}"
engine: Engine = create_engine(url=sqlite_url, echo=True)


def create_db_and_tables() -> None:
    """
    All processes for creating the database and database tables'
    I.e. Starts the database connection and schema creation logic.
    """
    SQLModel.metadata.create_all(bind=engine)


# ADJUSTED Initialization and @asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    An asynchronous context manager for FastAPI's lifespan events.

    This function handles startup and shutdown logic for the application.
    The code before 'yield' runs during application startup.
    The code after 'yield' runs during application shutdown.

    Args:
        app (FastAPI): The FastAPI application instance. This parameter
                       is provided by FastAPI when it calls the lifespan function.

    Yields:
        None: This context manager does not yield any value to be consumed
              by the 'async with' statement. It's primarily used for
              its side effects (startup/shutdown logic).

    Returns:
        AsyncGenerator[None, None]: The return type indicates that this is an asynchronous generator.
        - The first 'None' signifies that the generator yields no value (or specifically, 'None' if a value were to be yielded, which is not the case here as it's for side effects).
        - The second 'None' signifies that no value is sent *into* the generator using .send().
    """
    # Startup
    print("Creating database tables...")  # Added for debugging confirmation
    create_db_and_tables()
    yield
    # Shutdown (optional, but good practice if you have cleanup)
    # --- Application Shutdown Logic ---
    print("[Lifespan] Application shutting down. Performing cleanup...")
    # Add any cleanup code here, e.g., closing database connections,
    # stopping background tasks, etc.
    print("[Lifespan] Shutdown complete.")


# Initialize HERE FastAPI application, passing the lifespan context manager
app: FastAPI = FastAPI(lifespan=lifespan)


#  OLD Initialization and @asynccontextmanager

# app: FastAPI = FastAPI()

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Startup
#     create_db_and_tables()
#     yield
#     # shutdown


@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


#  POST - works with: {"name": "erre","price": 100,"is_offer": false,"password": "Don't show this"} or {"name": "elle", "price": 1000, "is_offer": true,"password": "Show this"}
@app.post(path="/items/")
def create_item(item: Item) -> Item:
    with Session(bind=engine) as session:
        session.add(instance=item)
        session.commit()
        session.refresh(instance=item)
        return item


@app.get(path="/items/", response_model=list[Item])
def read_items():
    with Session(bind=engine) as session:
        items = session.exec(statement=select(Item)).all()
        return items


# def main():
#     print("Hello from fast-prgk!")


# if __name__ == "__main__":
#     main()

#  ___________________
#  Import LIBRARIES
#  Import FILES
#  ___________________
