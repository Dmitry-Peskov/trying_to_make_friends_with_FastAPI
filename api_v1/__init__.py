__all__ = [
    "api_v1_router"
]

from fastapi import APIRouter
from .employee import employee_router
api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(employee_router)
