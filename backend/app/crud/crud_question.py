from ..crud.base import CRUDBase
from ..models.question import Question
from ..schemas.question import QuestionCreate, QuestionUpdate


class CRUDQuestion(CRUDBase[Question, QuestionCreate, QuestionUpdate]):
    def is_active(self, question: Question) -> bool:
        return question.active


question = CRUDQuestion(Question)
