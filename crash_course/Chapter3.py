# 3-1. Names
names = ["Jacky", "Nikola", "Elon", "Dennis"]
#print(names[0])
#print(names[1])
#print(names[2])
#print(names[3])

# 3-2. Greetings
#print(f"Hello {names[0]}, how are you doing today?") #Change the int in the names format to change the name

# 3-3. Your own list
vehichles = ["Volkswagen T1", "Silvia S14", "Silvia S15", "Nissan R34"]
#print(f"I think the {vehichles[0]} is great for travelling.\nThe {names[1]} amd {names[2]} are really cool driving/racing cars.\nAnd the {names[-1]} is just a speed beast!")

# 3-4. Guest list
list = ["albert einstein", "nikola telsa", "dennis richie", "elon musk"]
#for x in list: #Using a for loop to iterate through list, not part of the assignment but this makes it easier and more neatly organized.
    #print(f"Hello {x.title()}, i'm throwing a dinner party and would love if you could make it.\n\nBest wishes\nRes")

# 3-5. Changing guest list
list_cancel =  list[0], list[1]
#print(f"{list_cancel[0].title()} and {list_cancel[1].title()} sadly wont be joining us for dinner tonight.")

new_list = ["elon musk", "nikola tesla"]
#for x in new_list:
    #print(f"\nHello {x.title()}, this is a new invitation to the dinner party since some guests ware not able to make it, hope to see you there.\nDetails will be mailed soon\n\nGreetings\nRes")

#3-6. More guests
#for x in new_list:
    #print(f"Hello {x.title()} more guests will be joining us.")

new_list.insert(0,"warren buffet")
new_list.insert(3,"tony hawk")
new_list.insert(-1, "jezz bezos")

#for x in new_list:
    #print(f"\nHello {x.title()},\n\ni hereby invite you to my dinner party this sunday.\nDetails will follow soon.\n\nGreetings\nRes")

# 3-7. Shrinking guest list
#for x in new_list:
    #print(f"\nHello {x.title()},\n\nIt seems some of the guests won't be in time for dinner.\nThere are only two seats left\n\nGreetings from Res")

popped_guests = new_list.pop() + new_list.pop() + new_list.pop()

#for x in new_list:
    #print(f"Dear {x.title()},\n\nYou're still invited for dinner this sunday.\nI hope to see you at my house\n\nWe'll serve steaks with fine wines, and some fancy deserts!\nHope to see you soon!\n\nGreetins\nRes")

# 3-8. Seeing the World
locations_to_visit = ["japan","death valley","ethiopia: etra ale","washington","north pole"]
#print(locations_to_visit)
#print(sorted(locations_to_visit))
#print(locations_to_visit)
locations_to_visit.reverse()
#print(locations_to_visit)
locations_to_visit.reverse()
#print(locations_to_visit)
locations_to_visit.sort()
#print(locations_to_visit)

# 3-9. Dinner guests
print(f"I'm inviting {len(new_list)} people over for dinner.")

# 3-10. Every function
mountains = ['mount everest','k2','lhotse','manaslu','broad peak']
print(mountains)
sorted_mountains = sorted(mountains)
print(len(mountains))
mountains.insert(0,'cho oyu')
print(mountains)
mountains.pop()
print(mountains)
del mountains[0]
print(mountains)
mountains.reverse()
print(mountains)