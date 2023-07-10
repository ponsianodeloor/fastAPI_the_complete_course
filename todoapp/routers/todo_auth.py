from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from schemas import todo_auth
from models import Todo
from database import get_db
from routers.user import get_user_by_token

router = APIRouter(
    prefix='/todo_auth',
    tags=['todo_auth']
)


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_user_by_token)]

TodoAuthSchema = todo_auth.TodoAuthSchema


@router.get("/read_all", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todo).all()


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def read_id(db: db_dependency, id: int = Path(gt=0)):
    todo_by_id = db.query(Todo).filter(Todo.id == id).first()
    if todo_by_id is not None:
        return todo_by_id
    raise HTTPException(status_code=404, detail='Todo no encontrado')


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(
        user: user_dependency,
        db: db_dependency,
        todos_schema: TodoAuthSchema
):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    todo_create = Todo(**todos_schema.dict(), user_id=user.get('id'))

    db.add(todo_create)
    db.commit()


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
        db: db_dependency,
        todos_request: TodoAuthSchema,
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


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, id: int = Path(gt=0)):
    todo_delete = db.query(Todo).filter(Todo.id == id).first()

    if todo_delete is None:
        raise HTTPException(status_code=404, detail='ID no encontrado')

    db.delete(todo_delete)
    db.commit()
