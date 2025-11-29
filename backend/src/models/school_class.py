from pydantic import BaseModel, Field


class SchoolClassIdReference(BaseModel):
    id: int


class SchoolClassCreate(BaseModel):
    digit: int = Field(max_digits=2)
    letter: str = Field(max_length=1)

class SchoolClassPersistence(SchoolClassCreate):
    teacher_id: int

class SchoolClassRecord(SchoolClassPersistence):
    id: int
