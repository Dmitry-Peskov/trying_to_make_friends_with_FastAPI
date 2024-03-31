import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime, String

from .base import BaseModel


class Employee(BaseModel):
    fullname: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    happy_birthday: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        nullable=False
    )
    group: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    post: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
