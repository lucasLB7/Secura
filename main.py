#!/usr/bin/env python3.6
from user_class import User
from credentials_class import Credentials
import time, csv, sys, pyperclip, random, string


def create_user(u_name,p_word):
    """
    Creates a new user instance with two arguments:
    u_name (User name)
    p_word (password)
    """

    new_user = User(u_name,p_word)
    print("-"*50)
    print("Hi there ",new_user.user_name)
    print("Your account has been created..\nRemember to save your details\n")
    print("User name: ",new_user.user_name)
    print("Your password: ",new_user.password)
    print("-"*50)
    print("Key in: li : To log into your new account..")
    return new_user

def save_user(User):
    '''
    Function to save contact
    '''
    User.save_new_user()

def create_credentials(website , user_name_cr , password_cr):
    new_creds= Credentials(website , user_name_cr , password_cr)
    print("Your details has been stored.\nRemember to save your details\n")
    print("website: ",new_creds.website)
    print("Your password: ",new_creds.password_cr)
    print("Your user name: ",new_creds.user_name_cr)

    return new_creds


def save_credentials(Credentials):
    Credentials.save_credentials()


def display_users():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()


def display_credentials():
    return Credentials.view_credentials()

def valid_user():
    return User.valid_user()


def password_generator(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))







def user_validation():
    if valid_user():
        print("enter your unsername: ")
        user_n = input()
        print("enter your password: ")
        pass_w = input()
        pass_list = [user_n,pass_w]
        for user in valid_user():
            stored_list = [user.user_name,user.password]
            if stored_list == pass_list:
                print(stored_list)
                print(pass_list)
                password_manager()
            print(stored_list)
            print(pass_list)





def main_run():
    print("Welcome to SECURA")
    time.sleep(1)
    print("Checking if your are a new user..")
    time.sleep(1)
    if display_users():
        user_validation()
    print("New user..")
    print("\n Press cc to create your account.")
    pass

    while True:
        print("Use these short codes : ")
        print("-"*50)
        print("cc - create a secure user account,\n dc - display contacts,\n li - log in")
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

        elif short_code == "li":
            user_validation()



def password_manager():
    for user in valid_user():
        print("Succesfully logged in, welcome to the password manager",user.user_name)
        while True:
            print(" \n Use the following short codes: ")
            print("-"*50)
            print("np - Create a new password,\n sp - Search passwords by website,\n vp - view passwords,\n dp - Delete password")
            short_code = input().lower()

            if short_code == 'np':
                print('Please enter the website')
                website = input()
                print("PLease enter the user name for the account")
                user_name_cr = input()
                print("Master passsword will be auto generated")
                time.sleep(0.5)
                password_cr = password_generator()
                print("."*50)
                print(password_cr)

                time.sleep(2)
                save_credentials(create_credentials(website,user_name_cr,password_cr))

            elif short_code == 'vp':
                print("View your passwords")
                time.sleep(2)
                for creds in display_credentials():
                    print('website: ' f"{creds.website}")
                    print('Username: ' f"{creds.user_name_cr}")
                    print('Password: ' f"{creds.password_cr}")






                    # with open('credentials.csv', 'a', newline='') as csvfile:
                    #     spamwriter = csv.writer(csvfile, delimiter=' ',
                    #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    #
                    #     # spamwriter.writerow(fieldnames)
                    #     # spamwriter.writerow(user_data[0])
                    #     # spamwriter.writerow("Username: "+user_data[1])
                    #     # spamwriter.writerow("Password: "+user_data[2])
                    #     # spamwriter.writerow("-"*20)
                    #     spamwriter.writerow({fieldnames[0]: name, fieldnames[1]: user_data[1],fieldnames[2]:user_data[1]})
                    #
                    #     print("Your files have been recorded..")
                    #     print("Your username: "+username+"\nYour name: "+name+"\nYour password: "+password))










main_run()
