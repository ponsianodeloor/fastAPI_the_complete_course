from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from schemas import todo
from models import Todo
from database import SessionLocal


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

TodoSchema = todo.TodoSchema


@router.get("/")
def go_to_docs():
    return RedirectResponse("/docs")


@router.get("/read_all", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todo).all()


@router.get("/todo/{id}", status_code=status.HTTP_200_OK)
async def read_id(db: db_dependency, id: int = Path(gt=0)):
    todo_by_id = db.query(Todo).filter(Todo.id == id).first()
    if todo_by_id is not None:
        return todo_by_id
    raise HTTPException(status_code=404, detail='Todo no encontrado')


@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todos_schema: TodoSchema):
    todo_create = Todo(**todos_schema.dict())

    db.add(todo_create)
    db.commit()


@router.put("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
        db: db_dependency,
        todos_request: TodoSchema,
        id: int = Path(gt=0)
):
    todo_update = db.query(Todo).filter(Todo.id == id).first()

    if todo_update is None:
        raise HTTPException(status_code=404, detail='Todo no encontrado')

    todo_update.title = todos_request.title
    todo_update.description = todos_request.description
    todo_update.priority = todos_request.priority
    todo_update.complete = todos_request.complete

    db.add(todo_update)
    db.commit()


@router.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, id: int = Path(gt=0)):
    todo_delete = db.query(Todo).filter(Todo.id == id).first()

    if todo_delete is None:
        raise HTTPException(status_code=404, detail='ID no encontrado')

    #db.query(todo_delete).filter(Todo.id == id).delete()
    db.delete(todo_delete)
    db.commit()
