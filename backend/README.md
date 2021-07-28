# quiz-game-api

## Requirements

- pyenv
- poetry
- Docker

## Quick start

Install deps

```bash
poetry shell
poetry install
```

Start docker container with Postgres and PGAdmin

```bash
docker-compose up -d
```

Create empty DB using PGAdmin

Create `.env` file using `.env.example` and populate with DB config

Run migrations

```bash
alembic upgrade head
```

Start application

```bash
uvicorn quiz_game_api.main:app --reload
```

Navigate to http://localhost:8000/docs
