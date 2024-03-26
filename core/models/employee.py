import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime, String, Boolean
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
    department: Mapped[str] = mapped_column(
        String,
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
    email: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    phone: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )
