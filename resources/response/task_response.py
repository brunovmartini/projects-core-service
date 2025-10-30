from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class TaskResponse(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str]
    start_date: Optional[datetime]
    due_date: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
