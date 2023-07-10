from datetime import timedelta, datetime
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from schemas import user, token
from database import get_db
from models import User
from passlib.context import CryptContext

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

router = APIRouter(
    prefix='/user',
    tags=['user']
)

SECRET_KEY = '197b2c37c391bed93fe80344fe73b806947a65e36206e05a1a23c2fa12702fe3'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='user/token')

db_dependency = Annotated[Session, Depends(get_db)]

UserSchema = user.UserSchema
TokenSchema = token.TokenSchema


@router.get("/")
async def get_users(db: db_dependency):
    return db.query(User).all()


@router.post("/create", status_code=status.HTTP_201_CREATED)
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

    return get_user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {
        'sub': username, 'id': user_id
    }

    expires = datetime.utcnow() + expires_delta

    encode.update({
        'exp': expires
    })

    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_user_by_token(user_token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(user_token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')

        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
        return {
            'username': username,
            'id': user_id
        }
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')


@router.post("/token", response_model=TokenSchema)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: db_dependency
):
    login_user = auth_user(form_data.username, form_data.password, db)

    if not login_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')

    get_token = create_access_token(login_user.username, login_user.id, timedelta(minutes=20))

    return {
        'access_token': get_token,
        'token_type': 'bearer'
    }
