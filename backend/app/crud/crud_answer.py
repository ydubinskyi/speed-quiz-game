from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from ..crud.base import CRUDBase
from ..models.answer import Answer
from ..schemas.answer import AnswerCreate, AnswerUpdate


class CRUDAnswer(CRUDBase[Answer, AnswerCreate, AnswerUpdate]):
    def create_with_question(
        self,
        db: Session,
        *,
        question_id: UUID4,
        obj_in: AnswerCreate,
    ) -> Answer:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, question_id=question_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_question(
        self, db: Session, *, question_id: UUID4, skip: int = 0, limit: int = 100
    ) -> List[Answer]:
        return (
            db.query(self.model)
            .filter(self.model.question_id == question_id)
            .limit(limit)
            .offset(skip)
            .all()
        )

    def is_active(self, answer: Answer) -> bool:
        return answer.active


answer = CRUDAnswer(Answer)
