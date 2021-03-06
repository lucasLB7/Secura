# SECURA PROJECT #
## Pre-Alpha V 1.02 ##
========================

# INSTALLING & RUN APP #

To  run this app, make sure you have python 3 installed on your computer.
clone the app from the github repository into you computer with the command:
```git clone https://github.com/lucasLB7/Secura.git```
**Remember to do this in your the folder you want to clone into**

Once cloning is done, we are nearly there...
    - In the root directory of the app (**where you have the main.py**).
    - Run the following command in your command:
        ```python3 main.py```

    This will run the application locally on your machine..

# INTRODUCTION #

- The SECURA project is designed as an introductory python 3 project to classes and OOP.
- The SECURA application stores requires a login form a user in order to access and manage passwords.
- The SECURA application allows passwords to be stored, read and deleted via it's command based navigation

# INSTALLATION #

The SECURA application must be cloned from GitHub repo:
[SECURA REPOSITORY: LucasLB7](https://github.com/lucasLB7/Secura)

Once cloning is complete, run the main.py file in command using the prefix __python3.6__.

eg. 
    ```python3 main.py```


# WHAT YOU'LL SEE #

On running the program you will be greeted by a welcome sign and a __check to see if a user exists__.
-If a user does exist, you are taken to the login.
-If a user does not exist, you are prompted with a sign up prompt, to create a __user__.
As no databases are used for this, there will not be any user.

```
Welcome to SECURA
Checking if your are a new user..
New user..
Use these short codes :
cc - create a secure user account,
dc - display contacts,
li - log in,
vp -view passwords (logged in only)

Press cc to create your account.
```

__If you press cc__:
# You will be prompted to crease a new user #

```
Press cc to create your account.
cc
Enter your NEW username..
lucas
Enter your NEW password..
freshCandlellamas
Enter the password again..
freshCandlellamas
Hi there  lucas
Your account has been created..
Remember to save your details

User name:  lucas
Your password:  freshCandlellamas
```

__If you enter a blank username/password or your passwords didn't match__, you will receive a message and go back to the start.

```
Press cc to create your account.
cc
Enter your NEW username..
lucas
Enter your NEW password..

Enter the password again..

Cannot leave a blank password..
Welcome to SECURA
Checking if your are a new user..
```

## I a correct set of credentials is entered:

You can now log in to the application 

## Saving and checking your website credentials

Press vp after creating a new credentials object to view the details.
The password is generated automatically and is stored for you.

To **view the saved credentials**, enter **vc** to display all created credentials.




## CREDITS

- Moringa LMS
- Stackoverflow
- Python documentation
