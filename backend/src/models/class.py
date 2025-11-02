from pydantic import BaseModel, Field

class ClassModel(BaseModel):
    id: int
    teacher_id: int
    digit: int = Field(max_digits=2)
    letter: str = Field(max_length=1)

