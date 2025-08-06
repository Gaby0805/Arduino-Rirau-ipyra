from app.repo.users import create_user
from app.core.database import SessionLocal 



def test_repo_user_create():
    db = SessionLocal()
    user = create_user(db, "yte", "te")
    assert user.name is not "yte"
    print(user.name)
    db.close()
