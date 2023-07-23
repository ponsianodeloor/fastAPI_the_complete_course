from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from models import User
from database import get_db
from starlette import status
from routers.user import get_user_by_token
from passlib.context import CryptContext


router = APIRouter(
    prefix='/users',
    tags=['users']
)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_user_by_token)]


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


@router.get("/user")
async def get_auth_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    user_by_auth = db.query(User).filter(User.id == user.get('id')).first()

    if user_by_auth is not None:
        return user_by_auth
    raise HTTPException(status_code=404, detail='Todo no encontrado')


@router.put("/update_user_password", status_code=status.HTTP_204_NO_CONTENT)
async def update_user_password(
        user: user_dependency,
        db: db_dependency,
        user_verification: UserVerification,
):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    user_update_password_by_auth = db.query(User).filter(User.id == user.get('id')).first()

    if not bcrypt_context.verify(user_verification.password, user_update_password_by_auth.hashed_password):
        raise HTTPException(status_code=401, detail='Error on Password Change')

    user_update_password_by_auth.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_update_password_by_auth)
    db.commit()



