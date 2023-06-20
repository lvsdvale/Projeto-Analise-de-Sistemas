from typing import Optional, List
from pydantic import BaseModel, HttpUrl, EmailStr
from ProjectSchema import ProjectSchema

class CompanySchema(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    name: str
    city: str
    state: str
    user_id: Optional[int]

    class config:
        orm_mode = True

class CompanySchemaProjects(CompanySchema):
    tasks: Optional[List[ProjectSchema]]
