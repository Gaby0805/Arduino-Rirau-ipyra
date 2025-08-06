# app/models/users.py
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dataclasses import dataclass
from sqlalchemy import Integer, String
from app.core.database import Base


@dataclass
class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
