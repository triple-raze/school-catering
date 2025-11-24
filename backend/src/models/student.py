from pydantic import BaseModel, Field


class StudentIdReference(BaseModel):
    id: int


class StudentCreate(BaseModel):
    class_id: int
    first_name: str = Field(max_length=50)
    second_name: str = Field(max_length=50)
    patronymic: str = Field(max_length=50)


class StudentRecord(StudentCreate):
    id: int
