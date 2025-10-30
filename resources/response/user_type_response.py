from pydantic import BaseModel, ConfigDict


class UserTypeResponse(BaseModel):
    id: int
    user_type: str

    model_config = ConfigDict()
    model_config['from_attributes'] = True
