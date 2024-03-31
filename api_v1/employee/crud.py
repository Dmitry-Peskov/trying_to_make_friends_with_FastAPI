from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from core.models import Employee
from .schemas import EmployeeCreate


async def get_employees(session: AsyncSession) -> list[Employee]:
    stmt = select(Employee).order_by(Employee.created_at)
    result: Result = await session.execute(stmt)
    employees = result.scalars().all()
    return list(employees)


async def get_employee_by_id(session: AsyncSession, id: int) -> Employee | None:
    return await session.get(Employee, id)


async def create_employee(session: AsyncSession, employee: EmployeeCreate) -> Employee:
    employee_add = Employee(**employee.model_dump())
    session.add(employee_add)
    await session.commit()
    await session.refresh(employee_add)
    return employee_add
