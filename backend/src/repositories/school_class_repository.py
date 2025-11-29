from core.database import database
from models.school_class import (
    SchoolClassCreate,
    SchoolClassIdReference,
    SchoolClassRecord,
)


async def get_class_by_id(
    school_class: SchoolClassIdReference,
) -> SchoolClassRecord | None:
    raw_record = await database.fetchrow(
        "SELECT * FROM students WHERE id = $1",
        school_class.id,
    )
    return SchoolClassRecord(**raw_record) if raw_record else None


async def create_class(school_class: SchoolClassCreate) -> SchoolClassRecord | None:
    raw_record = await database.fetchrow(
        "INSERT INTO classes (teacher_id, digit, letter) "
        "VALUES ($1, $2, $3) RETURNONG *",
        school_class.teacher_id,
        school_class.digit,
        school_class.letter,
    )
    return SchoolClassRecord(**raw_record) if raw_record else None


async def delete_class_by_id(school_class: SchoolClassIdReference) -> None:
    await database.execute("DELETE FROM classes WHERE id = $1", school_class.id)
