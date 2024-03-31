from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import database
from core.models import Employee
from . import crud
from .dependencies import employee_by_id
from .schemas import EmployeeGet, EmployeeCreate, EmployeeUpdate

employee_router = APIRouter(prefix="/employee", tags=["Сотрудник"])


@employee_router.get("/", response_model=list[EmployeeGet], summary="Получить всех «Сотрудников»")
async def get_employees(
        session: AsyncSession = Depends(database.session_dependency)
):
    return await crud.get_employees(session=session)


@employee_router.post("/", response_model=EmployeeGet, status_code=status.HTTP_201_CREATED, summary="Создать нового «Сотрудника»")
async def create_employees(
        employee: EmployeeCreate,
        session: AsyncSession = Depends(database.session_dependency)
):
    return await crud.create_employee(session=session, employee=employee)


@employee_router.get("/{employee_id}/", response_model=EmployeeGet, summary="Получить «Сотрудника» по его ID")
async def get_employee_by_id(
        employee: Employee = Depends(employee_by_id)
):
    return employee


@employee_router.patch("/{employee_id}/", response_model=EmployeeGet)
async def update_product(
        employee_update: EmployeeUpdate,
        employee_current: Employee = Depends(employee_by_id),
        session: AsyncSession = Depends(database.session_dependency)
):
    return await crud.update_employee(
        session=session,
        employee=employee_current,
        employee_upd=employee_update
    )


@employee_router.delete("/{employee_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee(
        employee: Employee = Depends(employee_by_id),
        session: AsyncSession = Depends(database.session_dependency)
) -> None:
    await crud.delete_employee(session=session, employee=employee)
