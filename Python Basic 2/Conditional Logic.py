###########################################################################
#                           CONDITIONS
############################################################################


# We're going to create a car that automatically detects if you can start the engine.
# Maybe if you're not old enough, the engine won't start and it won't let you drive so that they make

from tkinter import W
from urllib import response


is_old = True
is_licenced = False

# is saying if true: return the values inside () 
# if it`s true im runing , if it`s false i`m skipping 
if is_old:
    print("you are old enough to drive") 
elif is_licenced:
    print('you can driver now')
else:
    print('you are not of age')

print('okokok')
# if wasn`t true so im running else 
# else run if the first line of code evaluates to false 

# So we learned that there is this if keyword, but there's also another thing we can use called else.
# And you'll notice here that I didn't add it to the indentation.
# And else, as the name suggests, simply says.


# Hey, if this something is true, 
#       then do this.
# Otherwise also else 
#       do this.

# the power of indentention is that we will be able to skip line 
print('\n')

# and is another keyword , both expressions has to evaluate to true 
# elif is used to set multiple conditions 

if is_old and is_licenced:
    print('you are good to drive')
else:
    print("you don`t meet the minimim requiremnts to drive")



###########################################################################
#                          INDENTETIONS 
############################################################################
print('\n')
print('IDENTENTION')
print('*'*20)
print('\n')

if is_old:
    print("you are old enough to drive") 
elif is_licenced:
    print('you can driver now')
else:
    print('you are not of age')

print('okokok')

# Every single line of code always starts as well in the first space.
# Different languages will use this differently.
# But in order to organize code, usually you'll see some indentation like this.
# Now.
# Python, however, is unique because the indentation and spaces that we see here.
# Makes the interpreter see it and say, Hey, this means something.
# The interpreter would actually see the space and say, because there space here, I know that this is
# part of the if.

###########################################################################
#                          TRUTHY 7 FALSEY
############################################################################
print('\n')
print('TRUTHY & FALSEY')
print('*'*20)
print('\n')

is_old = 'hello'  # behind the scennes python is convertin this values to bolean
is_licenced = 23

print(bool('hello')) # this is a truthy 

print(bool(''))
print(bool(0)) # this is a false , it retur a false value 

if is_old:
    print("you are old enough to drive") 
elif is_licenced:
    print('you can driver now')
else:
    print('you are not of age')

print('okokok')

print('*'*20)
print('\n')


password = '123'
username = 'Ardit'

if password and username:
    print('you can login')
else:
    print('please login with your username and password')


###########################################################################
#                          TERNARY OPERATOR
############################################################################
print('\n')
print('TERNARY OPERATORS')
print('*'*20)
print('\n')
# So you can only use these on certain conditional logic.
# This is a shortcut, in a sense for you to make your code a little bit cleaner.
# ternary operators can also be called conditional expressions.

# So a ternary operator or a conditional expression is an operation that evaluates to something based
# on the condition being true or not.

# The way we use this is to say 
# 
# is condition. #If this is true,   # then do this.


#   condition_if_true  if condition else condition_if_false
            # IF is cheking the condiiton
            # so it`s starts in the midle is daying if the condition is true run left 
            # else run on the right 
        
# Let's say we're trying to determine a well, if a user is your friend, so we'll say is friend.

is_friend = False
can_message = 'messafe allowed' if is_friend else 'not allowed to message'

print(can_message)


###########################################################################
#                          SHORT CIRCUITING
############################################################################
print('\n')
print('SHORT CIRCUITING')
print('*'*20)
print('\n')

is_friend = False
is_user = True

if is_user and is_friend:
     print('best friend')

# Now short circuiting can be done when we use something like or, which we


if is_user or is_friend:
     print('best friend')

#  now or says if either one of these conditions are true, then
# run this piece of code.

# or - i only care if only one conditino is true 
# and - i have to evaluate both conditions but it happens a short circuite too 


###########################################################################
#                          LOGICAL OPERATORS
############################################################################
print('\n')
print('LOGICAL OPERATORS')
print('*'*20)
print('\n')

#   = is uset to assing a value to a variable 
#  == is used to compare things 

print(4 > 5)
print(4 < 5)
print(4 == 5)

print('a'>'b')
# # Each character has a value according to the ASCII table:
# 'a' = 97

# 'b' = 98

# 'A' = 65

# Which is why 97 > 98 returns false

print('a'>'A')

print(1<2>=3<4<5)
print(1 >= 0)
print(1 <= 0)
print(0 != 0)  # is 0 not equal to 0 

