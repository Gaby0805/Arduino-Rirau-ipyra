from pydantic import BaseModel


class AlarmDayCreate(BaseModel):
    alarm_id: int
    day_of_week: int


class AlarmDayResponse(AlarmDayCreate):
    id: int

    class Config:
        orm_mode = True
