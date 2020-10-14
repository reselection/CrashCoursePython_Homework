import json

# 10-1. Learning Python
outside = ''
with open('learned.txt') as learned: #Using this method Python will close the file for me
    for line in learned:
        #print(line.strip())
        outside += line

#print(f"\n{outside}" )
# Here we can still work with the data from the file while its already closed, since its saved to the variable "outside"

# 10.2. Learning C
#Skipping this for now .replace() doesnt seem to be working correctly according to the book

#1 10-3. Guest
"""with open('guest.txt','w') as guest_list:
    guest = input("What is your first and last name? ")
    guest_list.write(f"\n{guest.title()}")
"""
# 10-4. Guest-book
'''
while True:
    print("press 'quit' to exit the program")
    name = input("What is your name? ")
    if name == 'quit':
        break
    with open('guest_book.txt','a') as guest_book:
        print(f"Hello {name.title()}, we've reserved a table for you")
        guest_book.write(f"\n{name.title()} has reserved a table.")
'''
# 10-5. Programming Poll
'''
while True:
    poll_awnser = input("Why do you like progamming?")
    with open('programming_pol.txt', 'a') as programming_pol:
        programming_pol.write(poll_awnser)
'''
# 10-6. Addition
def sum_of_two(num1, num2):
    '''Adds two numbers together, if a ValueError is raised the function will ask for two numbers'''
    try:
        print(int(num1) + int(num2))
    except ValueError:
        print("Enter two numbers, not text")

# 10-7. Addition Calculator
'''
while True:
    try: # Previous code was in a function so i made some a new program here
         # While loop asking for two numbers, print the result if ValueError is raised you get a friendly error
        print("\nPress q to quit")
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        if num1 == "q" or num2 == 'q':
            break
        print(int(num1) + int(num2))
    except ValueError:
        print("Enter two numbers, not text")
'''

# 10-8. Cats and Dogs
'''
try:
    with open('cats.txt') as file:
        for cat in file:
            print(cat)
except FileNotFoundError:
    print("Failed")

# 10-9. Silent Cats and Dogs

try:
    with open('cas.txt') as file:
        for cat in file:
            print(cat)
except FileNotFoundError:
    pass
'''
# 10-10. Common Words
'''
with open('science.txt', 'r') as file:
    words = file.read()
    print(words.count('the '))
'''

# 10-11. Favorite number
'''
favorite_number = input("What is your favorite number? ")
file_favorite = 'favnum.json'

with open(file_favorite, 'w') as ffav:
    json.dump(favorite_number, ffav)

with open(file_favorite) as saved_favorite:
    saved = json.load(saved_favorite)
    print(f"We have saved your favorite number: {saved}")
'''

# 10-12. Favorite Number Remembered
# Need to come back here later

# 10-13. Verify user

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as  file:
        json.dump(username, file)
    return username

def greet_user():
    """Greet user by name"""
    username = get_stored_username()
    if username:
        confirm = input(f"Is this the correct username? {username} (yes/no) ")
        if confirm == 'yes':
            print(f"Welcome back { username}")
        elif confirm == 'no':
            get_new_username()
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as file:
            json.dump(username, file)
            print(f"We'll remember your name, {username}.")

greet_user()