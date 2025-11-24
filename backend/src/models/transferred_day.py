from datetime import date

from pydantic import BaseModel


class TransferredDayIdReference(BaseModel):
    id: int


class TransferredDayCreate(BaseModel):
    workday: date
    holiday: date


class TransferredDayRecord(TransferredDayCreate):
    id: int
