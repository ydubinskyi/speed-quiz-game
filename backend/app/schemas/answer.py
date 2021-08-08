from typing import Optional

from pydantic import BaseModel, UUID4


# Shared properties
class AnswerBase(BaseModel):
    question_id: Optional[UUID4] = None
    content: Optional[str] = None
    active: Optional[bool] = False
    correct: Optional[bool] = False


# Properties to receive via API on creation
class AnswerCreate(AnswerBase):
    content: str
    correct: bool


# Properties to receive via API on update
class AnswerUpdate(AnswerBase):
    pass


class AnswerInDBBase(AnswerBase):
    id: Optional[UUID4] = None
    question_id: UUID4

    class Config:
        orm_mode = True


# Additional properties to return via API
class Answer(AnswerInDBBase):
    pass


# Additional properties stored in DB
class AnswerInDB(AnswerInDBBase):
    pass
