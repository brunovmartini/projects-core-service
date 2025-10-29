from pydantic import BaseModel, ConfigDict


class UserTypeResponse(BaseModel):
    id: int
    user_type: str

    model_config = ConfigDict(from_attributes=True)
