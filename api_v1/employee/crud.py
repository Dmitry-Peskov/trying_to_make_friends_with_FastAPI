from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from core.models import Employee
from .schemas import EmployeeCreate, EmployeeUpdatePartial, EmployeeUpdate


async def get_employees(session: AsyncSession) -> list[Employee]:
    stmt = select(Employee).order_by(Employee.created_at)
    result: Result = await session.execute(stmt)
    employees = result.scalars().all()
    return list(employees)


async def get_employee_by_id(session: AsyncSession, employee_id: int) -> Employee | None:
    stmt = select(Employee).where(Employee.id == employee_id)
    result: Result = await session.execute(stmt)
    employee: Employee | None = result.scalar_one_or_none()
    return employee


async def create_employee(session: AsyncSession, employee: EmployeeCreate) -> Employee:
    employee_add = Employee(**employee.model_dump())
    session.add(employee_add)
    await session.commit()
    await session.refresh(employee_add)
    return employee_add


async def update_employee(
        session: AsyncSession,
        employee: Employee,
        employee_upd: EmployeeUpdatePartial | EmployeeUpdate,
        partial: bool = False
):
    for name, value in employee_upd.model_dump(exclude_unset=partial, exclude_none=partial).items():
        setattr(employee, name, value)
    await session.commit()
    await session.refresh(employee)
    return employee


async def delete_employee(session: AsyncSession, employee: Employee) -> None:
    await session.delete(employee)
    await session.commit()
