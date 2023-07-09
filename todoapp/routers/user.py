from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from starlette import status
from schemas import user
from database import get_db
from models import User
from passlib.context import CryptContext

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

db_dependency = Annotated[Session, Depends(get_db)]

UserSchema = user.UserSchema


@router.get("/users")
async def get_users(db: db_dependency):
    return db.query(User).all()


@router.post("/users/create", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: UserSchema):
    create_user_model = User(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )

    db.add(create_user_model)
    db.commit()


def auth_user(username: str, password: str, db):
    get_user = db.query(User).filter(User.username == username).first()
    if not get_user:
        return False

    if not bcrypt_context.verify(password, get_user.hashed_password):
        return False

    return True


@router.post("/token")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: db_dependency
):
    login_user = auth_user(form_data.username, form_data.password, db)

    if not login_user:
        return 'Failed Authentication'
    return form_data.username
