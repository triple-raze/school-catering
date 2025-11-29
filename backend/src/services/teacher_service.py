from models.teacher import TeacherIdReference, TeacherRecord
from repositories import teacher_repository


async def get_teacher(teacher_reference: TeacherIdReference) -> TeacherRecord:
    return await teacher_repository.get_teacher_by_id(teacher_reference)
