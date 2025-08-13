from typing import List
from app.core.database import SessionLocal
from app.models.alarms_days import Alarms_days


class AlarmsDaysRepository:

    def create_alarm_day(self, alarm_id: int, day_of_week: int) -> Alarms_days:
        with SessionLocal() as db:
            alarm_day = Alarms_days(alarm_id=alarm_id, day_of_week=day_of_week)
            db.add(alarm_day)
            db.commit()
            db.refresh(alarm_day)
            return alarm_day

    def get_alarm_day_by_id(self, alarm_day_id: int) -> Alarms_days | None:
        with SessionLocal() as db:
            return db.query(Alarms_days).filter(Alarms_days.id == alarm_day_id).first()

    def get_all_alarm_days(self) -> List[Alarms_days]:
        with SessionLocal() as db:
            return db.query(Alarms_days).all()

    def get_alarm_days_by_alarm_id(self, alarm_id: int) -> List[Alarms_days]:
        with SessionLocal() as db:
            return db.query(Alarms_days).filter(Alarms_days.alarm_id == alarm_id).all()

    def delete_alarm_day(self, alarm_day: Alarms_days) -> None:
        with SessionLocal() as db:
            db.delete(alarm_day)
            db.commit()
