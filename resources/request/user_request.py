from pydantic import BaseModel, Field, EmailStr


class UpdateUserRequest(BaseModel):
    email: EmailStr = Field(examples=['email@domain.com'])
    username: str = Field(examples=['username'])
    name: str = Field(examples=['Name Example'])
    user_type: int = Field(examples=[1, 2])


class CreateUserRequest(UpdateUserRequest):
    password: str = Field(examples=['password'])
