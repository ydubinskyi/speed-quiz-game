from uuid import uuid4
from typing import TYPE_CHECKING

from uuid import uuid4
from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship

from ..db.base import Base

if TYPE_CHECKING:
    from .question import Question  # noqa: F401

class Question(Base):
    """
    Quiz question model
    """

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    content = Column(Text)
    active = Column(Boolean)
    answers = relationship("Answer", back_populates="question")
