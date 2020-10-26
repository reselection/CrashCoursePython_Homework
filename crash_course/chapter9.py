# Remove docstrings from the tests to view the code, or add your own tests.

#9-1. Restaurant
class Restaurant:
    """This class will describe the restaurant and when its open"""
    def __init__(self, restaurant_name, cuisine_type):
        """Here we define our attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """prints the restaurant name and cuisine type"""
        print(f"Restaurant {self.restaurant_name} serves {self.cuisine_type} food")

    def open_restaurant(self):
        """A method to show the restaurant is open"""
        print("We're open!")
'''
restaurant = Restaurant("Sushi Bar", "Japanese")

print(f"Name:{restaurant.restaurant_name}, Cuisine:{restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2. Three Restaurants

restaurant1 = Restaurant("KFC", "Kentucky style")
restaurant2 = Restaurant("Meat & More", "American")
restaurant3 = Restaurant("Nam & Beer", "Indian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
'''
#9-3. Users
class User:
    """This class holds user info, describes a user and greets him"""
    def __init__(self, first_name, last_name, age, country):
        """Here we define our attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        """This method describes a user, full name, age and country"""
        print(f"Name:{self.first_name} {self.last_name}, age:{self.age}, country:{self.country}")

    def greet_user(self):
        """A method that greets the user, if the great Destroyer is recgonized offer to drop a nuke."""
        full_name = f"{self.first_name} {self.last_name}"
        if full_name == "Donald Biden":
            print(f"Welcome {full_name.title()} would you like to call in a tactical nuke?")
        else:
            print(f"Welcome {full_name}, how are you doing today?")
"""
user1 = User("Donald", "Biden", 101, "USA")

user1.describe_user()
user1.greet_user()

user2 = User("Elon","Musk", 43, "South Africa")

user2.describe_user()
user2.greet_user()
"""

#9-4. Number Served
class Restaurant9_4:
    """
    Version 2 of Restaurant, added how many people have been served
    and added a method to increase this number when called for
    """
    def __init__(self, restaurant_name, cuisine_type):
        """Here we define our attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """prints the restaurant name and cuisine type"""
        print(f"Restaurant {self.restaurant_name} serves {self.cuisine_type }.")

    def open_restaurant(self):
        """A method to show the restaurant is open"""
        print("We're open!")

    def set_number_served(self, served):
        """Set the number of poeple served"""
        self.number_served = served
        print(f"People served: {served}.")

    def increment_number_served(self, customers_served):
        """Increment the amount of people served"""
        customers_served += self.number_served
        print(f"People served: {customers_served}.")
'''
people_fed = Restaurant9_4("Tokitoki", "Asian")
people_fed.set_number_served(20)
people_fed.increment_number_served(20)
'''

#9-5. Login Attempts
class Userv2:
    """
    Version 2 of User.
    Added two methods increment logins and reset login.
    One that keeps track how many times a login attempt has been made,
    and the other to reset the login attempts (Code isn't in a while loop so it will not hold the login attempts
    after the program stops)
    """
    def __init__(self, first_name, last_name, age, country):
        """Here we define our attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        """This method describes a user, full name, age and country"""
        print(f"Name:{self.first_name} {self.last_name}, age:{self.age}, country:{self.country}")

    def greet_user(self):
        """A method that greets the user, if the great Destroyer is recgonized offer to drop a nuke."""
        full_name = f"{self.first_name} {self.last_name}"
        if full_name == "Donald Biden":
            print(f"Welcome {full_name.title()} would you like to call in a tactical nuke?")
        else:
            print(f"Welcome {full_name}, how are you doing today?")

    def increment_login_attempts(self):
        """increment the login attempts by 1"""
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")
    # If you run the code again you will notice that it will always remain 1, unless you call
    # the method increment_login_attempts, this is becauses the code resets and cannot hold the value of login_attempts.
    # You can change this by adding a while loop to save the value.

    def reset_login_attempts(self):
        """This method resets the login attempts to 0, and returns a f string indicating this"""
        self.login_attempts = 0
        print(f"We have reset your login attempts\n\tLogin attempts:{self.login_attempts}")

userlog = Userv2("Res", "Greenie", 23, "The Netherlands")
"""
userlog.increment_login_attempts()
userlog.increment_login_attempts()
userlog.increment_login_attempts()
userlog.reset_login_attempts()
userlog.increment_login_attempts()
"""

#9-6. Ice Cream Stand
class IceCreamStand(Restaurant9_4):
    """
    Icecream class that inherents from Restaurant9_4 for flavor display
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes from the Parent class.
        """
        super().__init__(restaurant_name, cuisine_type)

    def ice_selection(self):
        """
        This method holds the icecream flavors, and when called will print them out with a
        for loop.
        """
        self.icecreams = ['vanila', 'strawberry', 'chocolate']

        print("We have the following flavors:")
        for icecream in self.icecreams:
            print(f"\t - {icecream.title()}")
'''
flavors = IceCreamStand("IceCream Stand", "Belgium Icecreams")

flavors.describe_restaurant()
flavors.ice_selection()
'''

#9-7. Admin
class Admin(Userv2):
    """A class for the Admin, that inherents from Usersv2"""

    def __init__(self, first_name, last_name, age, country):
        """Initialize attributes"""
        super().__init__(first_name, last_name, age, country)
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can change passwords', 'can change titles']
        self.privilege = Privileges()

    def show_privileges(self):
        """This atribute will use a for loop to list all the admin privileges"""
    '''
        print('Admin priviledges include:')
        for privilege in self.privileges:
            print(f"\t{privilege.capitalize()}.")
    '''
'''
admin = Admin("Code", "Election", 23, "The Netherlands")
admin.show_privileges()
'''
#9-8. Privileges
class Privileges:
    """This class displays the admin powers."""
    def __init__(self):
        """Initialize attributes"""
        self.privileges = ['can add post', 'can pin a post', 'can ban user', 'can delete post']

    def show_privileges(self):
        """This atribute will use a for loop to list all the admin privileges."""
        print('Admin priviledges include:')
        for privilege in self.privileges:
            print(f"\t{privilege.capitalize()}.")
'''
adminuser = Admin("Code", "Election", 23, "The Netherlands")
adminuser.privilege.show_privileges()
'''

#9-9. Battery Upgrade
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        """prints a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
"""
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(20000)
my_new_car.read_odometer()

my_new_car.increment_odometer(1000)
my_new_car.read_odometer()
"""
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes from the Parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def battery_upgrade(self):
        if self.battery_size != 100:
            self.battery_size = 100

'''
my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.get_range()
my_tesla.battery.describe_battery()

my_tesla.battery.battery_upgrade()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
'''
