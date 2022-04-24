class User:
    """
    Class that generates new instances of a user.

    """
    user_list = []

    def __init__(self, username, password):
        """
        __init__ method that defines properties of user login object.
        """
        self.username = username
        self.password = password
    def save_user(self):
        """
        method to save new user instance into the user list
        """
        User.user_list.append(self)
    @classmethod
    def display_user(cls):
        """
        method to display list of users.
        """
        return cls.user_list
    def delete_user(self):
        '''
        method to delete saved account from list of users.
        '''
        User.user_list.remove(self)

    