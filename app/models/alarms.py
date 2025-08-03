from sqlalchemy import Column, Integer, String, Time, Boolean
from app.core.database import Base

class Alarms(Base):
    __tablename__ = 'alarms'

    id = Column(Integer, primary_key=True, index=True )
    label = Column(String, index=True)
    time = Column(Time, index=True)
    is_active = Column(Boolean, default=True, index=True)