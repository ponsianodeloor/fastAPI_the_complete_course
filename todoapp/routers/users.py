from typing import Annotated
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


@router.get("/user")
async def get_auth_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    user_by_auth = db.query(User).filter(User.id == user.get('id')).first()

    if user_by_auth is not None:
        return user_by_auth
    raise HTTPException(status_code=404, detail='Todo no encontrado')


@router.get("/update_user_password/{new_password}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user_password(
        user: user_dependency,
        db: db_dependency,
        new_password: str,
):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    user_update_password_by_auth = db.query(User).filter(User.id == user.get('id')).first()

    if user_update_password_by_auth is None:
        raise HTTPException(status_code=404, detail='Todo no encontrado')

    user_update_password_by_auth.password = new_password
    db.add(user_update_password_by_auth)
    db.commit()



