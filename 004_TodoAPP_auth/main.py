from typing import Annotated
from sqlalchemy.orm import Session

from fastapi.responses import RedirectResponse
from fastapi import FastAPI, Depends, HTTPException, Path
from starlette import status

import models
from models import Todos, TodosRequest
from database import engine, SessionLocal

from routers import auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# incluir rutas desde otros archivos
app.include_router(auth.router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
def go_to_docs():
    return RedirectResponse("/docs")


@app.get("/read_all", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()


@app.get("/todo/{id}", status_code=status.HTTP_200_OK)
async def read_id(db: db_dependency, id: int = Path(gt=0)):
    todo = db.query(Todos).filter(Todos.id == id).first()
    if todo is not None:
        return todo
    raise HTTPException(status_code=404, detail='Todo no encontrado')


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todos_request: TodosRequest):
    todo_model = Todos(**todos_request.dict())

    db.add(todo_model)
    db.commit()


@app.put("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
        db: db_dependency,
        todos_request: TodosRequest,
        id: int = Path(gt=0)
):
    todo_model = db.query(Todos).filter(Todos.id == id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo no encontrado')

    todo_model.title = todos_request.title
    todo_model.description = todos_request.description
    todo_model.priority = todos_request.priority
    todos_request.complete = todos_request.complete

    db.add(todo_model)
    db.commit()


@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail='ID no encontrado')

    db.query(Todos).filter(Todos.id == id).delete()
    db.commit()
