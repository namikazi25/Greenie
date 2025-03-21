from loguru import logger
from fastapi import HTTPException
from typing import Dict, Any, Optional, Callable
import traceback
import functools

# Custom exception for application errors
class AppError(Exception):
    """Custom exception for application errors."""
    def __init__(self, message: str, status_code: int = 500, details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)

# Function to handle exceptions in routes
def handle_exceptions(func: Callable) -> Callable:
    """Decorator to handle exceptions in routes."""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except AppError as e:
            logger.error(f"Application error: {e.message}")
            raise HTTPException(status_code=e.status_code, detail={
                "message": e.message,
                "details": e.details
            })
        except HTTPException:
            # Re-raise FastAPI HTTP exceptions
            raise
        except Exception as e:
            # Log unexpected exceptions
            error_detail = traceback.format_exc()
            logger.error(f"Unexpected error: {str(e)}\n{error_detail}")
            raise HTTPException(status_code=500, detail={
                "message": "An unexpected error occurred",
                "error": str(e)
            })
    return wrapper

# Function to format error responses
def format_error_response(message: str, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Format error response."""
    return {
        "error": True,
        "message": message,
        "details": details or {}
    }

# Function to validate request data
def validate_request_data(data: Dict[str, Any], required_fields: list) -> None:
    """Validate request data."""
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise AppError(
            message=f"Missing required fields: {', '.join(missing_fields)}",
            status_code=400,
            details={"missing_fields": missing_fields}
        )