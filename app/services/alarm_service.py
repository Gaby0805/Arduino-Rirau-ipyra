from datetime import time as tm
import logging
from typing import List
from app.models.alarms import Alarms
from app.repo.alarms import AlarmsRepository
from app.exceptions.alarm_not_found_exception import AlarmNotFoundException
from pydantic import conlist
from app.services.user_service import UserService
from app.services.alarms_days_service import AlarmsDaysService
from app import scheduler
from app.core.manager import websocket_manager 
class AlarmsService:
    def __init__(self):
        self.repository = AlarmsRepository()
        self.user_service = UserService()
        self.alarms_days_service = AlarmsDaysService()

    def create_alarm(self, label: str, time: tm,days:List[int], user_name:str, is_active: bool = True) -> dict:
        user_id = self.user_service.get_user_by_name(user_name).id
        alarm =  self.repository.create_alarm(label, time,user_id, is_active)
        #aqui nao é o melhor jeito de se fazer, o certo é escrever uma query personalizada
        for day in days:
            self.alarms_days_service.create_alarm_day(alarm.id, day)
        scheduler.load_alarms()
        return  {
        "id": alarm.id,
        "label": alarm.label,
        "time": alarm.time,
        "user_id": alarm.user_id,
        "is_active": alarm.is_active,
        "days": days  
    }
        

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
    
    async def trigger_alarm(self ):
        command = f"ALARME"

        logging.info(f" Enviando via WebSocket")
        await websocket_manager.send_to_arduino(command)
        self.last_command = command
        return {"status": "ok", "command": command}

    def get_command(self):
        cmd = self.last_command
        self.last_command = None
        return {"command": cmd}