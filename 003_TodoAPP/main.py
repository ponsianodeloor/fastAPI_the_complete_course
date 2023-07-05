from typing import Annotated
from sqlalchemy.orm import Session

from fastapi.responses import RedirectResponse
from fastapi import FastAPI, Depends, HTTPException, Path
from starlette import status

import models
from models import Todos
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


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


