from sqlalchemy import Integer, String, Column, Float, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from TaskModel import TaskModel




from core.config import settings


class TimeEntrieModel(settings.DBBaseModel):
    __tablename__ = 'TimeEntrie'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start = Column(DateTime, nullable=True)
    duration = Column(Float, nullable=True)
    project = relationship(
        'TaskModel',
        back_populates="timeEntrie",
        lazy="joined")
    