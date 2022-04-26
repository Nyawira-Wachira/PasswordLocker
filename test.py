import unittest
from user import User
from credentials import Credentials



class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('Nyawira','12AB$8zy')

    def test_init(self):
        """
        test case to check if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'Nyawira')
        self.assertEqual(self.new_user.password,'12AB$8zy')

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list

        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_display_all_users(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

    def test_delete_user (self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Nyash","qwAZXFgl") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)


class TestCredentials(unittest.TestCase):
    """
    test class that defines test cases for credentials class

    """ 
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.

        """
        self.new_credential = Credentials('Instagram','abigailnyawira','zy65h#QW')
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'Instagram')
        self.assertEqual(self.new_credential.userName,'abigailnyawira')
        self.assertEqual(self.new_credential.password,'zy65h#QW')

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []


    def test_save_credential(self):
        """
        test case to test if the crential object is saved into the credentials list.

        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_credentials()
        test_credential = Credentials("Facebook","Abigail_Nyash","VYk%89yt")
        test_credential.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_display_all_saved_credentials(self):
        '''
        method that displays all the credentials saved in the credentials list.
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


    
    def test_find_credential(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_credentials()
        test_credential = Credentials("Facebook","Abigail_Nyash","VYk%89yt") 
        test_credential.save_credentials()

        the_credential = Credentials.find_credential("Facebook")

        self.assertEqual(the_credential.account,test_credential.account)


if __name__ == '__main__':
    unittest.main()
