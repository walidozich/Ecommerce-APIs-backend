.PHONY: run test lint fmt migrate alembic-init

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest

lint:
	ruff check .

fmt:
	black .

migrate:
	alembic revision --autogenerate -m "update"
	alembic upgrade head

alembic-init:
	alembic init alembic