# and or not   keyword 

# not is also a function 

print(not(True))

print(not(False))

print(not(1==1))

###########################################################################
#                          IS  VS   ==
############################################################################
print('\n')
print('IS  VS   ==')
print('*'*20)
print('\n')


print(True == 1)
print('1' == 1)  # false , you are checking two types 
print([] == 1)
print(10 == 10.0)
print([] == [])


# is is a key work 
print('*'*20)
print('\n')

print(True is 1)
print(True is True)
print('' is 1)  
print([] is 1)
print([] is [])  #false becouse everytime we create a list is added in a locaiton in memory, so whenever we create a new list it`s added in another place in memory 
print(10 is 10.0)
print(10 is 10)
print([1,2,3,4] is [1,2,3,4])

# the diference is that IS actually checks if the location in memory for this value is the same 


###########################################################################
#                           LOOPS 
############################################################################
print('\n')
print('LOOPS')
print('*'*20)
print('\n')

# loops It allows us to run lines of code over and over and over.

# WE CREATE THEM USING THE KEYWORD  FOR 
# # key word . variable that we create we can name it whaterver 
# This is a variable and a variable is created here for each item after the.
# In so it's saying hey, for every item in zero two mastery, do something.

for item in 'Zero to Mastery':
    print(item)

# we call 'Zero To Mastery'
# An iterable is something that is able to get looped over.
# So an iterable allows us to use this notation of a for something in an iterable to iterate over each
# item.
#list
for item in [1,2,3,4,5,6]:
    print(item)

#set
for item in {1,2,3,4,5,65}:
    print(item)

#tuple
for item in (1,2,3,4,5,6):
    print(item)


print('*'*20)
print('\n')

# So for loops allow us to iterate over anything that has a collection of items
              # we are looping 6 times here 
# for item in (1,2,3,4,5,6):
#     print(item)

for item in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(item,x)

#prints 
# 1a
# 1b
# 1c
# 2a
# 2b
# 2c
# becouse when the program first run it`s saying i have 1 
#     print(1,a)  then it goes back to the second iterable becouse it still has value
#     print(1,b)
#     print(1,c)   ok i dont have more values on the second iterable , so move on the fist loop 
#     print(2 ,a) 
#     print(2 ,b)
#     print(2 ,c)  and so on and on 

###########################################################################
#                           ITERABLE
############################################################################
print('\n')
print('ITERABLE')
print('*'*20)
print('\n')


# So again, an iterable can be a list, can be a dictionary, can be a tuple, can be a set.
# It's a collection of items.

# Iterated -> means we can go one by one to check each item in the collection

user = {
    'name': 'Ardit',
    'age' : 27,
    'can_swim' : False
}
# return the tuple
for item in user.items():
    print(item)
# return the values 
for item in user.values():
    print(item)
# return the keys 
for item in user.keys():
    print(item)

print('*'*20)
# tuple unpacking 
for item in user.items():
    key,value = item  # im assinge what i have in the tuple
    print(key , value)

# the shortway of doing this is also 
for key, value in user.items():
    print(key,value)


# for item in 50:   # we canot iterat over one integer 
    print(item)



###########################################################################
#                           RANGE
############################################################################
print('\n')
print('RANGE')
print('*'*20)
print('\n')

# When looping in Python, one of the most common tools is this range function that we get out of the
# box with Python.
# And you see here that range well is a range object, a special type of object in Python that returns
# an object that produces a sequence of integers from start to stop.

print(range(100)) 

# I get range of 0 to 100.
# Hmm.
# So it looks like a tuple, but it's not.
# It's a range object.
# It's a special type of object.


# you see, besides tuples and lists and sets and dictionaries and strings, you can iterate over a range.


# So we want to send tend emails to an email list, for example.
 # -  i don`t care anout the variable i`m just trying to use range 
for _ in range(10):
        print ('email email list')


for _ in range(0,10,2):
    print(_)



# Well, range creates a special kind of object that we can iterate over.



for _ in range(10,0,-1):  # it`s descenting 
    print(_)

for _ in range(10,0 -2):
    print(_)

print('*'*20)
print('\n')
              # behing the scenes i will created a range anf i create a list then i looping that 10 times
