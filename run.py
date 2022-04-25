#!/usr/bin/env python3.8
from user import User
from credentials import Credentials

def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save new user
    '''
    user.save_user()
def display_users():
    """
    Function to display existing users
    """
    return User.display_user()
def login_user(username,password):
    """
    function that verifies user is in userlist and asks for login details.
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def delete_user(user):
     '''
     Function to delete a contact
     '''
     user.delete_user()

def create_new_credential(account,userName,password):
     """
     Function that creates new credentials for a given user account
     """
     new_credential = Credentials(account,userName,password)
     return new_credential
def save_credentials(credentials):
     """
     Function to save Credentials to the credentials list
     """
     credentials. save_credentials()
def display_accounts_details():
     """
     Function that returns credentials saved in the list.
     """
     return Credentials.display_credentials()

def delete_credential(credentials):
     """
     Function to delete a Credentials from credentials list

     """
     credentials.delete_credentials()
def find_credential(account):
     """
     Function that finds account credentials through account name
     """
     return Credentials.find_credential(account)

def generate_Password():
     '''
     generates a random password for the user.
     '''
     auto_password=Credentials.generatePassword()
     return auto_password


def main():
        print("Hi, what is your name?")
        user_name = input()
        print('.' * 50)
        print(f"Hello {user_name}, what would you like to do?")
        print('.' * 50)

        print("Use short codes :\n ca - To create Password Locker account,\n al -To login to existing account")

        short_code = input().lower()

        if short_code == 'ca':
                    print('\n') 
                    print("Sign Up")
                    print('.' * 10)
                    username = input("User_name: ")
                    password = input("Enter Password\n")
                    save_user(create_new_user(username,password))
                    print('\n')
                    print("*"*80)
                    print(f"Hello {username}, Your account has been created successfully! Your password is: {password}")
                    print("*"*80)

        elif short_code == "al":
                    print("*"*50)
                    print("Enter your User name and your Password to log in")
                    print('*' * 50)
                    username = input("User name: ")
                    password = input("password: ")
                    print('\n')

                    print('.' * 50)
                    print(f"Hello {username}, Welcome to your Password Locker.") 
                    print('.' * 50) 
                    print('\n')                        
        while True:
                    print("Use these short codes:\n cc - create new credentials \n dc - display credentials \n fc - find credential \n d - delete credential \n ex - Exit application")
                    short_code = input().lower().strip()
                    if short_code == "cc":
                        print("Create New Credential")
                        print("."*20)
                        print("Account name ....")
                        account = input().lower()
                        print("Your Account username")
                        userName = input()
                        while True:
                            print(" tp - type password for available account:\n gp - generate random password")
                            print('\n')
                            password_Choice = input().lower().strip()
                            if password_Choice == 'tp':
                                print('\n')
                                password = input("Enter your own password\n")
                                break
                            elif password_Choice == 'gp':
                                password = generate_Password()
                                break
                            else:
                                print("Invalid password please try again")
                                
                        save_credentials(create_new_credential(account,userName,password))
                        print('\n')
                        print('.'* 90)
                        print(f"Credentials for: {account} account - UserName: {userName} - Password:{password} created succesfully")
                        print('.'* 90)
                        print('\n')
                    elif short_code == "dc":
                        if display_accounts_details():
                            print("Here's your list of account credentials: ")
                            
                            print('*' * 30)
                            print('_'* 30)
                            for account in display_accounts_details():
                                print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                                print('_'* 30)
                                print('*' * 30)
                        else:
                            print("You don't have any credentials saved yet")
                          
                    elif short_code == "fc":
                        print("Enter the account name you want to search for")
                        search_name = input().lower()
                        if find_credential(search_name):
                            search_credential = find_credential(search_name)
                            print(f"Account Name : {search_credential.account}")
                            print('-' * 50)
                            print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                            print('-' * 50)
                        else:
                            print("That Credential does not exist")
                            print('\n')
                    elif short_code == "d":
                        print("Enter account name of the Credentials you want to delete")
                        search_name = input().lower()
                        if find_credential(search_name):
                            search_credential = find_credential(search_name)
                            print("_"*50)
                            search_credential.delete_credentials()
                            print('\n')
                            print(f"Credentials for {search_credential.account} successfully deleted")
                            print('\n')
                        else:
                            print("Credential doesn't exist.")

                    elif short_code == 'gp':

                        password = generate_Password()
                        print(f" {password} has been generated succesfully.")

                    elif short_code == 'ex':
                        print("Bye... Thanks for using Password Locker!")
                        break
                    
                    else:
                        print("Wrong entry! Please use the short codes")
              
if __name__ == '__main__':
    main()         
                                        

                            

                                
                                            
                                