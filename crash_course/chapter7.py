# 7-1. Rental Car
car = input("What car would you like to view? ")
print(f"We have the {car.title()} in stock, let me show you")

# 7-2. Restraurant Seating
guests = input("How many guests are you with?")

if int(guests) >= 8:
    print("Please wait for a table")
else:
    print("We have a table for you")

# 7-3. Multiple of Ten
number = input("Enter a multiple of 10: ")
if int(number) % 10 == 0:
    print("This is a multiple of 10")
else:
    print("This isn't a multiple of 10")

# 7-4. Pizza Toppings
request = ""
while request != 'quit':
    request = input("What topping would you like? ")
    if request != 'quit':
        print(f"Adding {request} to pizza...")

# 7-5. Movie Tickets
age_price = input("How old are you? ")
if int(age_price) <= 3:
    print("Your childs ticket is free")
elif int(age_price) <= 12:
    print("Your ticket will be $10")
elif int(age_price) > 12:
    print("The ticket will cost $15")

# 7-6. Thee Exits
requests = []
request = ""
while request != 'quit':
    request = input("What topping would you like? ")
    if request == 'pineapple':
        print("Get out...")
        break
    elif request != 'quit':
        print(f"Adding {request} to pizza...")
        requests.append(request)
        if len(requests) > 6:
            print("You have ordered too much, no more than 6 toppings per pizza")
            break
        print(requests)

# 7-7. Infinity
while True:
    print("Welcome to the matrix")

# 7-8. Deli
sandwhich_orders = ["meatball","chicken","pastrami","grilled cheese","pastrami","veggie","smoked salmon","pastrami"]

finished_sandwhiches = []
while sandwhich_orders:
    while "pastrami" in sandwhich_orders:
        sandwhich_orders.remove("pastrami")
    order = sandwhich_orders.pop()
    finished_sandwhiches.append(order)
    print(f"Finsihed making {order} sandwhich.")
# 7-9. No pastrami above in Deli

# 7-10. Dream Vacation
responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("What would be your dream vacation ")

    responses[name] = response

    repeat = input("Would you like to enter your dream vacation? (yes/no) ")
    if repeat == "no":
        polling_active = False
    elif repeat == "yes":
        continue

    print("\n-----Polling Results----")

    for name, response in responses.items():
        print(f"{name.title()} would like to go on vacation to: {response}.")