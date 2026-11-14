"""
It will convert our custom Python exceptions into appropriate HTTP responses.
"""
from starlette.responses import JSONResponse
from fastapi import Request
import logging
from agentlens_backend.core.exceptions import DatasetNotFoundError, EvaluationNotFoundError, EvaluationExecutionError

logger = logging.getLogger("agentlens")


async def dataset_not_found_handler(request: Request, exc: DatasetNotFoundError): # exc - exception
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "error":{
                "code": "DATASET_NOT_FOUND",
                "message": "Dataset not found"
            }
        }
    )

async def evaluation_not_found_handler(request: Request, exc: EvaluationNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "error":{
                "code": "EVALUATION_NOT_FOUND",
                "message": "Evaluation not found"
            }
        }
    )

async def evaluation_execution_error_handler(request: Request, exc: EvaluationExecutionError):
    logger.error(
        "Evaluation execution failed",
        exc_info=(type(exc), exc, exc.__traceback__)
    )
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error":{
                "code": "EVALUATION_EXECUTION_FAILED",
                "message": "Evaluation execution failed"
            }
        }
    )