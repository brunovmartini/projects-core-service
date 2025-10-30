from typing import Optional

from pydantic import BaseModel, ConfigDict

from resources.response.user_type_response import UserTypeResponse


class UserResponse(BaseModel):
    id: Optional[int] = None
    email: str
    username: str
    name: str
    type: UserTypeResponse
    created_by: int
    updated_by: Optional[int]

    model_config = ConfigDict()
    model_config['from_attributes'] = True
