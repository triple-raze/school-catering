from pydantic import BaseModel, Field

class TeacherReference(BaseModel):
    id: int

class TeacherLogin(BaseModel):
    login: str = Field(max_length=100)
    password: bytes = Field(max_length=60)

class TeacherCreate(TeacherLogin):
    first_name: str = Field(max_length=50)
    second_name: str = Field(max_length=50)
    patronymic: str = Field(max_length=50)

class TeacherRecord(TeacherCreate):
    id: int
