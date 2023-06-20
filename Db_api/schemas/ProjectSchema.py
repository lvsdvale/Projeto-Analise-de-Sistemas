from typing import Optional, List
from pydantic import BaseModel, HttpUrl, EmailStr
from TaskSchema import TaskSchema
import datetime

class ProjectSchema(BaseModel):
    id: Optional[int] = None
    name: str
    deadline: datetime.date
    company_id: Optional[int]

    class config:
        orm_mode = True

class ProjectSchemaTasks(ProjectSchema):
    tasks: Optional[List[TaskSchema]]

class ProjectSchemaUpdate(ProjectSchema):
    name: Optional[str]
    deadline: Optional[datetime.date]

