### keep list names pluaral, names, employees, jobs etc. ###

# names list
names = ['ayush', 'koni', 'bhairava', 'lori']

print(names[0].title())

# print(names.title()) gives error, because list is a collection of different types of objects. 
# Therefore, it cannot have a type of it's own.






# Reverse indexing is negative without zero. So last item is -1, second last item is -2.
# print last item from names

print(names[-1].title())






# Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

transports = ['rapido', 'uber', 'aura', 'scooty', 'flights']
transports_informations = [f"I have recently started using {transports[0].title()}", 
						   f"I like {transports[1].title()} more than ola",
						   f"I like the smoothness of {transports[2].title()}\'s engine", 
						   f"I like riding {transports[3].title()} at night to feel the cool wind", 
						   f"I like short duration {transports[4].title()}" ]

print(transports_informations)





# modifying list data type. 

# original motorcycles
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# add ducati motorcycle at end of motorcycles
motorcycles.append('ducati')
print(motorcycles)

# List can also be created from an empty list using append

motorcyles = []
motorcyles.append('yamaha')
motorcyles.append('honda')
motorcyles.append('bmw')


# motorcyles[0] is the first inhabitant of the motorcycles list. motorcycles[0] has an identity of it\'s own.
# It is the occupant with a name. It\'s the first house to be constructed on a street of a new housing project.
# the code
# motorcyles[0] = 'yamaha' 
# will not create a new list because motorcyles[0] is the first label of the list. But the list is empty 
# so motorcyles[0] position does not exist. 

print(f" here are the motorcyles {motorcycles}")





# insert element. I can insert at any position. Just put that position inside the insert method. 
motorcycles.insert(3, 'triumph')
# motorcycles.insert(2, 'triumph')
print(motorcycles)





# remove elements using position

	# 1. del
	# _________

del motorcycles[2]
print(motorcycles)
	# why is del a statement and not a method? What's going on here? what is the underlying difference between statement and method

	# 2. pop
	# _________

	# pop method uses the index to remove the element from the list.

	# It gives the element to us for storing

	# it can be used after sorting to get 1st, 2nd, last, middle data value for future use. This will reduce the list size.
	# So, this will be used get the desired result from the list and the list will fulfill it's purpose of giving itself away 
	# for greater good.

motorcycles.pop(0) # this will also work
x = motorcycles.pop(0)
print(motorcycles, x)



# remove items using value
	# insert method
	# _______________

motorcycles.insert(1, 'ducati')
print(motorcycles)
motorcycles.remove('ducati') # remove methods works on just the first occurence.
print(motorcycles)








# ______________________________________________________________________________________________________________________________
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
# practice
# Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

guests = ['Buddha', 'Nagarjuna', 'Chanakya']

guest_greetings = [f"{guests[0]} I\'m scared of you. I'm afarid you will try to turn me into a monk",
				   f"{guests[1]}, Please teach me the logic and Buddhism", 
				   f"{guests[2]}, help me find my place in the world"]

print(guest_greetings)


# You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# •	 Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
print(f"{guests.pop(0)} will not be available")


# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
guests.insert(0, 'Mahavira')

print(f"I would love to have {guests[0]} in my house")
guest_greetings[0] = f"{guests[0]} is a comtemporary of Buddha. I like his philosophy on Atma and Jeeva "
print(guest_greetings)


# More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
guests.append("Chandragupta Maurya")
guests.insert(0, "Vivekananda")
guests.insert(2, "APJ Abdul Kalam")

print(guests)

print(f"{guests.pop(0)} sorry I have to cancel the invitation due to logistics issue")
print(f"{guests.pop(0)} sorry I have to cancel the invitation due to logistics issue")
print(f"{guests.pop(0)} sorry I have to cancel the invitation due to logistics issue")
print(f"{guests.pop(0)} sorry I have to cancel the invitation due to logistics issue")


print(guests)

print(guest_greetings)

guest_greetings.pop(0)
guest_greetings.pop(0)
print(guest_greetings)

guest_greetings.append(f"{guests[1]} I would love to hear you discuss life with Chanakya")


print(guest_greetings)

# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# ______________________________________________________________________________________________________________________________





# sorting
# sort() method is funfamental nehviour of list creature. This is it's inherent quality.
# sorted() is an external lens that temporarily shows us the sorted list 


