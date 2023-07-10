from fastapi import FastAPI
import models
from database import engine
from routers import user, todo, todo_auth
from fastapi.responses import RedirectResponse


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def redirect():
    return RedirectResponse("/docs")


app.include_router(user.router)
app.include_router(todo.router)
app.include_router(todo_auth.router)

