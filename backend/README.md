# quiz-game-api

## Requirements

- pyenv
- poetry
- Docker

## Quick start

Install deps

```
poetry shell
poetry install
```

Start docker container with Postgres and PGAdmin

```
docker-compose up -d
```

Create empty DB using PGAdmin

Create `.env` file using `.env.example` and populate with DB config

Run migrations

```
alembic upgrade head
```

Start application

```
uvicorn quiz_game_api.main:app --reload
```

Navigate to http://localhost:8000/docs
