from pydantic import BaseModel, Field

class ClassReference(BaseModel):
    id: int

class ClassCreate(BaseModel):
    teacher_id: int
    digit: int = Field(max_digits=2)
    letter: str = Field(max_length=1)

class ClassUpdate(BaseModel):
    teacher_id: int | None
    digit: int | None = Field(max_digits=2)
    letter: str | None = Field(max_length=1)
    id: int | None
