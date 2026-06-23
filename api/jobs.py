from fastapi import APIRouter

from services.search_service import (
    search_jobs
)

router = APIRouter()


@router.get("/search")
def search(keyword: str):

    jobs = search_jobs(keyword)

    return [
        {
            "title": j.title,
            "url": j.apply_url,
            "location": j.location
        }
        for j in jobs
    ]