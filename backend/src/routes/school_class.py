from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from core.dependecies import get_teacher
from models.school_class import SchoolClassCreate, SchoolClassIdReference
from models.teacher import TeacherRecord
from services import school_class_service

router = APIRouter(prefix="/classes")


@router.get("/{school_class_id}")
async def get_school_class(school_class_id: str) -> JSONResponse:
    school_class_reference = SchoolClassIdReference(id=school_class_id)

    school_class = await school_class_service.get_school_class(school_class_reference)

    return JSONResponse(
        {
            "digit": school_class.digit,
            "letter": school_class.letter,
            "teacher_id": school_class.teacher_id,
            "id": school_class.id,
        },
        status_code=200,
    )


@router.post("/")
async def create_school_class(
    create_school_class_data: SchoolClassCreate,
    teacher: Annotated[TeacherRecord, Depends(get_teacher)],
) -> JSONResponse:
    school_class = await school_class_service.create_school_class(
        create_school_class_data,
        teacher,
    )

    return JSONResponse(
        {
            "digit": school_class.digit,
            "letter": school_class.letter,
            "teacher_id": teacher.id,
            "id": school_class.id,
        },
        status_code=201,
    )
