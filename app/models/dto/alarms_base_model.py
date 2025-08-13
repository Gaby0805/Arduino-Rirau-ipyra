from pydantic import BaseModel, conlist, field_validator
from datetime import time as tm
from typing import List
class AlarmCreate(BaseModel):
    label: str
    time: tm
    days: conlist(int, min_length=1, max_length=7)  # lista de inteiros com no mínimo 1 item
    is_active: bool = True

    @field_validator("days")
    def validate_days_rangle(cls, v):
        if any(day < 0 or day > 6 for day in v):
            raise ValueError("Cada dia deve estar entre 0 (domingo) e 6 (sábado).")
        return v 

class AlarmResponse(AlarmCreate):
    id: int
    user_id: int
    class Config:
        orm_mode = True
