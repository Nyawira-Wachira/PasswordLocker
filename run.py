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

