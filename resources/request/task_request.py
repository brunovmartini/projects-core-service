from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TaskRequest(BaseModel):
    name: str = Field(examples=['Create User Endpoint'])
    description: Optional[str] = Field(default=None, examples=['Task for creating an endpoint to create an user.'])
    start_date: Optional[datetime] = Field(default=None, examples=['2025-10-29 14:22:11.949'])
    due_date: Optional[datetime] = Field(default=None, examples=['2026-10-29 14:22:11.949'])
