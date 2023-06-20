from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from CompanyModel import CompanyModel


from core.config import settings


class UserModel(settings.DBBaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    admin = Column(Boolean, default=False)
    companys = relationship(
        'CompanyModel',
        cascade="all,delete-orphan",
        back_populates="created_by_user",
        uselist=True,
        lazy="joined") 
   