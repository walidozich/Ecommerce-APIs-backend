"""FastAPI application entrypoint."""

from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(title="E-Commerce API", version="0.1.0")

app.include_router(api_router)


@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
