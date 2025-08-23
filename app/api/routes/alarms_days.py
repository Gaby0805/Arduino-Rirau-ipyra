from fastapi import APIRouter, Depends, status
from typing import List

from app.models.alarms_days import Alarms_days
from app.models.dto.alarms_days_base_model import AlarmDayCreate, AlarmDayResponse
from app.services.alarms_days_service import AlarmsDaysService
from app.models.dto.user_base_model import User
from app.api.routes.auth import get_current_user

router = APIRouter(prefix="/alarms-days", tags=["alarms_days"])

service = AlarmsDaysService()


@router.post("/", response_model=AlarmDayResponse, status_code=status.HTTP_201_CREATED)
async def create_alarm_day(
    alarm_day: AlarmDayCreate,
    current_user: User = Depends(get_current_user),
):
    return service.create_alarm_day(alarm_day.alarm_id, alarm_day.day_of_week)


@router.get("/", response_model=List[AlarmDayResponse])
async def get_all_alarm_days(
    current_user: User = Depends(get_current_user),
):
    return service.get_all_alarm_days()


@router.get("/{alarm_day_id}", response_model=AlarmDayResponse)
async def get_alarm_day_by_id(
    alarm_day_id: int,
    current_user: User = Depends(get_current_user),
):
    return service.get_alarm_day_by_id(alarm_day_id)


@router.get("/alarm/{alarm_id}", response_model=List[AlarmDayResponse])
async def get_alarm_days_by_alarm_id(
    alarm_id: int,
    current_user: User = Depends(get_current_user),
):
    return service.get_alarm_days_by_alarm_id(alarm_id)


@router.delete("/{alarm_day_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_alarm_day(
    alarm_day_id: int,
    current_user: User = Depends(get_current_user),
):
    service.delete_alarm_day(alarm_day_id)
