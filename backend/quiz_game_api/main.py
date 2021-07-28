from fastapi import FastAPI

from quiz_game_api.api.api import api_router

app = FastAPI()
app.include_router(api_router)
