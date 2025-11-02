from pydantic import BaseModel, Field

class StudentModel(BaseModel):
    id: int
    first_name: str = Field(max_length=50)
    second_name: str = Field(max_length=50)
    patronymic: str = Field(max_length=50)


