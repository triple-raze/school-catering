from pydantic import BaseModel
from typing import Literal, Optional
from datetime import date

class VisitReference(BaseModel):
    id: int

class VisitCreate(BaseModel):
    date: date
    student_id: int
    status: Literal['attended', 'skipped', 'absent']

class VisitRecord(VisitCreate):
    id: int
