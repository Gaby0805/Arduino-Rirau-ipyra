from pydantic import BaseModel
from datetime import time as tm


class AlarmCreate(BaseModel):
    label: str
    time: tm
    is_active: bool = True


class AlarmResponse(AlarmCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True
