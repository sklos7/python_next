# Classes - Chapter 9
# classes name always start with the Capital Letter

class Dog():
    """This is the general class about the dog"""
    breed = ''
    name = ''


    # Behaviour, methods
    def bark(self):
        print("wouf wouf!!")

# Object is the instance of class
mydog = Dog() #mydog is the object of Dog() class
mydog.breed = 'German shepard'
mydog.name = 'Rex'
mydog.bark()

yourdog = Dog()
yourdog.breed = 'Bobik'
yourdog.breed = 'Poodle'
yourdog.bark()

class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initializing name and age attributes"""
        self.name = name
        self.age = age


    def sit(self):
        """Simulate a sitting to response to a command"""
        print(self.name.title() + " is now sitting.")


    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
your_dog = Dog("lucy", 3)
my_dog.sit()
my_dog.roll_over()

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old")

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old")
your_dog.sit()
your_dog.roll_over()
my_dog.name


class Car():
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initializing attributes to  describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23500

    def get_disctiptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")


    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_disctiptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()



my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_disctiptive_name())
my_new_car.update_odometer(30)
my_new_car.read_odometer()



class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 16

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' ' + self.cuisine_type.title() + '.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open!')

    def served_numbers(self):
        print("Total number of customers served: " + str(self.number_served))

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, meals):
        self.number_served += meals


new_restaurant = Restaurant('mama mia', 'italian')
new_restaurant.describe_restaurant()


print("New restaurant " + "'" + new_restaurant.restaurant_name.title() + "'" + " is the newest and hottest " + new_restaurant.cuisine_type.title() + " eatery in town!")
new_restaurant.open_restaurant()

new_restaurant.set_number_served(45)
new_restaurant.increment_number_served(15)
new_restaurant.served_numbers()

class Battery():
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=85):
        """Initializing battery attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe a battery size."""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on full charge"
        print(message)



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()

#
# def ElectricCar(Car):
#     def fill_gas_tank():
#         print("this car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_disctiptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = 13

    def ice_flavors(self):
        print("the new Gellato stand has " + str(self.flavors))

new_ice_cream_stand = IceCreamStand("Mama Mia","Gellato Stand")

new_ice_cream_stand.describe_restaurant()
new_ice_cream_stand.ice_flavors()



""" A class that can be used to represent a car"""
