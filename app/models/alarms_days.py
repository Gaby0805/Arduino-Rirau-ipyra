from sqlalchemy import Column, Integer,  ForeignKey, SmallInteger, CheckConstraint
from sqlalchemy import DeclarativeBase, Mapped, mapped_column, Integer

from app.core.database import Base


class Alarms_days(Base):
    __tablename__ = 'alarms_days'


    id: Mapped[int]  = mapped_column(Integer, primary_key=True, index=True)
    alarm_id: Mapped[int]  = mapped_column(Integer, ForeignKey('alarms.id', ondelete='CASCADE'), nullable=False)
    day_of_week: Mapped[int]  = mapped_column(SmallInteger, nullable=False)

    __table_args__ = (
        CheckConstraint('day_of_week >= 0 AND day_of_week <= 6', name='check_day_of_week'),
    )