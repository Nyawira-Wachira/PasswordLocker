class User:
    """
    Class that generates new instances of a user.

    """
    user_list = []

    def __init__(self, username, password):
        """
        method that defines login details of a user.
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        method that saves a new user instance into the user list
        """
        User.user_list.append(self)
    

    @classmethod
    def display_user(cls):
        """
        method that displays saved accounts of user
        """
        return cls.user_list

    def delete_user(self):
        '''
        method that deletes a  saved account from the list
        '''
        User.user_list.remove(self)
