# Functions
camp = 'Level Up'
from email.utils import *
import time


# #Defining the Functions

def greet_user():
    """Greets the user."""
    print('Welcome to Class!')
    print('this was basic function')


def greet_user_1(name):
    """Greeting the user with given name"""
    print(f'welcome to {name}')


def greet_user_2(company, username):
    """Greeting the user with given name"""
    print(f'{username.title()}, Welcome to {company.upper()} !')
    print('Have a Great Week')


def greet_user_3(username, company='Google'):
    """Greeting the user with given name and keyword argument 'company' """
    print(f'{username.title()}, Welcome to {company.upper()} !')
    print('Have a Great Week')


def greet_user_4(username, company= None):
    """Greeting the user with given name and keyword argument 'company' """
    if company is None:
        print(f'{username.title()}, Welcome to new Home !')
    else:
        print(f'{username.title()}, Welcome to {company.upper()} !')
    print('Have a Great Week')





# print(EXECUTION OF FUNCTIONS)

# greet_user()
#
# time.sleep(3)
# greet_user_1(camp)
# greet_user_1('Jungle')
# # print('Print Statement')
#
# greet_user_1(input('Enter company name: '))

greet_user_2('Wonderful Inc.', 'Serge')

greet_user_3('Serge')

greet_user_4('John', 'Statford')

# Package - __init__.py
# Module - .py file (python file)
