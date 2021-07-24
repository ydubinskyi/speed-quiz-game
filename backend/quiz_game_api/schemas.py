from typing import Optional

from pydantic import BaseModel, UUID4


# Shared properties
class QuestionBase(BaseModel):
    content: Optional[str] = None
    is_active: Optional[bool] = False


# Properties to receive via API on creation
class QuestionCreate(QuestionBase):
    content: str


# Properties to receive via API on update
class QuestionUpdate(QuestionBase):
    content: str


class QuestionInDBBase(QuestionBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Question(QuestionInDBBase):
    pass


# Additional properties stored in DB
class QuestionInDB(QuestionInDBBase):
    pass
