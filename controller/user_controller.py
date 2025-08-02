from model.entity.user import User
from model.repository.user_repository import UserRepository

class UserController:

    def save(self, user_id, first_name, last_name, username, password, role, locked):
        try:
            user = User(user_id, first_name, last_name, username, password, role, locked)
            user_repo = UserRepository()
            user_repo.save(user)
            return True, f"user saved successfully {user}"
        except Exception as e:
            return False, f"error saving user : {e}"

    def edit(self, user_id, first_name, last_name, username, password, role, locked):
        try:
            user = User(user_id, first_name, last_name, username, password, role, locked)
            user_repo = UserRepository()
            user_repo.edit(user)
            return True, f"user edited successfully {user}"
        except Exception as e:
            return False, f"error editing user : {e}"

    def delete(self,user_id):
        try:
            user_repo = UserRepository()
            user_repo.delete(user_id)
            return True, f"user removed successfully {user_id}"
        except Exception as e:
            return False, f"error removing user : {e}"

    def find_all(self):
        try:
            user_repo = UserRepository()
            return True, user_repo.find_all()
        except Exception as e:
            return False, f"error find all users : {e}"

    def find_by_user_id(self,user_id):
        try:
            user_repo = UserRepository()
            user=user_repo.find_by_user_id(user_id)
            if user is None:
                return True, []
            else:
                return True, [user]
        except Exception as e:
            return False, f"error find user_id : {user_id} error : {e}"

    def find_by_first_name_last_name(self,first_name,last_name):
        try:
            user_repo = UserRepository()
            return True, user_repo.find_by_first_name_last_name(first_name,last_name)
        except Exception as e:
            return False, f"error find first_name : {first_name} last_name : {last_name} error : {e}"

    def find_by_username(self, username):
        try:
            user_repo = UserRepository()
            user = user_repo.find_by_username(username)
            if user is None:
                return True, []
            else:
                return True, [user]
        except Exception as e:
            return False, f"error find username : {username} error : {e}"

    def find_by_username_password(self,username,password):
        try:
            user_repo = UserRepository()
            return True, user_repo.find_by_username_password(username,password)
        except Exception as e:
            return False, f"error find username: {username} password: {password} error : {e}"

