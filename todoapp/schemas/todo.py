from pydantic import BaseModel, Field


class TodoSchema(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=10)
    priority: int = Field(gt=0, lt=6)
    complete: bool
    user_id: int
