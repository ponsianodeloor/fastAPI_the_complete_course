from pydantic import BaseModel


class UserSchema(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    role: str
