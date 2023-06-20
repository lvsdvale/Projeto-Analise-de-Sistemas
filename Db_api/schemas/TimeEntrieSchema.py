from typing import Optional, List
from pydantic import BaseModel, HttpUrl, EmailStr
from TimeEntrieSchema import TimeEntrieSchema
import datetime

class TimeEntrieSchema(BaseModel):
    id: Optional[int] = None
    start: datetime.datetime
    duration: float
    task_id: Optional[int]

    class config:
        orm_mode = True

