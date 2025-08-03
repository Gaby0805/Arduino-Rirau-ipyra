from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Users(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    passaword = Column(String, index=True)