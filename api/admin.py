from fastapi import APIRouter

from schemas.job_schema import (
    CompanyInput
)

from services.sync_service import (
    sync_company
)

router = APIRouter()


@router.post("/sync-company")
async def sync(
    data: CompanyInput
):

    return await sync_company(
        data.company_url
    )