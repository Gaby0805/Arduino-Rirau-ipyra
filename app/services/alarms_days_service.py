from typing import List
from app.models.alarms_days import Alarms_days
from app.repo.alarms_days import AlarmsDaysRepository
from app.exceptions.alarm_day_not_found_exception import AlarmDayNotFoundException


class AlarmsDaysService:
    def __init__(self):
        self.repository = AlarmsDaysRepository()

    def create_alarm_day(self, alarm_id: int, day_of_week: int) -> Alarms_days:
        return self.repository.create_alarm_day(alarm_id, day_of_week)

    def get_alarm_day_by_id(self, alarm_day_id: int) -> Alarms_days:
        alarm_day = self.repository.get_alarm_day_by_id(alarm_day_id)
        if alarm_day is None:
            raise AlarmDayNotFoundException()
        return alarm_day

    def get_all_alarm_days(self) -> List[Alarms_days]:
        return self.repository.get_all_alarm_days()

    def get_alarm_days_by_alarm_id(self, alarm_id: int) -> List[Alarms_days]:
        return self.repository.get_alarm_days_by_alarm_id(alarm_id)

    def delete_alarm_day(self, alarm_day_id: int) -> None:
        alarm_day = self.get_alarm_day_by_id(alarm_day_id)
        self.repository.delete_alarm_day(alarm_day)
