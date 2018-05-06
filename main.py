#!/usr/bin/env python3.6
from user_class import User

def create_user(u_name,p_word):
    """
    Creates a new user instance with two arguments:
    u_name (User name)
    p_word (password)
    """

    new_user = User(u_name,p_word)
    print("Hi there ",new_user.user_name)
    print("Your account has been created..\nRemember to save your details")
    print("User name: ",new_user.user_name)
    print("Your password: ",new_user.password)
    return new_user

def save_user(User):
    '''
    Function to save contact
    '''
    User.save_new_user()


def display_users():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()

def user_validation():
    print("enter your unsername: ")
    user_n = input()
    print("enter your password: ")
    pass_w = input()
    if User.valid_user(user_n,pass_w):
        print("ok")
    print("not okay")


# def del_user(contact):
#     '''
#     Function to delete a contact
#     '''
#     contact.delete_user()
#
# def find_contact(number):
#     '''
#     Function that finds a contact by number and returns the contact
#     '''
#     return Contact.find_by_name(number)
#
# def check_existing_contacts(number):
#     '''
#     Function that check if a contact exists with that number and return a Boolean
#     '''
#     return Contact.user_exist(number)
#


def main_run ():
    print("Welcome to SECURA")
    user_validation()
    while True:
        print("Use these short codes : cc - create a secure user account,\n dc - display contacts, fc -find a contact, ex -exit the contact list ")
        short_code = input().lower()

        if short_code == "cc":
            print("Enter your NEW username..")
            u_name = input()
            print("Enter your NEW password..")
            p_word = input()
            print("Enter the password again..")
            p_word2 = input()
            if u_name == "":
                print("Cannot leave a blank username.. ")
                return main_run()
            elif p_word == "":
                print("Cannot leave a blank password.. ")
                return main_run()
            else:
                if p_word != p_word2:
                    print("Passwords must match..")
                    return main_run()
                save_user(create_user(u_name,p_word))



        elif short_code == 'dc':
            if display_users():
                print("Here is a list of all your contacts")
                print('\n')
                for user in display_users():
                    print(f"{user.user_name}")
                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any contacts saved yet")
                print('\n')



main_run()
