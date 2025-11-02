from pydantic import BaseModel, Field
from datetime import date

class TransferredDay(BaseModel):
    id: int
    workday: date
    holiday: date
