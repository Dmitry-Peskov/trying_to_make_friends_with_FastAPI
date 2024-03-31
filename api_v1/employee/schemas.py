from typing import Literal
from pydantic import BaseModel, PastDate


Groups = Literal["УЦ", "ГКО", "ОФД", "ГУИ", "ЭДО"]
Posts = Literal["Аналитик", "Старший аналитик", "Ведущий аналитик", "Руководитель группы"]


class EmployeeCreate(BaseModel):
    fullname: str
    happy_birthday: PastDate
    group: Groups
    post: Posts
