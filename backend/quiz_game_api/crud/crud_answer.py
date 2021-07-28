from ..crud.base import CRUDBase
from ..models.answer import Answer
from ..schemas.answer import AnswerCreate, AnswerUpdate


class CRUDAnswer(CRUDBase[Answer, AnswerCreate, AnswerUpdate]):
    def is_active(self, answer: Answer) -> bool:
        return answer.active


answer = CRUDAnswer(Answer)
