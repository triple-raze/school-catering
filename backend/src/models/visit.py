from pydantic import BaseModel
from typing import Literal, Optional
from datetime import date

class VisitReference(BaseModel):
    id: int

class VisitCreate(BaseModel):
    date: date
    student_id: int
    status: str = Literal['attended', 'skipped', 'absent']

class VisitUpdate(BaseModel):
    id: int | None
    date: date | None
    student_id: int | None
    status: str | None = Literal['attended', 'skipped', 'absent']
