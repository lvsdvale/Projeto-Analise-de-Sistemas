from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from CompanyModel import CompanyModel
from TaskModel import TaskModel


from core.config import settings


class ProjectModel(settings.DBBaseModel):
    __tablename__ = 'Project'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    deadline = Column(Date, nullable=True)
    company = relationship(
        'CompanyModel',
        back_populates="projects",
        lazy="joined")
    tasks = relationship(
        'TaskModel',
        cascade="all,delete-orphan",
        back_populates="project",
        uselist=True,
        lazy="joined")
    
