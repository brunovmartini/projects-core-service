import os

from dotenv import load_dotenv
from pydantic import PostgresDsn
from sqlalchemy.orm import registry
from flask_sqlalchemy import SQLAlchemy

load_dotenv()


mapper_registry = registry()

db: SQLAlchemy = SQLAlchemy(session_options={"expire_on_commit": False}, metadata=mapper_registry.metadata)


def get_database_url() -> str:
    return str(
        PostgresDsn.build(
            scheme=os.getenv("DATABASE_SCHEME"),
            username=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=int(os.getenv("DATABASE_PORT")),
            path=os.getenv("DATABASE_NAME"),
        )
    )
