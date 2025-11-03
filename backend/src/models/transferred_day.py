from pydantic import BaseModel
from datetime import date

class TransferredDayReference(BaseModel):
    id: int

class TransferredDayCreate(BaseModel):
    workday: date
    holiday: date

class TransferredDayRecord(TransferredDayCreate):
    id: int 
