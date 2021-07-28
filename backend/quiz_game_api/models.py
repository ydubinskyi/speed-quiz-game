from uuid import uuid4
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Boolean

from .db.base import Base


class Question(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    content = Column(String)
    is_active = Column(Boolean)