for _ in range(10,0,-1):     # (10,9,8,7,6,5,4,3,2,1 )
    print(list(range(10)))   # [1,2,3,4,5,6,7,8,9]  10
                             # [1,2,3,4,5,6,7,8,9]   9
                             # [1,2,3,4,5,6,7,8,9]   8
                             # [1,2,3,4,5,6,7,8,9]   7
                             # [1,2,3,4,5,6,7,8,9]   6
                             # [1,2,3,4,5,6,7,8,9]   5
                             # [1,2,3,4,5,6,7,8,9]   4
                             # [1,2,3,4,5,6,7,8,9]   3
                             # [1,2,3,4,5,6,7,8,9]   2
                             # [1,2,3,4,5,6,7,8,9]   1


###########################################################################
#                           ENUMERATE
############################################################################
print('\n')
print('ENUMERATE')
print('*'*20)
print('\n')

# We wrap around something that, well, we want to enumerate, so let's see what that means.
# It returns an enumerate to object.
# So Iterable must be an other object that supports iteration.
# So we have to give it something that enumerate can iterate over.
                                        #Because we use enumerate, we get this eye or index of each item and where it is in the index.
for i,char in enumerate('Helllloooo'):  #indsex,range 
    print(i,char)                       # 0 H
                                        # 1 e
                                        # 2 l
                                        # 3 l
                                        # 4 l
                                        # 5 o
                                        # 6 o
                                        # 7 o
                                        # 8 o
                                        # 9 o
print('\n')
      # enumerate retunr the value and where that value is stored in memory
for _ in enumerate(['a','d','v']):
    print(_)
print('\n')
for _ in enumerate(('f','g','c','d')):
    print(_)



###########################################################################
#                          WHILE LOOP
############################################################################
print('\n')
print('WHILE LOOP')
print('*'*20)
print('\n')

# while loop is a little different in that we say while a condition is happening.
# Do something.

# i = 0
# while i < 50:   # 0 < 50
#    print(i)     # hey is 0 < 50 ? True
                  # print 0
                  # hey is 0 < 50 ? True
                  # print 0
# the logic behind is while the condition is True , return the printed value 
i = 0
# while i < 50:   # 0 < 50
#     print(i)    # 
#    i += 1       # i = 0 + 1
                  # 1 < 50
                  # i = 1 + 1
                  # 2 < 50..... 50 < 50  stop the loop condition False 

# So to jump out of a while loop, you can either turn the condition false or you can break out of the
# loop.

while i < 50:
    print(i)
    i += 1
    break
else:                                # this runs as soon as condiiton goes to false
    print('Done with all the work')


# So when should you use a while loop and when should you use a for loop?
# And it really depends on the problem you're trying to solve.
# For example, in a for loop I could do four item in let's say a list one, two, three.
# And just looking at this code, you know right away that it's going to be looped over three times.

# So when should you use a while loop and when should you use a for loop?

my_list = [1,2,3]

for item in my_list:   # this code is going to be looped over three times 
    print(item)
# we can do this in a while loop as well 

i=0
while i < len(my_list):  # while loops are more powerfull 
    print(my_list[i])
    i += 1               # we have to increment ti variable to not loop over and over


# For example, let's say we're trying to go through an email list that we've collected on a website,
# and for each email list, we want to send an email.
# Well, while the list is still there, let's just keep sending emails.
# There are many, many cases, but one of the most useful ways to use the while loop is like this.
# It's to say while.
# # True.
# Do something.
# And make sure that at the end we break.
 
# while True:
#     print('smth')   
#     break
print('\n')
#  while True:
#     input('say smth: ')   # But now we can do something powerful like input here.
   # if i remove break , i will keep asking me the same quesiton in infinity

# WE CAN USE CONDITIONAL LOGIC WITH WHILE LOOPS 
# while True:                               # im collecting whatever the responce is 
#    response = input('Say something: ')    # im asking the user to say smth :
#    if (response == 'bye'):                # any response = True , therfore repeat question.
#        break                              # when the user answer is = to condition 'bye'
                                            # the condition is set to True , move forward
                                            # read the other line , is Break , OK stop looping ! 
     
print('\n')
print('CAN WE BREAK IN FOR LOOPS')
print('\n')

for item in my_list:
    print(item)
    continue

print('\n')
print('*'*20)
print('\n')

i=0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue   # why do i need this ?

# we can use two other things besides break 
# 1 -  continue 
# 2 -  pass

i=0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass    # pass just pass it on the next line 


for item in my_list:   # when i have a loop 
 # thinking about it   # but in out code it not cleat what we wan`t to do with it 
  pass                 # and if we continiue coding and run the code , we gonna get an indendtatino Error 
                       # becouse the for loop is looking for something 
                       # so that`s where we use pass , to say move on with the next line 
                       # rarely used in production , mostly is used while developing smth 

