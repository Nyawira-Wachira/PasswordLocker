from user import User 
import random
import string
import pyperclip

class Credentials():
    """
    Class that generates new instances of user credentials
    """
    credentials_list = []
    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify user in the list of users.
        """
        saved_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    saved_user == user.username
        return saved_user