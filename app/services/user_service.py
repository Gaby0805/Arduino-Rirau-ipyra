from app.repo.users import UserRepository,Users
from app.exceptions.user_already_exists_exception import UserAlreadyExistsException
from app.exceptions.user_not_found_exception import UserNotFoundException
class UserService:
    def __init__(self):
        self.repository = UserRepository()
    def create_user(self, name: str, password: str) -> Users:
        if self.repository.get_user_by_name(name):
            raise UserAlreadyExistsException()
        
        return self.repository.create_user(name, password)
    
    def get_user_by_id(self, user_id: int) -> Users:
        user = self.repository.get_user_by_id(user_id)
        if user is None:
            raise UserNotFoundException()
        return user
    
    def get_all_users(self) -> list[Users]:
        return self.repository.get_all_users()
    
    
    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        self.repository.delete_user(user)
    
    def get_user_by_name(self, user_name: str) -> Users:
        user = self.repository.get_user_by_name(user_name)
        if user is None:
            raise UserNotFoundException()
        return user