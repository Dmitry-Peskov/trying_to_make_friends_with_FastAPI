from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import database
from . import crud
from .schemas import EmployeeGet, EmployeeCreate

employee_router = APIRouter(prefix="/employee", tags=["Сотрудник"])


@employee_router.get("/", response_model=list[EmployeeGet], summary="Получить всех «Сотрудников»")
async def get_employees(
        session: AsyncSession = Depends(database.session_dependency)
):
    return await crud.get_employees(session=session)


@employee_router.post("/", response_model=EmployeeGet, summary="Создать нового «Сотрудника»")
async def create_employees(
        employee: EmployeeCreate,
        session: AsyncSession = Depends(database.session_dependency)
):
    return await crud.create_employee(session=session, employee=employee)


@employee_router.get("/{user_id}/", response_model=EmployeeGet, summary="Получить «Сотрудника» по его ID")
async def get_employee_by_id(
        employee_id: int,
        session: AsyncSession = Depends(database.session_dependency)
):
    employee_get = await crud.get_employee_by_id(session=session, id=employee_id)
    if employee_get is not None:
        return employee_get
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Пользователь с id = {employee_id} не найдет в системе"
    )
