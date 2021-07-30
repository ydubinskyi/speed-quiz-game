from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Question])
def read_questions(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    questions = crud.question.get_multi(db=db, skip=skip, limit=limit)
    return questions


@router.post(
    "/",
    response_model=schemas.Question,
    status_code=HTTP_201_CREATED,
)
def create_question(
    *, db: Session = Depends(deps.get_db), question_in: schemas.QuestionCreate
) -> Any:
    question = crud.question.create(db=db, obj_in=question_in)
    return question


@router.put(
    "/{id}",
    response_model=schemas.Question,
)
def update_question(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    question_in: schemas.QuestionUpdate,
) -> Any:
    question = crud.question.get(db=db, id=id)
    if not question:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Question not found")
    question = crud.question.update(db=db, db_obj=question, obj_in=question_in)
    return question


@router.get(
    "/{id}",
    response_model=schemas.Question,
)
def read_question(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    question = crud.question.get(db=db, id=id)
    if not question:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Question not found")
    return question


@router.delete(
    "/{id}",
    response_model=schemas.Question,
)
def delete_question(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    question = crud.question.get(db=db, id=id)
    if not question:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Question not found")
    question = crud.question.remove(db=db, id=id)
    return question
