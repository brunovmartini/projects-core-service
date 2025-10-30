from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProjectRequest(BaseModel):
    name: str = Field(default=None, examples=['Tech Project'])
    subject: Optional[str] = Field(default=None, examples=['Web Application for hospitals management.'])
    start_date: Optional[datetime] = Field(default=None, examples=['2025-10-29 14:22:11.949'])
    due_date: Optional[datetime] = Field(default=None, examples=['2026-10-29 14:22:11.949'])
