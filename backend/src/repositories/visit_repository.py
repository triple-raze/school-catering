from core.database import database
from models.student import StudentIdReference
from models.visit import VisitCreate, VisitIdReference, VisitRecord


async def get_visit_by_id(visit: VisitIdReference) -> VisitRecord | None:
    raw_record = await database.fetchrow("SELECT * FROM visits WHERE id = $1", visit.id)
    return VisitRecord(**raw_record) if raw_record else None


async def get_visits_by_user_id(
    student_reference: StudentIdReference,
) -> list[VisitRecord]:
    raw_record = await database.fetchrow(
        "SELECT FROM visits WHERE student_id=$1",
        student_reference.id,
    )
    return VisitRecord(**raw_record) if raw_record else None


async def create_visit(visit: VisitCreate) -> VisitRecord | None:
    raw_record = await database.fetchrow(
        "INSERT INTO visits (student_id, status, date) VALUES ($1, $2, $3) RETURNING *",
        visit.student_id,
        visit.status,
        visit.date,
    )
    return VisitRecord(**raw_record) if raw_record else None


async def delete_visit_by_id(visit: VisitIdReference) -> None:
    await database.execute("DELETE FROM visits WHERE id = $1", visit.id)
