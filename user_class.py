import pyperclip
class User:
    """
    Class User will create instances of user, which will allow us to manage who uses the app.
    This class holds two arguments, user_name & password.
    """

    list_of_users = []


    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password


    def save_new_user(self):
        User.list_of_users.append(self)


    def delete_user(self):
        User.list_of_users.remove(self)

    @classmethod
    def find_by_name(cls,user_name):
        for user in cls.list_of_users:
            if user.user_name == user_name:
                return user

    @classmethod
    def user_exist(cls,user_name):

        for user in cls.list_of_users:
            if user.user_name == user_name:
                    return True
        return False

    @classmethod
    def new_user(cls,user_name):
        for user in cls.list_of_users:
            if user.user_name == user_name:
                    return True
        return False

    @classmethod
    def display_users(cls):
         return cls.list_of_users

    @classmethod
    def valid_user(cls):
        return cls.list_of_users






    # @classmethod
    # def copy_passwords(cls,user_name):
    #     contact_found = User.find_by_name(user_name)
    #     pyperclip.copy(contact_found.password)
