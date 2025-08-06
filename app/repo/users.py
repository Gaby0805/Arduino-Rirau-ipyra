# app/repositories/user_repository.py
from sqlalchemy.orm import Session
from app.models.users import Users

def create_user(db: Session, name: str, password: str) -> Users:

    user = Users(name=name,password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: int) -> Users | None:
    return db.query(Users).filter(Users.id == user_id).first()

def get_all_users(db: Session) -> list[Users]:
    return db.query(Users).all()

def delete_user(db: Session, user_id: int) -> bool:
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
