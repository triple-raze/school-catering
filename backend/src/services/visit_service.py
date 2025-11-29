from models.student import StudentIdReference
from models.visit import VisitCreate, VisitRecord
from repositories import visit_repository


async def get_student_visits(student_reference: StudentIdReference) -> VisitRecord:
    return await visit_repository.get_visits_by_user_id(student_reference)


async def create_visit(visit_create_data: VisitCreate) -> VisitRecord:
    return await visit_repository.create_visit(visit_create_data)
