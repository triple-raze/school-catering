from pydantic import BaseModel, Field
from datetime import date

class Holiday(BaseModel):
    id: int
    date: date
