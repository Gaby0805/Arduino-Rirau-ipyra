from fastapi import APIRouter, Depends, status
from typing import List
from datetime import time as tm

from app.models.alarms import Alarms
from app.models.dto.alarms_base_model import AlarmCreate, AlarmResponse
from app.services.alarm_service import AlarmsService
from app.models.dto.user_base_model import User
from app.api.routes.auth import get_current_user

router = APIRouter(prefix="/alarms", tags=["alarms"])

service = AlarmsService()


@router.post("/", response_model=AlarmResponse, status_code=status.HTTP_201_CREATED)
async def create_alarm(
    alarm: AlarmCreate,
    current_user: User = Depends(get_current_user),
):
    return service.create_alarm(alarm.label, alarm.time, current_user.name, alarm.is_active)


@router.get("/", response_model=List[AlarmResponse])
async def get_all_alarms(
    current_user: User = Depends(get_current_user),
):
    return service.get_all_alarms()


@router.get("/{alarm_id}", response_model=AlarmResponse)
async def get_alarm_by_id(
    alarm_id: int,
    current_user: User = Depends(get_current_user),
):
    return service.get_alarm_by_id(alarm_id)


@router.delete("/{alarm_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_alarm(
    alarm_id: int,
    current_user: User = Depends(get_current_user),
):
    service.delete_alarm(alarm_id)
