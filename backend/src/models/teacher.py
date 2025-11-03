from pydantic import BaseModel, Field

class TeacherReference(BaseModel):
    id: int

class TeacherLogin(BaseModel):
    login: str = Field(max_length=100)
    password: bytes = Field(max_length=60)

class TeacherDelete(TeacherLogin):
    id: int

class TeacherCreate(TeacherLogin):
    first_name: str = Field(max_length=50)
    second_name: str = Field(max_length=50)
    patronymic: str = Field(max_length=50)

class TeacherUpdate(BaseModel):
    id: int | None
    login: str | None = Field(max_length=100)
    password: bytes | None = Field(max_length=60)
    first_name: str | None = Field(max_length=50)
    second_name: str | None = Field(max_length=50)
    patronymic: str | None = Field(max_length=50)
