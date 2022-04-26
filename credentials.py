from user import User 
import random
import string


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
    def __init__(self,account,userName, password):
        """
        __init__ method that defines properties of user credentials object.
        """
        self.account = account
        self.userName = userName
        self.password = password
    def save_credentials(self):
        """
        method to save new user account credentials to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        method to delete user account credentials from the credentials list
        """
        Credentials.credentials_list.remove(self)
    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list

        """
        return cls.credentials_list

     
    @classmethod
    def find_credential(cls, account):
        """
        Method that returns credentials matching keyed in account_name.

        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential


    def generatePassword(stringLength=8):
        """
        method to generate a random password
        
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))

    