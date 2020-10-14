# 5-1. Conditional Tests
car = "nissan"
print(car == "nissan") # = True
print(car == 'audi') # = False
print(car != "nissan") # = False
print(car != 'audi') # True
print("nissan" in car)
print("audi" in car)
print(len(car) > 4)
print(len(car) < 4)
print(len(car) >= 6)
print(len(car) <= 5)

# 5-2. More Conditional Tests
print("5-2")
print(car == "Nissan")
print(car == "NISSAN".lower())

print(car == "NISSAN".lower or car == "nissan")

print(car =="NISSAN" or len(car) == 6)


print(car == list)
print(car != list)

# 5-3. Alien Colors #1
alien_color = 'red'

if alien_color == 'green':
    points = 5
if alien_color == 'yellow':
    print("Yellow")
if alien_color == 'red':
    points = 5
print(f"You killed a {alien_color} alien, and got {points} points!")

#5-4. Alien Colors #2
alien_color = 'blue'
if alien_color == 'green':
    points = 5
    print(f"You just earned {points} points!")
if alien_color != 'green':
    points = 10
    print(f"You just earned {points} points")

alien_color = 'blue'
if alien_color == 'green':
    points = 5
    print(f"You just earned {points} points!")
else:
    points = 10
    print(f"You killed a {alien_color} alien, and recieved {points} points")

# 5-5; Alien Colors #3
alien_color = 'yellow'
if alien_color == 'green':
    print('You recieved 5 points')
if alien_color == 'yellow':
    print("You recieved 10 points")
if alien_color == 'red':
    print("You earned 15 points")

# 5-6
age = 3

if age < 2:
    print("You're a baby")
elif age >= 2 and age < 4:
    print("You're a toddler")
elif age >= 4 and age < 13:
    print("Yer a kiddo")
elif age >= 13 and age < 20:
    print("You're a teenager")
elif age >= 20 and age < 65:
    print("You're an adult")
else:
    print("You're an elder")

# 5-7 Favorite Fruit
fruits = ['mango', 'watermelon', 'strawberry','peach']

fav_fruits = fruits[-3:]
print(fav_fruits)
if 'peach' in fav_fruits:
    print("Peach is great")
if 'banana' in fav_fruits:
    print("Banana is a good food for bodybuilders")
if 'watermelon' in fav_fruits:
    print("Melons are very juicy")
if 'mango' in fav_fruits:
    print('Mango is a tropical fruit')
if 'strawberry' in fav_fruits:
    print("A large juicy berry")

# 5-8. Hello Admin:
usernames = ['reselection','zombiecamper','theo','tolly','admin']

if 'admin' in usernames:
    print("Hello admin, would you like to see a status report? Y/n")
else:
    print("Hello Jaden, welcome back")
# 5-9
if usernames:
    print("We need to find some users!")
else:
    for name in usernames:
        print(f"Removing {name} from database.")
        name.pop()

# 5-10. Checking for usernames
current_users = ['res', 'theo' 'zombie' 'tolly' 'admin']
new_users = ['jack', 'theo','ptx','zombie','ray']

# 5-11. Ordinal Numbers
numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num == 1:
        print(f'{num}th')
    elif num == 2:
        print(f'{num}nd')
    else:
        print(f'{num}st')