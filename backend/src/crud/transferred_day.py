from core.database import database
from models.transferred_day import TransferredDayCreate, TransferredDayReference
from asyncpg import Record

async def get_transferred_day(transferred_day: TransferredDayReference) -> Record:
    return database.fetchrow("SELECT * FROM transferred_days WHERE id = $1", (transferred_day.id,))

async def insert_transferred_day(transferred_day: TransferredDayCreate) -> None:
    database.execute(
        "INSERT INTO transferred_days (workday, holiday) VALUES ($1)", 
        (transferred_day.workday, transferred_day.holiday)
        )
    
async def delete_transferred_day(transferred_day: TransferredDayReference) -> None:
    database.execute("DELETE FROM transferred_days WHERE id = $1", (transferred_day.id,))
    
