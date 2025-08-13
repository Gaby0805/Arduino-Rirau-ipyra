from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Time, Boolean, ForeignKey
from dataclasses import dataclass
from app.core.database import Base
from datetime import time as tm


@dataclass
class Alarms(Base):
    __tablename__ = 'alarms'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True )
    label: Mapped[str] = mapped_column(String, index=True)
    time: Mapped[tm] = mapped_column(Time, index=True)
    user_id: Mapped[int]  = mapped_column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
