class User:
    """
    Class that generates new instances of a user.

    """
    user_list = []

    def __init__(self, username, password):
        """
        __init__ method that defines login details of a user.
        """
        self.username = username
        self.password = password

    