###########################################################################
                          # LIST
###########################################################################

# And list is an ordered sequence of objects that can be of any type.
# So you can think of them as strengths, right
# We had strengths previously that we learned about, except that each sequence of this string, well,
# was was a string was a letter or a number wrapped in quotation marks.
# Lists, on the other hand, looks something like this.
# list = [ ]

# # Let's say we create a variable ally and lists we denote with square brackets.

# li = [ ]

# # And inside of the square brackets we can have different objects.

# li = [1,2,3,4,5,6]
# li_2 = ['a','b','c']
# li_3 = [1,2, 'a', True]

# In Python lists are a form of array.

# Now, the neat thing about lists is that it's the first data structure that we're learning.
# Data structure is a very important concept in programming languages.
# It's a way for us to organize information and data into, let's say, a folder or a cupboard or a box
# so that these data structures can be used with different pros and cons.

# data sctructure is a containter of inforamtion , strings ,int , float , boal 

# amazon_cart = ['notebooks', 'sunglasses']
# # in memory = [     0     ,      1      ]  

# now we can access this list in diferent ways
 
# print(amazon_cart[0])   # i want item 0 
#  print(amazon_cart[2])   # list index out of range

#list slicing 
# shopping_cart = [
#     'notebooks',
#     'sunglasses',
#     'Toys',
#     'grapes'
# ]

# print(shopping_cart[0:2])

# print(shopping_cart[0::2]) # Strart at 0 go all the way in the end and step over with 2

#list are mutable , witch not like strings i`m able to change my list 
# shopping_cart[0] = 'laptop'
# new_cart = shopping_cart[0:3]
# new_cart = shopping_cart[:]  # if you want to copy a list without modifying
# new_cart[0] = 'gum'
# print(shopping_cart[0:3])
# print(shopping_cart)
# print(new_cart)


###########################################################################
                          # LIST METHODS
###########################################################################


# basket = [1,2,3,4,5]
# print(len(basket))

# # ADDINGS METHOD  .append 

# new_list = basket.append(100)  # .append changes the list in place 
# # so it`s saying , i`m going to append this 100 to this list that you gave me 
# #after we appended than we can assing that the new list point to the list that was modifyed 
# print(basket)
# print(new_list)


# # INSERT METHOD .insert

# basket.insert(4,100)
# print(basket)


# # EXTEND METHOD 
# new_list = basket.extend([100,101,303]) # extend our list 
# print(basket)
# print(new_list)


# # REMOVE METHOD 

# basket.pop()    # it removes the last item of the list in out case 303
# new_list = basket.pop(0)   # remove the item on the index 0 , witch is one 
# print(basket)
# print(new_list)     # got value 1   becouse pop it removes it out of the list but it does return that value back to you 



# # the other method is .remove 

# new_list = basket.remove(4)  #remove doesn`t change the list 
# print(basket)
# print(new_list)

# # the other method is clear .clear()
# new_list = basket.clear()
# print(basket)    # basket is empty , it removes all the items of the list 
# print('\n')
# print('*'*50)
# print('\n')

# # Index method .index   where my data is stored in memory 

# basket = [1,2,3,4,5,6]
# print(basket.index(2))   # it`s asking where is nr two stored in memory 

# basket = ['a','b','c','d','e','b','b']
# #Memory=   0   1   2   3   4
# print(basket.index('c'))         

# #   print(basket.index('d',0,2))    # we got an error becouse we are starting in 0 and stoping in 2 , and d is in index 3
# # if i do 

# print(basket.index('d',0,4))

# # what if we are looking for smth and we are not sure if it`s there or not 
# # that involves python keyword 
# # i can use in  in to say hey is d in basket ? and return a value of true 
# print('d' in basket)
# print('x' in basket)


# # .count   we can count how many times an item ocours 

# print(basket.count('b'))


# Sort list .sort 
from operator import ne


basket = ['a','x','f','c','e','g','d']
# basket.sort()
# print(basket)

print(sorted(basket))    
print(basket)

# the diference betwen sorted()  and .sort()  is that:
# when we use sorted() the function produces a new array and sorted and doesn`t modify the list 
# sorted()   is like we are saying:
#  new_basket=basked[:]
# new_basket.sort()
# print(new_basket)  
# the method modifyes the list 

# it`s also a .copy method that i can use 

new_basket = basket.copy()
print(new_basket)


basket.reverse()
print(basket)
basket.sort()
print(len(basket))
print(basket[::-1])

# generate a list quicly
print(list(range(101)))

# .join method  / join is a string method 
sentence = ' '
new_sentence = sentence.join(['Hi','my','name','is','Ardit'])
print(new_sentence)

# the practice way of dpoing this is 
new_sentence = ' '.join(['Hi','my','name','is','Ardit'])
print(new_sentence)

# list unpacking 
# asign a variable to each items on the list 

# same as with the variables 
a,b,c ,*other ,d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)

# What if we wanted to unpack one, two and three?
# But.
# But keep everything else still in a list.


print(other)
print(d)

###########################################################################
#                       CONCETP OF NONE     
###########################################################################

# If you remember, I mentioned none as a special data type that exists in Python, and most languages
# have something like this to represent the absence of value in some other languages you might have heard
# of NULL, which is another thing that again represents the absence of value.



# Let's say, for example, we're just starting a video game and in this video game we have a user's weapons.
# But when you're just starting the game, there are no weapons that the user has.
# Well, in that case, we might want to assign the variable weapons.
# Maybe in our code we use this variable, but we also want to know that this user doesn't really have
# any weapons.
# It's none.

weapons = None 
print(weapons)

# So this is completely valid python.
# If I run this.
# I get none.