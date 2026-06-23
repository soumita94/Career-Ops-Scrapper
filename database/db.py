from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "sqlite:///career_ops.db"

print("CURRENT DIR:", os.getcwd())
print("DATABASE:", os.path.abspath("career_ops.db"))

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autoflush=False,
    bind=engine
)