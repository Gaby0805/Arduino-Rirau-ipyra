# app/repositories/user_repository.py
from sqlalchemy.orm import Session
from app.models.users import Users
class UserRepository:

    def create_user(self, name: str, password: str) -> Users:
        with Session() as db:
            user = Users(name=name,password=password)
            db.add(user)
            db.commit()
            db.refresh(user)
            return user

    def get_user_by_id(self, user_id: int) -> Users | None:
        with Session() as db:
            return db.query(Users).filter(Users.id == user_id).first()

    def get_all_users(self) -> list[Users]:
        with Session() as db:
            return db.query(Users).all()

    def delete_user(self, user: Users) -> None:
        with Session() as db:
                db.delete(user)
                db.commit()

    def get_user_by_name(self, user_name: str) -> Users| None:
        with Session() as db:
            return db.query(Users).filter(Users.name == user_name).first()
