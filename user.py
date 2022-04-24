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
        method that saves a new user instance into the user list
        """
        User.user_list.append(self)
    
    