# 9-1. Restaurant
'''
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}.")
        print(f"We serve {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print("We're open for service tonight.")

restaurant0 = Restaurant("Maguro bros", "Japanese")

print(f"{restaurant0.restaurant_name} {restaurant0.cuisine_type}")
restaurant0.describe_restaurant()
restaurant0.open_restaurant()

# 9-2 Three Restaurants
restaurant1 = Restaurant("BBQ and Chill", "American")
restaurant2 = Restaurant("Sausage & Beer", "German")
restaurant3 = Restaurant("Taco's & Meals", "Mexican")

print(f"We have three restaurants in our town: {restaurant1.restaurant_name}, {restaurant2.restaurant_name}, {restaurant3.restaurant_name}")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

class User:

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"{full_name.title()}, age: {self.age}, location: {self.location}")

    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello {full_name.title()}, Welcome to our website")


# 9-4. Number Served
class Restaurant1:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}.")
        print(f"We serve {self.cuisine_type} cuisine.")
        self.number_served += 22
        print(f"We've served {self.number_served} customers tonight.")

    def open_restaurant(self):
        print("We're open for service tonight.")
        print()

    def increment_number_served(self, served):
        self.number_served += served
        print(f"We have served {served} customers today")

restaurantclass = Restaurant1("El taco", "Mexican")
restaurantclass.describe_restaurant()
restaurantclass.increment_number_served(53)

# 9-5. Login attempts
class User:

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempt = 0

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"{full_name.title()}, age: {self.age}, location: {self.location}")

    def greet_user(self):
        """Greets a user"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello {full_name.title()}, Welcome to our website")

    def increment_login_attempts(self, login):
        """This methods add a login attempt"""
        self.login_attempt += 1
        print(login)

    def reset_login_attempts(self,):
        self.login_attempt = 0
'''

#Skipping this chapter to move on to the next which is "Files and Exceptions, which will be more relatable to school
#Will come back to this on a later data wishing i added more comments and dogstrings

#School hasn't started a month after it was suppost to, kinda disapointing but what can ya do