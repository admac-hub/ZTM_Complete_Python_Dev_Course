# #Fundamental Data Types 

###########################################################################
                          # #integers 
###########################################################################
# print(2 + 4) 
# print(2 - 4)
# print(2 * 4)
# print(2 / 4)

# #what`s the type of 2 + 4
# print(type(2 + 4))   #what`s the type of 6 , 6 is an integer 
# print(type(2 - 4))
# print(type(2 * 4))
# print(type(2 / 4))

# # print(type(0))   #INT 

# # float takes a lot more space in memory then a int 
# # to store a int the machine conver that in binary and the int take one location in memory
# # 12

# # to store a float it takes two location x.y one for x and one for y



# print(2 ** 2)   # ** to the power of 
# print(2 // 4)  # int division 
# print(5 % 4)  # the remainder 


# print(round(3.1))

# print(abs(-20))  #absolute value 



#Operator Precedence 
# from numpy import binary_repr


# print((20 - 3) +3 ** 4)  # first we follow ( ) # second is **

# complex number 

# int & float get stored in memory such as 5 as binary 

# bin(5) return the binary_repr 

# print(bin(4))
# print(int('0b101',2))  # we are saying grab this nr from memory (thin nr is base 2) convert it to int and print the value 

###########################################################################
                          #STRINGS  
###########################################################################

#A string is a pice of text it can be wrinten with quotation marks or double quotes 

# print(type('hello'))
# print(type("hello world"))

# #For example, imagine you're creating a login form and we want to collect somebodies username and password.
# #Well we can have username variable that we assign, let's say some sort of username.

# username = 'supercoder'
# password = 'supersecret'
# long_string = '''  
# wow
# 0 0
# ---
# '''
# #mulit line string

# print(long_string)


# #What if I had something like this?
# #Let's say I wanted to grab the first name of a user.

# first_name = 'Ardit'
# last_name = 'Cuko'
# full_name = first_name + ' ' + last_name
# print(full_name)

# ###########################################################################
#                           #STRING CONCATENATION
# ###########################################################################

# #ADDNG STRINGS TOGETHER

# print('hello' + 'Ardit')

# ###########################################################################
#                           #TYPE CONVERTION
# ###########################################################################


# print(c)

# print(type(str(100)))
# print(type(int(str(100))))

# a = str(100)
# b = int(a)

# c = type(b)

# print(c)



###########################################################################
                          #ESCAPE SEQUENCE 
###########################################################################


# from dataclasses import replace
# from types import new_class


# Weather_2 = 'it'#s suny'    # ?? no idea what this is 

# Weather_sd = "it`s sunny"

# Weather = " it\`s \"kind of \" sunny  hope you have a good day"     # whaterver come after \ i recognize it , i`m going to asume it`s a string 
# # \t  - tab
# # \n  - new line 
# print(Weather)

###########################################################################
                          #FORMATED STRING
###########################################################################


# Up until now, we've just written simple strings, but we want a program that's dynamic, that's static.

# name = 'Ardit'
# age = 27

# print('Hi ' + name + '. you are ' + str(age) + ' year old')

# But there's a better way of doing this.
# And with formatted strings, all we need to do is add an F at the beginning.
# And this F at the beginning is going to tell Python, hey, this is going to be a formatted string.
# And instead of doing all this plus and name and all this stuff and doing the STR to convert the type.
# We can simply do something like this.

#this is python 3 
# print(f'Hi  {name}. you are  {age}  year old')

# #this is python 2 
# print('Hi  {}. you are  {}  year old'.format('Ardit','55'))

# print('Hi  {}. you are  {}  year old'.format(name,age))

# print('Hi  {new_name}. you are  {age}  year old'.format(new_name='sally',age=age))

###########################################################################
                          #STRING INDEXES
###########################################################################
#str order seq of character
# and strings underneath the hood are stored in memory, as I said, as an ordered sequence of characters.

# selfish = 'me me me'
#           #01234567

# So if you think of a bookshelf, each one of these is ordered in a different part of the bookshelf,
# but one after another.
# And the way we can think about this is like this.
# The M is stored in location zero and then E is stored in location one and then space is stored in location
# two and so on and so forth.
# And each shelf now corresponds

# print(selfish[0])

# Well, using the square brackets, I'm telling the computer.
# Hey, grab the variable.
# Selfish.
# And then from that variable selfish grab whatever is an index of zero.
# And what's on that bookshelf of index of zero?  M

# print(selfish[7])

# print(selfish[4])

# #[where to start : where to stop]
# numbers = '01234567'
#           #01234567
# print(numbers[0:2])   #[0:2] grab 0 and stop as soon as you get to bookshelf 2

# print(numbers[0:8])

# #[where to start : where to stop : stepover]   defaoul of stepover i 1 

# print(numbers[0:8:2])

# print(numbers[0:8:3])

# print(numbers[1:]) #start at one and stop all the way to the end 
# print(numbers[:5]) # start default 0 and stop top 5

# print(numbers[:5:2]) # start default 0 and stop top 5 stepover with 2 

# print(numbers[-1])  # i get 7
# # The negative index means, hey, start at the end of the string

# print(numbers[::-1]) #[start:stop:step over from the back] this reverse the order 
 
# numbers = '01234567'
#           #01234567

# # numbers[0] = '8'
# print(numbers)



# print(len('hello world'))   # len()   count as human start from 0 \

# greet = 'hellllopooo'
# print(greet[:])           # [:] it`s called  slicing 

# print(greet[0:len(greet)])



###########################################################################
                          # BOLEANS 
###########################################################################
# THERE`S ONLY TWO OPTIONS IT`S EITHER TRUE OR FALSE 

# name = 'Ardit'
# is_cool = False

# And then I can say, well, let's say we're creating an even better social network than Facebook or
# creating our own.
# And this social network also has the is cool option on your user profile.
# And let's say for now it's false.
# You see over here that's being highlighted now is cool is set to false.

# is_cool =True

# Booleans represent this idea of true and false, which in programming is kind of like saying zero and one.



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

