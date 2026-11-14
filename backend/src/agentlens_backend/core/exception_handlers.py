"""
It will convert our custom Python exceptions into appropriate HTTP responses.
"""
from starlette.responses import JSONResponse
from fastapi import Request
from agentlens_backend.core.exceptions import DatasetNotFoundError

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