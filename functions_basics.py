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


def full_name(first, last):
    return f'{first.title()} {last.title()}'



def adding(a, b):
    return a + b

def full_name_dict(first, last):
    """Returns full name"""
    result = {'first_name': first.title(), 'last_name': last.title()}
    return result

total = adding(456, 987)
print(f'Total is : {adding(456, 765)}')
print(f'Total is : {total}')

student_1 = full_name_dict('tatyana', "shark")

print(student_1['first_name'])

# full_name('anvar', 'nasirov')
# name = full_name('john', 'doe')
# # removed_value = list.pop()
#
# print(f'{name}, Welcome to the Class!')


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def get_formatted_name(first_name, middle_name, last_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = first_name + " " + middle_name + ' ' + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age= 27)
print(musician)


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()

# This is infinite loop
# while True:
#     print('\nPlease tell me your name:')
#     print('(enter "q" at anytime to quit)')
#     f_name = input('First name: ')
#     if f_name == 'q':
#         break
#     l_name = input('Last name: ')
#     if l_name == 'q':
#         break
#
#     formatted_name= get_formatted_name(f_name, l_name)
#     print('\nHello, ' + formatted_name + '!')


def city_country (city, country):
    both = city + ', ' + country
    return both.title()

group = city_country('santiago', 'chile')
print('"'+ group + '"')

def make_album(artist_name, album_title, n_tracks=''):
    album = {'Artist': artist_name, 'Album': album_title}
    if n_tracks:
        album['n_tracks']= n_tracks
    return album


artist = make_album('jimi hendrix', 'bizarre', 13)
print(artist)
artist = make_album('papa roach', 'god send')
print(artist)


def make_album(artist_name, album_title, n_tracks=''):
    album = {'Artist': artist_name, 'Album': album_title}
    if n_tracks:
        album['n_tracks']= n_tracks
    return album
# while True:
#     print('\nPlease provide artist and album names: ')
#     print("Enter 'Q' to quit")
#     a_name = input("artist name: ")
#     if a_name == 'q':
#         break
#     a_title = input('album title: ')
#     if a_title == 'q':
#         break
#     making_album = make_album(a_name, a_title)
#     print(making_album)
#


def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = "Hello, " + name.title() + '!'
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# while unprinted_designs:
#     current_designs = unprinted_designs.pop()
#     print('Printing model: ' + current_designs)
#     completed_models.append(current_designs)
#
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models= []

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_designs = unprinted_designs.pop()


def show_completed_models(completed_models):
    print('\nThe following models have been printed')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models= []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

nums = [5, 55, 76, 1, -9, 0, 1, 456]

def find_num(num_list, number):
    for num in num_list:
        if num == number:
            print(f"{number} is found !")
            break


find_num(nums, 1)


# def desc_pizza(*toppings):
#     print("We only have cheese pizza with the following toppings: ")
#     print(toppings)
#
# desc_pizza('peperoni')
# desc_pizza('chicken', 'peperoni', 'bbq chicken')
#
# def desc_pizza(*toppings):
#     print("We only have cheese pizza with the following toppings: ")
#     for topping in toppings:
#          print("_ " + toppings)
#
# desc_pizza('peperoni')
# desc_pizza('chicken', 'peperoni', 'bbq chicken')


def make_pizza(*toppings):
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('_ '+topping)

make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(size, *toppings):
    print('\nMaking a ' + str(size) + '- inch pizza with the following toppings:')
    for topping in toppings:
        print('_ '+topping)


make_pizza(16, 'peperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    """Build a dictionary containing evrything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile[ 'last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')

print(user_profile)

def build_sandwich (*toppings):
    print('Making a sandwich with the following toppings:')
    for topping in toppings:
        print('-'+topping)

build_sandwich('lettuce','corn beef')
build_sandwich('tomato','ham', 'cheese', 'turkey', 'mayo')


def make_car(make, model, **car_package):
    package = {}
    package ['car_make']= make
    package ['car_model'] = model
    for key, value in car_package.items():
        package[key] = value
    return package


car_info= make_car('infinity', 'QX60', color = 'black', tow_package = True)

print(car_info)


