from core.database import database
from models.holiday import HolidayCreate, HolidayReference
from asyncpg import Record

class HolidayGateway:
    async def get_holiday(holiday: HolidayReference) -> Record:
        return database.fetchrow("SELECT * FROM holidays WHERE id = $1", (holiday.id,))
    
    async def create_holiday(holiday: HolidayCreate) -> None:
        database.execute("INSERT INTO holidays (date) VALUES ($1)", (holiday.date,))

    async def delete_holiday(holiday: HolidayReference) -> None:
        database.execute("DELETE FROM holidays WHERE id = $1", (holiday.id,))
    
