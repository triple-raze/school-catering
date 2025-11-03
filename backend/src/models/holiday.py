from pydantic import BaseModel
from datetime import date

class HolidayReference(BaseModel):
    id: int

class HolidayCreate(BaseModel):
    date: date

class HolidayUpdate(BaseModel):
    id: int | None
    date: date | None
