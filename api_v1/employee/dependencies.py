from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core import database
from core.models import Employee
from . import crud


async def employee_by_id(
        employee_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.session_dependency)
) -> Employee:
    employee_get = await crud.get_employee_by_id(session=session, id=employee_id)
    if employee_get is not None:
        return employee_get
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Пользователь с id = {employee_id} не найдет в системе"
    )
