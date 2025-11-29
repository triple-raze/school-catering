from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.teacher import TeacherIdReference
from services import teacher_service

router = APIRouter(prefix="/teachers")


@router.get("/{teacher_id}")
async def get_teacher(teacher_id: int) -> JSONResponse:
    teacher_reference = TeacherIdReference(teacher_id)

    teacher_record = await teacher_service.get_teacher(teacher_reference)

    return JSONResponse(
        {
            "first_name": teacher_record.first_name,
            "second_name": teacher_record.second_name,
            "patronymic": teacher_record.patronymic,
            "id": teacher_record.id,
        },
        status_code=200,
    )
