from database.db import engine
from database.model import Base

Base.metadata.create_all(
    bind=engine
)

print(
    "Database created successfully"
)