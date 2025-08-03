from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASEURL =  "sqlite:///./arduino-rirau-ipyra.db"


engine = create_engine(DATABASEURL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()