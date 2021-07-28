from typing import Any, List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from . import actions, schemas
from .db.session import SessionLocal

# Create all tables in the database.
# Comment this out if you using migrations.
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get DB session.
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"message": "Hello world!"}


@app.get("/questions", response_model=List[schemas.Question], tags=["questions"])
def list_questions(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100
) -> Any:
    question = actions.question.get_all(db=db, skip=skip, limit=limit)
    return question


@app.post(
    "/questions",
    response_model=schemas.Question,
    status_code=HTTP_201_CREATED,
    tags=["questions"],
)
def create_question(
    *, db: Session = Depends(get_db), question_in: schemas.QuestionCreate
) -> Any:
    question = actions.question.create(db=db, obj_in=question_in)
    return question


@app.put(
    "/questions/{id}",
    response_model=schemas.Question,
    tags=["questions"],
)
def update_question(
    *,
    db: Session = Depends(get_db),
    id: UUID4,
    question_in: schemas.QuestionUpdate,
) -> Any:
    question = actions.question.get(db=db, id=id)
    if not question:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Question not found")
    question = actions.question.update(db=db, db_obj=question, obj_in=question_in)
    return question


@app.get(
    "/questions/{id}",
    response_model=schemas.Question,
    tags=["questions"],
)
def get_question(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    question = actions.question.get(db=db, id=id)
    if not question:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Question not found")
    return question


@app.delete(
    "/questions/{id}",
    response_model=schemas.Question,
    tags=["questions"],
)
def delete_question(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    question = actions.question.get(db=db, id=id)
    if not question:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="question not found")
    question = actions.question.remove(db=db, id=id)
    return question
