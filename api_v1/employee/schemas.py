from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, PastDate


Groups = Literal["УЦ", "ГКО", "ОФД", "ГУИ", "ЭДО"]
Posts = Literal["Аналитик", "Старший аналитик", "Ведущий аналитик", "Руководитель группы"]


class EmployeeCreate(BaseModel):
    fullname: str
    happy_birthday: PastDate
    group: Groups
    post: Posts


class EmployeeGet(EmployeeCreate):
    id: int
    created_at: datetime
    updated_at: datetime


class EmployeeUpdate(EmployeeCreate):
    pass


class EmployeeUpdatePartial(BaseModel):
    fullname: Optional[str] = None
    happy_birthday: Optional[PastDate] = None
    group: Optional[Groups] = None
    post: Optional[Posts] = None
