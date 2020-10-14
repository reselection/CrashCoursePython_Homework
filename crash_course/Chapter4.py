# 4-1
bad_pizza = ['pineapple', 'veggie', 'tofu']
for pizza in bad_pizza:
    print(f"I don't like {pizza.title()} pizza")

# 4-2. Counting to Twenty
common_animals = ['cat', 'great white shark', 'lion' ]
for animal in common_animals:
    print(f"\n{animal.title()}, is one of the best hunters in the world")
    print("These animals are very good hunters")

# 4-3. Counting to Twenty
for num in range(1,21):
    print(num)

# 4-4. One Million
for num in range(1,1000000):
    print(num)

# 4-5. Summing a million (just gonna do big random nums
big_list = [23, 44, 1223 ,22, 1]
print(min(big_list),max(big_list),sum(big_list))

# 4-6. Odd numbers
for num in range(1,22,2):
    print(num)

# 4-7. Threes
for three in range(3,31,3):
    print(three)

# 4-8. Cubes
for cube in range(1,11): # A number raised to the third power is called a cube.
    print(cube ** 3)

# 4-9. Cube Comprehension
cubes = [cube**3 for cube in range(1,11)] # A for loop that has a for loop in it
print(cubes)

# 4-10. Slices
#print(common_animals[:3])
print(big_list[1:-1])
print(big_list[-3:])

# 4-11. My Pizzas, Your Pizzas
friend_pizzas = bad_pizza[:] # To copy a list and make it unique you must add [:]
bad_pizza.append("califlower")
friend_pizzas.append("triple cheese")
print("Pizzas that i dislike:\n", bad_pizza)
print(friend_pizzas)

#4-12.
for food in bad_pizza:
    print(f"{food.title()} pizza")
for food in friend_pizzas:
    print(f"My buddy likes{food.title()} pizza")

# 4-13.
basic_foods = ('beef','cooked potatoes','brocoli','porkchops','rice')
for food in basic_foods:
    print(food.title())

basic_foods = ('beef','cooked potatoes','brocoli','fish','chicken')
for food in basic_foods:
    print(food.title())

