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

