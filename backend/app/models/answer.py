from typing import TYPE_CHECKING

from uuid import uuid4
from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship

from ..db.base import Base

if TYPE_CHECKING:
    from .question import Question  # noqa: F401

class Answer(Base):
    """
    Quiz question answer model
    """

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    content = Column(Text)
    active = Column(Boolean)
    correct = Column(Boolean)
    question_id = Column(UUID(as_uuid=True), ForeignKey("question.id"))
    question = relationship("Question", back_populates="answers")
