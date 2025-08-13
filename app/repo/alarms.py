from datetime import time as tm
from app.core.database import SessionLocal
from app.models.alarms import Alarms


class AlarmsRepository:

    def create_alarm(self, label: str, time: tm, user_id: int, is_active: bool = True) -> Alarms:
        with SessionLocal() as db:
            alarm = Alarms(label=label, time=time,user_id=user_id, is_active=is_active)
            db.add(alarm)
            db.commit()
            db.refresh(alarm)
            return alarm

    def get_alarm_by_id(self, alarm_id: int) -> Alarms | None:
        with SessionLocal() as db:
            return db.query(Alarms).filter(Alarms.id == alarm_id).first()

    def get_all_alarms(self) -> list[Alarms]:
        with SessionLocal() as db:
            return db.query(Alarms).all()

    def delete_alarm(self, alarm: Alarms) -> None:
        with SessionLocal() as db:
            db.delete(alarm)
            db.commit()

    def get_alarm_by_label(self, label: str) -> Alarms | None:
        with SessionLocal() as db:
            return db.query(Alarms).filter(Alarms.label == label).first()
