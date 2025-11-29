from exceptions.school_class import SchoolClassNotFoundException
from models.school_class import (
    SchoolClassCreate,
    SchoolClassIdReference,
    SchoolClassPersistence,
    SchoolClassRecord,
)
from models.teacher import TeacherRecord
from repositories import school_class_repository


async def get_school_class(
    school_class_id: SchoolClassIdReference,
) -> SchoolClassRecord:
    school_class_record = await school_class_repository.get_class_by_id(school_class_id)

    if not school_class_record:
        raise SchoolClassNotFoundException

    return school_class_record


async def create_school_class(
    user_school_class_data: SchoolClassCreate,
    teacher: TeacherRecord,
) -> SchoolClassRecord:
    school_class_data = SchoolClassPersistence(
        digit=user_school_class_data.digit,
        letter=user_school_class_data.letter,
        teacher_id=teacher.id,
    )

    return await school_class_repository.create_class(school_class_data)
