from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from quiz_game_api import crud, schemas
from quiz_game_api.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Answer])
def read_answers(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    answers = crud.answer.get_multi(db=db, skip=skip, limit=limit)
    return answers


@router.post(
    "/",
    response_model=schemas.Answer,
    status_code=HTTP_201_CREATED,
)
def create_answer(
    *, db: Session = Depends(deps.get_db), answer_in: schemas.AnswerCreate
) -> Any:
    answer = crud.answer.create(db=db, obj_in=answer_in)
    return answer


@router.put(
    "/{id}",
    response_model=schemas.Answer,
)
def update_answer(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    answer_in: schemas.AnswerUpdate,
) -> Any:
    answer = crud.answer.get(db=db, id=id)
    if not answer:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Answer not found")
    answer = crud.question.update(db=db, db_obj=answer, obj_in=answer_in)
    return answer


@router.get(
    "/{id}",
    response_model=schemas.Answer,
)
def read_answer(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    answer = crud.answer.get(db=db, id=id)
    if not answer:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Answer not found")
    return answer


@router.delete(
    "/{id}",
    response_model=schemas.Answer,
)
def delete_answer(*, db: Session = Depends(deps.get_db), id: UUID4) -> Any:
    answer = crud.answer.get(db=db, id=id)
    if not answer:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Answer not found")
    answer = crud.answer.remove(db=db, id=id)
    return answer
