from pydantic import BaseModel, Field
from typing import Literal
from datetime import date

class Visit(BaseModel):
    id: int
    class_student_id: int
    status: str = Literal['attended', 'skipped', 'absent']
    date: date
