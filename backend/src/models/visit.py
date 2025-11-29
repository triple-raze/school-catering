from datetime import date
from typing import Literal

from pydantic import BaseModel


class VisitIdReference(BaseModel):
    id: int


class VisitCreate(BaseModel):
    date: date
    student_id: int
    status: Literal["attended", "skipped", "absent"]


class VisitRecord(VisitCreate):
    id: int
