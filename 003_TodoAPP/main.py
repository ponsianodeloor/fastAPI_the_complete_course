from typing import Annotated
from sqlalchemy.orm import Session

from fastapi.responses import RedirectResponse
from fastapi import FastAPI, Depends
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

