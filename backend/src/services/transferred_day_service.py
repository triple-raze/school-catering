from models.transferred_day import (
    TransferredDayCreate,
    TransferredDayFilter,
    TransferredDayRecord,
)
from repositories import transferred_day_repository


async def get_transferred_day(
    transferred_day_filter: TransferredDayFilter,
) -> list[TransferredDayRecord]:
    return await transferred_day_repository.get_transferred_days_by_date(
        transferred_day_filter,
    )


async def create_transferred_day(
    create_transferred_day_data: TransferredDayCreate,
) -> TransferredDayRecord:
    return await transferred_day_repository.create_transferred_day(
        create_transferred_day_data,
    )
