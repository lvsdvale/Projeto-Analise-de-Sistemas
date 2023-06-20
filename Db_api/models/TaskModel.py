from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from ProjectModel import ProjectModel
from TimeEntrieModel import TimeEntrieModel



from core.config import settings


class TaskModel(settings.DBBaseModel):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    priority = Column(String(256), nullable=True)
    deadline = Column(Date, nullable=True)
    project = relationship(
        'ProjectModel',
        back_populates="tasks",
        lazy="joined")
    timeEntrie = relationship(
        'TimeEntrieModel',
        cascade="all,delete-orphan",
        back_populates="task",
        uselist=True,
        lazy="joined")