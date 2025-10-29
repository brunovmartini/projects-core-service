from pydantic import BaseModel, Field, EmailStr


class UpdateUserRequest(BaseModel):
    email: EmailStr = Field(default=None, examples=['email@domain'])
    username: str = Field(default=None, examples=["Name Example"])
    user_type: int = Field(default=None, examples=[1, 2])


class CreateUserRequest(UpdateUserRequest):
    password: str = Field(default=None, examples=['password'])
