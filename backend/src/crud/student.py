from core.database import database
from models.student import StudentCreate, StudentReference
from asyncpg import Record

class StudentGateway:
    async def get_student(student: StudentReference) -> Record:
        return database.fetchrow("SELECT * FROM students WHERE id = $1", (student.id,))
    
    async def create_student(student: StudentCreate) -> None:
        database.execute(
            "INSERT INTO students (class_id, first_name, second_name, patronymic) VALUES ($1, $2, $3)",
            (student.class_id, student.first_name, student.second_name, student.patronymic)
        )

    async def delete_student(student: StudentReference) -> None:
        database.execute("DELETE FROM students WHERE id = $1", (student.id,))
    
