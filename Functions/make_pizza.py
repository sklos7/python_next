import pizza

pizza.make_pizza(16, 'peperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza as mp

mp(16,'peperoni')
mp(18,'mushrooms','olives')

from functions_basics import *

print(user_profile)