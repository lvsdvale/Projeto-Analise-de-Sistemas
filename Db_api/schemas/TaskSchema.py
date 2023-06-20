from typing import Optional, List
from pydantic import BaseModel, HttpUrl, EmailStr
from TimeEntrieSchema import TimeEntrieSchema
import datetime

class TaskSchema(BaseModel):
    id: Optional[int] = None
    name: str
    priority: str
    deadline: datetime.date
    project_id: Optional[int]

    class config:
        orm_mode = True

class ProjectSchemaTasks(TaskSchema):
    tasks: Optional[List[TimeEntrieSchema]]

class TaskSchemaUpdate(BaseModel):
    name: Optional[str]
    priority: Optional[str]
    deadline: Optional[datetime.date]
