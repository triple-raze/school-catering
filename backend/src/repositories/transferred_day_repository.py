from core.database import database
from models.transferred_day import (
    TransferredDayCreate,
    TransferredDayFilter,
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


async def get_transferred_days_by_date(
    transferred_day_reference: TransferredDayIdReference,
    transferred_day_filter: TransferredDayFilter,
) -> list[TransferredDayRecord] | None:
    raw_records = await database.fetchrow(
        "SELECT FROM transferred_days WHERE id=$1 AND "
        "(workday BETWEEN $2 AND $3 OR holiday BETWEEN $2 AND $3)",
        transferred_day_reference.id,
        transferred_day_filter.start,
        transferred_day_filter.end,
    )
    records = [TransferredDayRecord(**raw_record) for raw_record in raw_records]
    return records if raw_records else None


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
