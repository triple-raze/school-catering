from core.database import database
from models.transferred_day import (
    TransferredDayCreate,
    TransferredDayIdReference,
    TransferredDayRecord,
)


async def get_transferred_day_by_id(
    transferred_day: TransferredDayIdReference,
) -> TransferredDayRecord | None:
    raw_record = await database.fetchrow(
        "SELECT * FROM transferred_days WHERE id = $1",
        transferred_day.id,
    )
    return TransferredDayRecord(**raw_record) if raw_record else None


async def create_transferred_day(
    transferred_day: TransferredDayCreate,
) -> TransferredDayRecord | None:
    raw_record = await database.fetchrow(
        "INSERT INTO transferred_days (workday, holiday) VALUES ($1, $2) RETURNING *",
        transferred_day.workday,
        transferred_day.holiday,
    )
    return TransferredDayRecord(**raw_record) if raw_record else None


async def delete_transferred_day_by_id(
    transferred_day: TransferredDayIdReference,
) -> None:
    await database.execute(
        "DELETE FROM transferred_days WHERE id = $1",
        transferred_day.id,
    )
