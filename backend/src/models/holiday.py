from datetime import date

from pydantic import BaseModel


class HolidayReference(BaseModel):
    id: int


class HolidayCreate(BaseModel):
    date: date


class HolidayRecord(HolidayCreate):
    id: int


