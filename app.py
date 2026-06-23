from fastapi import FastAPI

from api.admin import (
    router as admin_router
)

from api.jobs import (
    router as jobs_router
)

app = FastAPI()

app.include_router(
    admin_router,
    prefix="/admin",
    tags=["Admin"]
)

app.include_router(
    jobs_router,
    prefix="/jobs",
    tags=["Jobs"]
)