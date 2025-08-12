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

    def get_user_by_id(self,db: Session, user_id: int) -> Users | None:
        with Session() as db:
            return db.query(Users).filter(Users.id == user_id).first()

    def get_all_users(self,db: Session) -> list[Users]:
        return db.query(Users).all()

    def delete_user(self,db: Session, user_id: int) -> bool:
        with Session() as db:
            user = self.get_user_by_id(db, user_id)
            if user:
                db.delete(user)
                db.commit()
                return True
            return False

    def get_user_by_name(self,db: Session, user_name: str) -> Users| None:
        with Session() as db:
            return db.query(Users).filter(Users.name == user_name).first()
