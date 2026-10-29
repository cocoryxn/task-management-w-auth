from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email : EmailStr
    username : str

class CreateUser(UserBase):
    hash_password : str

class CreatedUserResponse(BaseModel):
    msg : str