from database.db import SessionLocal
from database.model import Job


def search_jobs(keyword):

    db = SessionLocal()

    jobs = (
        db.query(Job)
        .filter(
            Job.title.ilike(
                f"%{keyword}%"
            )
        )
        .all()
    )

    return jobs