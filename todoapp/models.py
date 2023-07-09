from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from pydantic import BaseModel, Field


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)


class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))


class TodosRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=10)
    priority: int = Field(gt=0, lt=6)
    complete: bool

