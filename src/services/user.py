from entities.user import User
from repositories.user_repository import user_repository
from util.util import encrypt_password, verify_password, get_timestamp
from dearpygui import core, simple


class UserServices:
    """Luokka"""

    def __init__(self):
        self._user_repo = user_repository
        self._user = None

    def get_all_users(self):
        return self._user_repo.get_all_users()

    def login(self, username, password):
        user = self._user_repo.get_user_by_usename(username)
        if user == None:
            return False
        else:
            #if verify_password(password, user.password):
            #    return True
            #else:
            #    return False
            pass

    def signup_user(self, username, email, password):
        hash_value = encrypt_password(password)
        created_on = get_timestamp()
        #does_username_exist = self._user_repo.get_user_by_usename(username)
        #if does_username_exist:
        #    core.log_debug("not exist")
        #    return False
        
        result = self._user_repo.add_new_user(User(username, email, password, created_on))
        return result

    def get_current_user(self):
        return self._user


user_services = UserServices()
