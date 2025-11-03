from core.database import database
from models.visit import VisitCreate, VisitReference
from asyncpg import Record

async def get_visit(visit: VisitReference) -> Record:
    return database.fetchrow("SELECT * FROM visits WHERE id = $1", (visit.id,))

async def insert_visit(visit: VisitCreate) -> None:
    database.execute(
        "INSERT INTO visits (student_it, status, date) VALUES ($1, $2, $3)",
        (visit.student_id, visit.status, visit.date)
    )

async def delete_visit(visit: VisitReference) -> None:
    database.execute("DELETE FROM visits WHERE id = $1", (visit.id,))
    
