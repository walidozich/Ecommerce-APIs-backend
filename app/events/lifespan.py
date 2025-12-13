"""Lifespan event placeholders."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.logging import configure_logging


@asynccontextmanager
def lifespan(_: FastAPI):
    configure_logging()
    yield
