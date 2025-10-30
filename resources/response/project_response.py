from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ProjectResponse(BaseModel):
    id: Optional[int] = None
    name: str
    subject: Optional[str]
    start_date: Optional[datetime]
    due_date: Optional[datetime]
    created_by: int
    updated_by: Optional[int]

    model_config = ConfigDict()
    model_config['from_attributes'] = True
