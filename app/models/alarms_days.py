from sqlalchemy import Column, Integer, String, Time, ForeignKey, SmallInteger, CheckConstraint
from app.core.database import Base


class Alarms_days(Base):
    __tablename__ = 'alarms_days'


    id = Column(Integer, primary_key=True, index=True)
    alarm_id = Column(Integer, ForeignKey('alarms.id', ondelete='CASCADE'), nullable=False)
    day_of_week = Column(SmallInteger, nullable=False)

    __table_args__ = (
        CheckConstraint('day_of_week >= 0 AND day_of_week <= 6', name='check_day_of_week'),
    )