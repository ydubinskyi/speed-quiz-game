from fastapi import APIRouter

from quiz_game_api.api.endpoints import questions, answers

api_router = APIRouter()
api_router.include_router(questions.router, prefix="/questions", tags=["questions"])
api_router.include_router(answers.router, prefix="/answers", tags=["answers"])
