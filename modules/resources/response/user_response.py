from typing import Optional

from pydantic import BaseModel, ConfigDict

from modules.resources.response.user_type_response import UserTypeResponse


class UserResponse(BaseModel):
    id: Optional[int] = None
    email: str
    username: str
    type: UserTypeResponse

    model_config = ConfigDict(from_attributes=True)
