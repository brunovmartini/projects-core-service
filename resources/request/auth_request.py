from pydantic import BaseModel, Field, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr = Field(examples=['email@domain.com'])
    password: str = Field(examples=['password'])
