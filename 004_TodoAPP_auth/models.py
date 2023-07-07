from database import Base
from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel, Field


class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)


class TodosRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=10)
    priority: int = Field(gt=0, lt=6)
    complete: bool

