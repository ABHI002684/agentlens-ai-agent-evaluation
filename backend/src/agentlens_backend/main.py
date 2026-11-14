from fastapi import FastAPI
from contextlib import asynccontextmanager
from agentlens_backend.core.config import get_settings
from agentlens_backend.core.logging import setup_logging
from agentlens_backend.core.exceptions import DatasetNotFoundError, EvaluationNotFoundError, EvaluationExecutionError
from agentlens_backend.core.exception_handlers import dataset_not_found_handler, evaluation_not_found_handler, evaluation_execution_error_handler
import logging

settings = get_settings()

setup_logging()

logger = logging.getLogger("agentlens")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("lifespan startup")

    yield

    logger.info("lifespan shutdown")

app = FastAPI(
    title=settings.APP_NAME,
    description="Backend API for the AgentLens agent evaluation platform.",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_exception_handler(
    DatasetNotFoundError,
    dataset_not_found_handler
)


app.add_exception_handler(
    EvaluationNotFoundError,
    evaluation_not_found_handler
)

app.add_exception_handler(
    EvaluationExecutionError,
    evaluation_execution_error_handler
)

@app.get("/test-exception")
async def test_exception():
    raise EvaluationExecutionError()


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to AgentLens API",
        "version": app.version,
    }