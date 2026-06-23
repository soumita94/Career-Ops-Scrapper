from database.db import SessionLocal
from database.model import Job

db = SessionLocal()

jobs = db.query(Job).all()

print(f"Total Jobs: {len(jobs)}")
print()

for job in jobs:
    print(job.title)
    print(job.location)
    print(job.apply_url)
    print("-" * 50)