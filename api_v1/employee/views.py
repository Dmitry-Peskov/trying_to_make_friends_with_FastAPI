from fastapi import APIRouter


employee_router = APIRouter(prefix="/employee", tags=["Сотрудник"])


@employee_router.get("/")
def index():
    return {"status": 200, "message": "Test"}
