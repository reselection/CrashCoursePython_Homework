# 6-1. Person
person_0 = {'first': 'elon',
          'last': 'musk',
          'age': 49,
          'city': 'bel air',
          }

# 6-2. Favorite Numbers
fav_num = {'sindre': 9,'theo': 5, 'niep': 8, 'res': 7, 'ptx': 4}
for num in fav_num:
    print(f"{num.title()} favorite number is {fav_num[num]}")

# 6-3. Glossary
programming = {'tuple': 'immutable list',
               'integer': 'solid number',
               'float': 'number with a dot',
               'list': 'mutable list',
               'dictionary': 'holds a key with its assigned value',
               }
for key in programming:
    print(f"\n{key.title()}: {programming[key]}\n")

# 6-4 Glossary 2 Already made this in 6-3 so no need to replace anything

# 6-5
rivers = {'nile': 'egypt',
          'niagara falls': 'united states',
          'congo river': 'congo',
          }
for river in rivers:
    print(f"The {river.title()} runs through {rivers[river].title()}")

# 6-6. Polling
favorite_langauge = {'jen': 'python',
                     'sarah': 'c',
                     'edward': 'ruby',
                     'phil': 'python',
                     }
poll = ['theo','res','sindre','phil','jen']
for name in poll:
    if name in favorite_langauge:
        print(f"Thank you for submitting an answer {name.title()}!")
    else:
        print(f"{name.title()}, would you like to sumbit your favorite programming language?")


# 6-7. People
person_1 = {'first': 'sindre',
            'last': 'knudsen',
            'age': 21,
            'city': 'scav'
            }
person_2 ={'first': 'theo',
           'last': 'bendall-breen',
           'age': 24,
           'city': 'guilford',
           }

for key, value in person_1.items():
    print(f"{value}")

# 6-8. Pets
teddy = {'animal': 'bear',
         'owner': 'Vlad',
         'age': 13,
         }
blubs = {'animal': 'fish',
         'owner': 'garry',
         'age': 4,
         }
world_ender = {'animal': 'cat',
               'owner': 'rick',
               'age': 14,
               }
pets = [teddy, blubs, world_ender]
for pet in pets:
    print(pet)

# 6-8. Favorite Places
favorite_places = {'sindre': 'the garage',
                   'theo': 'the lake',
                   'niep': 'online',
                   }
for person, place in favorite_places.items():
    print(f"{person.title()}'s favorite place is {place}")

# 6-10. Favorite Numbers
fav_num = {'sindre': [9, 13],
           'theo': [5, 22],
           'niep': [8, 2],
           'res': [7, 13],
           'ptx': [22,4],}
for name, nums in fav_num.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for num in nums:
        print(f"\t{num}")

# 6-11 Cities
cities = {'amsterdam': {'country': 'the netherlands',
                        'population': '17,418,65',
                        'fact': 'known for the coffeeshops',
                        },
          'new york': {'country': 'the united states',
                       'population': '308,401,808',
                       'fact': 'The Empire State Building gets hit by lightning around 23 times a year.'
                       },
          'tokyo': {'country': 'japan',
                    'population': '126,476,461',
                    'fact': 'The Tsukiji Market is the world’s largest, busiest fish market.'
                    },
          }
for city, info in cities.items():
    print(f"\n City: {city.title()}")
    print(f"\t Is located in {info['country'].title()}\n\tThe population is: {info['population']}\n\tA fun fact:\n\t\t{info['fact']}")

