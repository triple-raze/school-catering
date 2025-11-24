from pydantic import BaseModel, Field


class SchoolClassIdReference(BaseModel):
    id: int


class SchoolClassCreate(BaseModel):
    teacher_id: int
    digit: int = Field(max_digits=2)
    letter: str = Field(max_length=1)


class SchoolClassRecord(SchoolClassCreate):
    id: int
