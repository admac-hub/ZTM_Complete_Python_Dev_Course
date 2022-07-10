###########################################################################
                          # VARIABLES#
###########################################################################

#Variables store information that can be used in our programs so we can hold perhaps user inputs
#maybe your date of birth in a variable.
#Variables are ways for us to store information on our computer.


# And let's say you just took the quiz and you found out that your IQ is 190 quite high.
# Good job, but we need to store that information somewhere.
# Well, we can do that with variables so that in Python, all we need to do is name it whatever you want.
# In our case, it will be IQ and we're going to say IQ equals 190.

from tkinter import N
from numpy import sometrue


IQ = 190

# And this IQ here is a variable.

#I can name it whatever i want 

sdfgwdopfg = 190 


print(IQ)       #i can use it in the program to call it with an action 
print(sdfgwdopfg)
#And if I do that and click run, you see that I can use IQ.


# Now, variables can also sometimes be called names.
# So this could be a name, for example.
# And assigning a value is also known as binding.
# That is, we're binding the value 190 to this variable so that when we request this variable later on
# in our program, our computer knows how to look for this information.
# It's going to say, Hey, I know what IQ is.
# I stored it somewhere in memory and it's going to go look for that.
# And because it's being bound to a value, it points to this value.
# 190 And remember, this number in memory gets stored as a binary representation in zeros and ones,


# But on top of just naming variables however we want, there is some best practices around variables
# of how you should write good variables.
# And as a matter of fact, these are specific rules that the Python community as a whole has that you'll
# just have to remember.
# So let's have a look at this variables and remember this is the symbol for best practices are what we
# call snake case.
# Snake gas means it's all lowercase and then spaces well they don't exist.
# We use underscores variables must start with a lowercase or an underscore.
# Variables can be anything with letters, numbers and underscores.
# But remember, they have to start with lowercase and underscore that means we can start a variable with
# a number.
# They're also case sensitive.
# That means if I create a variable, but let's say this snake case, this variable has a capital E instead
# of a lowercase E, they'll be a different variable.
# And then finally you can't overwrite keywords.
# Let's go through these with some examples.
# First, a variable has to be in the form of a snake case.
# That is, if I want to call this user IQ, I should technically have an underscore here instead of a
# space just to make sure that a programmer maybe I'm working on a team can read this variable.
# So that's snake case.
# You also have to start your variables with either a letter or an underscore so I can technically do
# this and I click run.
# Well, that's going to give me an error because I've changed a variable.
# So now in order to access that variable, you have to go like this.
# Now underscore in Python signifies a private variable, something that we'll go over later on in the
# course.
# But usually you're starting your variables with a letter and afterwards.
# Yeah, you can add numbers if you want in here.


user_iq = 190  #snake case 
print(user_iq)

#variables are case sensitive 

user_Iq = 190  
print(user_iq)  # WONT`T WORK 


iq = 190
user_age = 19/4
a = user_age


print(user_age)

print(a)


#constants never change in a program 
PI = 3.14 #capital letters are constant values never to be changes don`t touch it 

# Another type of variable that you're going to see and this is something like 
__file__   #it start with two __
# It doesn't look like I just did double underscore here, but it's two underscores and we call these
# dunder and as you can see here, we have some dunder variables that Python has.
# But the idea here is that these are meant to be left alone.
# You should not touch them.


a,b,c = 1,2,3
#And this simply is a way for us to rapidly assign values to variables multiple times.

############################################################################
                          # EXPRESSIONS# & #STATEMENTS#
############################################################################

iq = 100 #statement 
user_age = iq / 5 #expresion is a peace of code that produce a value 
#statement the line of code that perfom an action

############################################################################
                          # ARGUMENTED ASSIGNMENT OPERATOR #
############################################################################

some_value = 5
some_value = some_value + 2
some_value = some_value - 2
some_value = some_value * 2

print(some_value)

#But there's a neater way of doing this called augmented assignment operator.
some_value= 5
some_value += 2
some_value -= 2
some_value *= 2
print(some_value)

############################################################################
                          # IMMUTABILITY #
############################################################################
# What does immutability mean?
# Well, strings and python re immutable.
# That means they cannot be changed

numbers = '01234567'
          #01234567

# numbers[0] = '8'
print(numbers)

# I get an error, I get a typo error saying string object does not support item assignment.
# Why is that?
# Because strings are immutable.
# That is, I cannot change the value of this once it's created.
# I can just immediately change it to eight.
# One, two, three, four, five, six, seven.

numbers = numbers + '8'
print(numbers)





