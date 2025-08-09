from app.repo.users import get_all_users
from app.core.database import SessionLocal 
from app.core.database import Base, engine



def test_repo_user_getall():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    user = get_all_users(db)
    print(user)
    db.close()
