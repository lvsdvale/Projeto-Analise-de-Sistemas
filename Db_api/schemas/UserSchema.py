from typing import Optional, List
from pydantic import BaseModel, HttpUrl, EmailStr
from ProjectSchema import CompanySchema

class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    admin: bool
    user_id: Optional[int]

    class config:
        orm_mode = True

class UserSchemaCreate(UserSchema):
    password: str

class UserSchemaUpdate(UserSchema):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

class UserSchemaCompanys(UserSchema):
    tasks: Optional[List[CompanySchema]]

