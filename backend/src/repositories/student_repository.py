from core.database import database
from models.student import StudentCreate, StudentIdReference, StudentRecord


async def get_student_by_id(student: StudentIdReference) -> StudentRecord | None:
    raw_record =  await database.fetchrow(
        "SELECT * FROM students WHERE id = $1",
        student.id,
    )
    return StudentRecord(**raw_record) if raw_record else None

async def create_student(student: StudentCreate) -> StudentRecord | None:
    raw_record = await database.fetchrow(
        "INSERT INTO students (class_id, first_name, second_name, patronymic) "
        "VALUES ($1, $2, $3) RETURNING *",
        student.class_id,
        student.first_name,
        student.second_name,
        student.patronymic,
    )
    return StudentRecord(**raw_record) if raw_record else None

async def delete_student_by_id(student: StudentIdReference) -> None:
    await database.execute("DELETE FROM students WHERE id = $1", student.id)
