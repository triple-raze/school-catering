from core.database import database
from models.holiday import HolidayCreate, HolidayRecord, HolidayReference


async def get_holiday_by_id(holiday: HolidayReference) -> HolidayRecord | None:
    raw_record = await database.fetchrow(
        "SELECT * FROM holidays WHERE id = $1",
        holiday.id,
    )
    return HolidayRecord(**raw_record) if raw_record else None


async def create_holiday(holiday: HolidayCreate) -> HolidayRecord | None:
    raw_record = await database.fetchrow(
        "INSERT INTO holidays (date) VALUES ($1) RETURNING *",
        holiday.date,
    )
    return HolidayRecord(**raw_record) if raw_record else None

async def delete_holiday_by_id(holiday: HolidayReference) -> None:
    await database.execute("DELETE FROM holidays WHERE id = $1", holiday.id)
