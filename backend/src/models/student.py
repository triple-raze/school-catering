from pydantic import BaseModel, Field

class StudentReference(BaseModel):
    id: int

class StudentCreate(BaseModel):
    class_id: int
    first_name: str = Field(max_length=50)
    second_name: str = Field(max_length=50)
    patronymic: str = Field(max_length=50)

class StudentUpdate(BaseModel):
    id: int | None
    class_id: int | None
    first_name: str | None = Field(max_length=50)
    second_name: str | None = Field(max_length=50)
    patronymic: str | None = Field(max_length=50)