# reverse() aka flip
# The list flips itself. reverse two times to get back to original position. 


# list cannot 'length' itself therefore len() function ( lens/tool ) shows us the length of the list.





# ______________________________________________________________________________________________________________________________
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# •	 Store the locations in a list. Make sure the list is not in alphabetical order.

places = ['Switzerland', 'Hawai', 'Alaska', 'Greece', 'Spain']

# •	 Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.

print(places)
# •	 Use sorted() to print your list in alphabetical order without modifying the
# actual list.
print(sorted(places))
# •	 Show that your list is still in its original order by printing it.

print(places)
# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(places, reverse=True))

# •	 Show that your list is still in its original order by printing it again.
print(places)
# •	 Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
places.reverse()
print(places)

# •	 Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
places.reverse()
print(places)

# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
places.sort()
print(places)

# •	 Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

places.sort(reverse=True)
print(places)



# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# ______________________________________________________________________________________________________________________________








# list comrpehension
# 1. Start with list name and []
# 2. Then put the mathematical expression of the value like i**2
# 3. Use a for loop with a range of values
squares = [i**3 for i in range(1, 1_000_000)]
print(sum(squares))



# list slices
# [:3] three from the beginning
# [3:] fourth to last
# [-3:] last to third last






# copy lists
copy_names = names[:]
names.append("himi") # this will not be copied to copy_names. 
# If I had done new_names = names then new_naems would also be modified
print(copy_names)







# ______________________________________________________________________________________________________________________________
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
pizzas =['peppy paneer', 'chicken mushroom', 'veg extravaganza']
friends_pizzas = pizzas[:]

# Then, do the following:
# •	 Add a new pizza to the original list.
pizzas.append("mexicano")
# •	 Add a different pizza to the list friend_pizzas.
friends_pizzas.append("olives")

# •	 Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.
print(pizzas)
print(friends_pizzas)

# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# ______________________________________________________________________________________________________________________________






# tuples

# letters = ('a','y', 'u', 's')
# letter = ('a', )
# We need to include ',' because technically tuples are defined by comma 




# item not in items
print('manas' in names or 'ayush' in names)





# ______________________________________________________________________________________________________________________________
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
foods = ('momo', 'chowmein', 'vada pao', 'tea', 'lassi')

# •	 Use a for loop to print each food the restaurant offers.
for food in foods:
	print(food)

# •	 Try to modify one of the items, and make sure that Python rejects the
# change.
# foods[0]= 'paneer'

# •	 The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.
foods = ('fried momo', 'hakka noodels', 'vada pao', 'tea', 'lassi')
for food in foods:
	print(food)

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# •	 Store the numbers 1 through 9 in a list.
# •	 Loop through the list.
# •	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line.

special_numbers = [1,2,3]
numbers = list(range(1,10))
print(numbers)

for number in numbers:
	if number not in special_numbers:
		print(f"{number}th")
	elif number == 1:
		print("1st")
	elif number == 2:
		print("2nd")
	elif number == 3:
		print("3rd")

# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# ______________________________________________________________________________________________________________________________







# dictionary
# my_dict.get('key', 'return this value if key does not exist')


# for k,v in my_dict.items():


# we can just do with keys method. No mandate to use items method
# my_dict.keys() is not a list. It is a dict key object. It can be used as for loop 
# iterable and with 'in' and 'not in' statements
# ex - if 'tea' not in favourite drinks:
# for drink in drinks.keys()

# Just use the dict name can be used









# ______________________________________________________________________________________________________________________________
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

# Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
glossary = {
'get' :'Dictionary method returns the value of the key or a custom message',
'del' : 'this function delets list element using index and dictionary element using key',
'pop' : 'The indexed element is popped out from the list'
}

# •	 Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.
print('pop', glossary['pop'])
for key, value in glossary.items():
	print(f"{key}\n{value}")

if 'pop' not in glossary:
	print('pop not in glossary')
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# ______________________________________________________________________________________________________________________________








# ______________________________________________________________________________________________________________________________
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# ______________________________________________________________________________________________________________________________


# ______________________________________________________________________________________________________________________________
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# ______________________________________________________________________________________________________________________________


# ______________________________________________________________________________________________________________________________
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# ______________________________________________________________________________________________________________________________





