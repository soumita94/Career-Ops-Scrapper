from agents.browser_use_agent import extract_jobs

from database.db import SessionLocal
from database.model import Job


async def sync_company(company_url):

    jobs_data = await extract_jobs(
        company_url
    )

    print("JOBS DATA:")
    print(jobs_data)
    print("COUNT:", len(jobs_data.get("jobs", [])))
    
    db = SessionLocal()

    inserted = 0

    for job in jobs_data["jobs"]:

        existing = (
            db.query(Job)
            .filter(
                Job.apply_url == job["url"]
            )
            .first()
        )

        if existing:
            continue

        db_job = Job(
            title=job["title"],
            apply_url=job["url"],
            location=job["location"],
            company_url=company_url
        )

        db.add(db_job)

        inserted += 1

    db.commit()

    return {
        "inserted": inserted
    }