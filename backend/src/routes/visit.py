from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from core.dependecies import get_teacher
from models.student import StudentIdReference
from models.teacher import TeacherRecord
from models.visit import VisitCreate
from services import visit_service

router = APIRouter(prefix="/visits")


@router.get("/{student_id}")
async def get_visit(student_id: str) -> JSONResponse:
    student_reference = StudentIdReference(student_id)

    visit_record = await visit_service.get_student_visits(student_reference)

    return JSONResponse(
        {
            "date": visit_record.date,
            "student_id": visit_record.student_id,
            "status": visit_record.status,
            "id": visit_record.id,
        },
        status_code=200,
    )


@router.post("/")
async def create_visit(
    visit_create_data: VisitCreate,
    teacher: Annotated[TeacherRecord, Depends(get_teacher)],  # noqa: ARG001
) -> JSONResponse:
    visit_record = await visit_service.create_visit(visit_create_data)

    return JSONResponse(
        {
            "date": visit_record.date,
            "student_id": visit_record.student_id,
            "status": visit_record.status,
            "id": visit_record.id,
        },
        status_code=201,
    )
