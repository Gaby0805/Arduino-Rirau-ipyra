from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.repo.users import create_user
from app.core.database import SessionLocal



def test_repo_funcional():
    db = SessionLocal()
    user = create_user(db, "Gaby", "123")
    assert user.id is not None

    db.close()
