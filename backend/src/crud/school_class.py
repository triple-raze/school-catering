from core.database import database
from models.school_class import ClassCreate, ClassReference
from asyncpg import Record

class ClassGateway:
    async def get_class(school_class: ClassReference) -> Record:
        return database.fetchrow("SELECT * FROM users WHERE id = $1", (school_class.id,))
    
    async def create_class(school_class: ClassCreate) -> None:
        database.execute(
            "INSERT INTO classes (teacher_id, digit, letter) VALUES ($1, $2, $3)",
            (school_class.teacher_id, school_class.digit, school_class.letter)
        )

    async def delete_class(school_class: ClassReference) -> None:
        database.execute("DELETE FROM classes WHERE id = $1", (school_class.id,))
    
