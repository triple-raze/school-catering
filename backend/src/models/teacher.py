from pydantic import BaseModel, Field


class TeacherIdReference(BaseModel):
    id: int


class TeacherLoginReference(BaseModel):
    login: str


class TeacherLogin(BaseModel):
    login: str = Field(max_length=100)
    password: str = Field(max_length=100)


class TeacherRegister(TeacherLogin):
    first_name: str = Field(max_length=50)
    second_name: str = Field(max_length=50)
    patronymic: str = Field(max_length=50)


class TeacherCreate(BaseModel):
    login: str = Field(max_length=100)
    password_hash: str = Field(max_length=100)
    first_name: str = Field(max_length=50)
    second_name: str = Field(max_length=50)
    patronymic: str = Field(max_length=50)


class TeacherRecord(TeacherCreate):
    id: int



