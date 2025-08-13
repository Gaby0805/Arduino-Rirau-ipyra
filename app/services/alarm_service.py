from datetime import time as tm
from typing import List
from app.models.alarms import Alarms
from app.repo.alarms import AlarmsRepository
from app.exceptions.alarm_not_found_exception import AlarmNotFoundException

from app.services.user_service import UserService
class AlarmsService:
    def __init__(self):
        self.repository = AlarmsRepository()
        self.user_service = UserService()

    def create_alarm(self, label: str, time: tm, user_name:str,is_active: bool = True) -> Alarms:
        user_id = self.user_service.get_user_by_name(user_name).id
        return self.repository.create_alarm(label, time,user_id, is_active)

    def get_alarm_by_id(self, alarm_id: int) -> Alarms:
        alarm = self.repository.get_alarm_by_id(alarm_id)
        if alarm is None:
            raise AlarmNotFoundException()
        return alarm

    def get_all_alarms(self) -> List[Alarms]:
        return self.repository.get_all_alarms()

    def delete_alarm(self, alarm_id: int) -> None:
        alarm = self.get_alarm_by_id(alarm_id)
        self.repository.delete_alarm(alarm)

    def get_alarm_by_label(self, label: str) -> Alarms:
        alarm = self.repository.get_alarm_by_label(label)
        if alarm is None:
            raise AlarmNotFoundException()
        return alarm
