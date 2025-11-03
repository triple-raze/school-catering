from pydantic import BaseModel
from datetime import date

class HolidayReference(BaseModel):
    id: int

class HolidayCreate(BaseModel):
    date: date

class HolidayRecord(HolidayCreate):
    id: int
