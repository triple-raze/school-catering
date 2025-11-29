from core.database import database
from models.teacher import (
    TeacherCreate,
    TeacherIdReference,
    TeacherLoginReference,
    TeacherRecord,
)


async def get_teacher_by_id(teacher: TeacherIdReference) -> TeacherRecord:
    raw_record = await database.fetchrow(
        "SELECT * FROM teachers WHERE id = $1",
        teacher.id,
    )
    return TeacherRecord(**raw_record) if raw_record else None


async def get_teacher_by_login(teacher: TeacherLoginReference) -> TeacherRecord | None:
    raw_record = await database.fetchrow(
        "SELECT * FROM teachers WHERE login = $1",
        teacher.login,
    )
    return TeacherRecord(**raw_record) if raw_record else None


async def create_teacher(teacher: TeacherCreate) -> TeacherRecord | None:
    raw_record = await database.fetchrow(
        "INSERT INTO teachers "
        "(login, password_hash, first_name, second_name, patronymic) "
        "VALUES ($1, $2, $3, $4, $5) RETURNING *",
        teacher.login,
        teacher.password_hash,
        teacher.first_name,
        teacher.second_name,
        teacher.patronymic,
    )
    return TeacherRecord(**raw_record) if raw_record else None


async def delete_teacher_by_id(teacher: TeacherIdReference) -> None:
    await database.execute("DELETE FROM teachers WHERE id = $1", teacher.id)
