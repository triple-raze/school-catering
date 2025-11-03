from core.database import database
from models.teacher import TeacherCreate, TeacherReference
from asyncpg import Record

class TeacherGateway:
    async def get_teacher(teacher: TeacherReference) -> Record:
        return database.fetchrow("SELECT * FROM teachers WHERE id = $1", (teacher.id,))
    
    async def create_teacher(teacher: TeacherCreate) -> None:
        database.execute(
            """INSERT INTO teachers (login, password, first_name, second_name, patronymic) 
            VALUES ($1, $2, $3, $4, $5)""",
            (teacher.login, teacher.password, teacher.first_name, teacher.second_name, teacher.patronymic)
        )

    async def delete_teacher(teacher: TeacherReference) -> None:
        database.execute("DELETE FROM teachers WHERE id = $1", (teacher.id,))
    
