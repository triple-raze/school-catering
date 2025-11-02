from pydantic import BaseModel, Field

class TeacherAuth(BaseModel):
    login: str = Field(max_length=100)
    password: bytes = Field(max_length=60)

class TeacherModel(TeacherAuth):
    id: int
    first_name: str = Field(max_length=50)
    second_name: str = Field(max_length=50)
    patronymic: str = Field(max_length=50)
