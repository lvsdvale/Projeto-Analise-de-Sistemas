from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from UserModel import UserModel
from ProjectModel import ProjectModel


from core.config import settings


class CompanyModel(settings.DBBaseModel):
    __tablename__ = 'Company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    name = Column(String(256), nullable=True)
    city = Column(String(256), nullable=True)
    state = Column(String(256), nullable=True)
    created_by_user = relationship(
        'UserModel',
        back_populates="companys",
        lazy="joined")
    projects = relationship(
        'ProjectModel',
        cascade="all,delete-orphan",
        back_populates="company",
        uselist=True,
        lazy="joined")