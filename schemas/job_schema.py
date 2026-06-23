from pydantic import BaseModel


class CompanyInput(BaseModel):
    company_url: str