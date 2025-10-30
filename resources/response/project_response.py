from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ProjectResponse(BaseModel):
    id: Optional[int] = None
    name: str
    subject: Optional[str]
    start_date: Optional[datetime]
    due_date: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
