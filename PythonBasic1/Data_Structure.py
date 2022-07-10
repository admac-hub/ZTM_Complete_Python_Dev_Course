###########################################################################
#                       DICTIONARY  
###########################################################################
print('*'*40)
print('**********','DICTIONARY','*******************')
print('*'*40)
print('\n')

from re import M, U


dict 

# Dictionary.
# What is it ?
# Well, it's a data type in Python, but it's also a data structure.

# It's a way for us to organize our data in a form that is has some different pros and cons in how we
# access it, for example, with lists.
# We saw that they're easily ordered.
# We can access them through indexes like zero one.
#  {}  denotes a dicitionary 
dictionary = {
    #key : value
    'a':1,
    'b':2,
    'x':3
}

# A key is a string for us to grab the value.

print(dictionary['b'])

# We're essentially telling the computer, Hey, I have this variable dictionary.
# I have this variable dictionary.
# I want you to go find the key B and this key B, if it exists, grab me the value.
# So it's going to go into your memory or into the machine's memory.
# It's going to find where B is stored in our memory and grab the value.

#print(dictionary['C'])  # We recive a key error , becouse that key doesn`t exist 

# the diference between list is that list it has this bookshelves right next to each other 
# dictionary is scatered all over our memory 

print(dictionary)


# Now here's the cool thing about data structures like dictionaries and lists.
# They're containers around data, right?
# So this can be anything that we want.
# Let's say we want this one to be a list.

fjalori = {
    #key : value
    'a': [1,2,3,4,5],
    'b': 'hello',
    'x': True
}

print(fjalori['a'][2])


my_list = [
    {
    #key : value
    'a': [1,2,3,4,5],
    'b': 'hello',
    'x': True 
 },
    {
    #key : value
    'a': [6,7,8,9,10],
    'b': 'world',
    'x': False 
 }
 
]
# So that I can now grab from my list.

print(my_list[0]['a'][2])
print(my_list[0]['a'][1])
print(my_list[1]['a'][2])
#print(mylist[first item on the list][key][item on the disctionarty])


user = {
    'basket':[1,2,3],
    'greet': 'hello',
    'age': 20
}

# So another good way to access a key and to see if it even exists is to use dot get and guess what dot
# get is.
# Did you guess a method?
# Well, there you go.
# Dot get is a method on the object or the dictionary in Python.

print(user.get('age', 55))   #program doesn`t error but says that the value is non , key do not exist 
              # if key age don`t exist , the default value should be 55

#this is not a common way of creating dictionary 
user2 = dict(name='Ardit')
print(user2)

# By the way, there is actually one more way that we've actually seen in list how to look for an item
# in a dictionary.
# Remember how enlists we use the keyword in.
# We said something along the lines of Hey, is I in a list that contains I or we even use a string like
# hi.
# Well, you can do the same with dictionaries

print('*'*40)
# Does basket exist in user ?
print('basket' in user)   # = True it does 

# What about size ?
print('size' in user) # = False it doesn`t exist 

# Dictionary method .keys() simply check the keys 

# If i wan`t to check keys
print('age' in user.keys())

# if i wan`t to check values 

print('hello' in user.values())


# .items()    grabs the entire item

print(user.items())   # print`s a tuple 


# .clear()

# print(user.clear())
# user.clear()
# print(user)


# copy a dictionary 

user2 = user.copy()
print(user)
print(user2)


# .pop  removes a value or  a key from dictionary 

print(user.pop('age'))
print(user.popitem()) # pops a pair of [key : value]
print(user)

# .update   update`s  the dicionary 

print(user.update({'ages': 55}))
print(user)


###########################################################################
#                       TUPLES   
###########################################################################
print('*'*40)
print('**********','Tuples','**********************')
print('*'*40)
print('\n')

# Well, a tuple are like lists, but unlike lists we cannot modify them.
# There are immutable so you can think of them as immutable lists and they look like this.

my_tuple = (1,2,3,4,5)
# my_tuple[1]='z'    

# It's going to tell me hey tuple object does not support item assignment.
# A tuple is immutable.
# Once you create it, it's the way it is.
# You can't sort it or reverse it like we saw with lists.
# It's just there.

print(my_tuple[2])
print(3 in my_tuple)

# So a good use of a tuple for example, if you work at Uber is geographic location and coordinates,
# right?
# You can have latitude and longitude here.
# And because let's say this won't change or maybe a user's location or pickup point doesn't often change.
# We can just use a tuple.

print(user.items())


# a tuple is a valid key in python 

# tuples, like I said, are quite similar to lists.

new_tuple = my_tuple[1:2]
print(new_tuple)   # a tuple that has a single item return a value and ,
x , y ,z , *other = my_tuple

print(x)
print(y)
print(other)

print(my_tuple.index(3))
print(len(my_tuple))

###########################################################################
#                       SET  
###########################################################################
print('*'*40)
print('**********','SET','*************************')
print('*'*40)
print('\n')

# set`s are unordered collection of unique objects 
# we create them with currly brackets like dictionaires 

my_set = {1,2,3,4,5,5,3,4}
print(my_set)  # it only return 1,2,3,4,5 / in set`s ther`s no dublicates 

my_set.add(100)
my_set.add(2)
print(my_set)   #added 100 but not 2 


#  If I gave you an array.
# And let's say this are contained.
# Well, this right here.
# And I want you to return an array with no duplicates.

my_array = [1,2,3,4,5,6,3,4,4,5,6,6,]
print(set(my_array))   # we use the built in funtion set to convert it 

# Imagine if we had usernames, right?
# Or email addresses.
# We're collecting email addresses on our startup page, but we don't want to have duplicate emails.
# We might want to convert this a list of emails to a set and remove any duplicates.
# So we're not sending emails over and over.


my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}


# set methods  .difference()

print(my_set.difference(your_set)) #what id diferent from your_set with my_set
print(your_set.difference(my_set))

# .discard() 
# print(my_set.discard(5))
# print(my_set)   # ignored 5 

# .diference_update()
# print(my_set.difference_update(your_set)) # it print none 
# print(my_set)  # it print 1,2,3 so we updating it that the diferences are removed 

# .intersection()   = & 
print(my_set.intersection(your_set)) #  print`s what two set`s have in common 
print(my_set & your_set)

# .isdisjoint()
print(my_set.isdisjoint(your_set))    #isdisjoint mean they have nothing in comon
# in out case our sets have values in comon so it reutrns false 


# .union()

print(my_set.union(your_set))   # join setes but removes the duplicates 
# .union()  = |

print(my_set | your_set)  


# .issubset()
other_set = {4,5}
print(other_set.issubset(your_set))

# .issuperset

print(other_set.issuperset(my_set))
print(my_set.issuperset(other_set))
