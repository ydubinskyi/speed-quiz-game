from fastapi import APIRouter

from app.api.endpoints import questions, answers

api_router = APIRouter()
api_router.include_router(questions.router, prefix="/questions", tags=["questions"])
api_router.include_router(answers.router, prefix="/questions/{question_id}/answers", tags=["answers"])
