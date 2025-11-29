from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from core.dependecies import get_teacher
from models.teacher import TeacherRecord
from models.transferred_day import TransferredDayCreate, TransferredDayFilter
from services import transferred_day_service

router = APIRouter(prefix="/transferred-days")


@router.get("/")
async def get_transferred_day(start: int, end: int) -> JSONResponse:
    transferred_day_filter = TransferredDayFilter(start=start, end=end)

    transferred_day_records = await transferred_day_service.get_transferred_day(
        transferred_day_filter,
    )

    response = [
        {
        "workday": record.workday,
        "holiday": record.holiday,
        "id": record.id,
        } for record in transferred_day_records
    ]

    return JSONResponse(response, status_code=200)


@router.post("/")
async def create_transferred_day(
    create_transferred_day_data: TransferredDayCreate,
    teacher: Annotated[TeacherRecord, Depends(get_teacher)],  # noqa: ARG001
) -> JSONResponse:
    transferred_day_record = await transferred_day_service.create_transferred_day(
        create_transferred_day_data,
    )

    return JSONResponse(
        {
            "workday": transferred_day_record.workday,
            "holiday": transferred_day_record.holiday,
            "id": transferred_day_record.id,
        },
        status_code=200,
    )
