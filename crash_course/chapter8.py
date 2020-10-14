# 8-1. Message
def display_message():
    print("This chapter is about learning functions,\nwhich is re-usable code")
# 8-2. Favorite book
def favorite_book(title):
    print(f"My favorite book is {title.title()}")

# 8-3. T-Shirt
def make_shirt(size, message):
    print(f"We're making a shirt with size {size} and as message we will print '{message}'.")

# 8-4. Large Shirts
def large_shirt(size="Large", message="I love Python"):
    print(f"We're making a shirt with size {size} and as message we will print '{message}'.")


# 8-5. Cities
def describe_city(city, country="USA"):
    print(f"{city.title()} is in {country.title()}")
#describe_city("new york")
#describe_city("florida", "america")
#describe_city("paris", country="mexico")

# 8-6. City Names
def city_country(city, country):
    location = f"{city.title()}, {country.title()}"
    return location
loc = city_country("Amsterdam", "Netherlands")

# 8-7. Album
def make_album(artist, album, songs=None):
    album_0 = {'artist': artist, 'album': album,}
    if songs:
        album_0 ={'artist': artist, 'album': album, 'songs': songs}
    return album_0

tdg = make_album("three day grace","Outsider",13)
"""
while True:
    print("\nEnter a artist name, album and song number if you know it")
    print("\nType 'quit' to exit the program")

    artist_name = input("Artist name: ")
    if artist_name == 'quit':
        break
    album_name = input("Album: ")
    if album_name == 'quit':
        break

    artist = make_album(artist_name, album_name)
    print(f"\nAwnser: {artist}")
"""
# 8-9. Messages
messages = ["Hello this is doge","dos.exe","traps are not gay","drumpf bad"]
def show_messages(messages):
    for message in messages:
        print(message)

# 8-10. / 8-11. Archived Messages
def send_messages():
    copy_messages = []
    for message in messages:
        copy_messages.append(message)
    print(copy_messages)
    print(messages)
send_messages()

# 8-12. Sandwhiches
def sandwhiches(*orders):
    for order in orders:
        print(f"Preparing your {order} sandwhich")

#sandwhiches("ham")
#sandwhiches("ham","cheese","french fries")

# 8-13. User Profile
def build_profile(first, last, **user_info):

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('daniel', 'verlinden',
                             location='netherlands',
                             field='computer science',
                             hobby='studying IT',
                             age=23,
                             education="Cyber security and Cloud")
#print(user_profile)

# 8-14. Cars
def make_car(car, model, **car_info):
    car_info['car'] = car
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

# 8-15: Can't do it because the code doesnt exist
# 8-16.
import pizza
from pizza import make_pizza
from pizza import make_pizza as fn
import pizza as mn
from pizza import *