from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)

    company_name = Column(String)

    title = Column(String)

    apply_url = Column(String, unique=True)

    location = Column(String)

    company_url = Column(String)