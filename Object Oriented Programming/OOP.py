###########################################################################
#                           OOP
############################################################################
from asyncio.windows_events import NULL
from unittest import result

from tomlkit import value


def divide_content():
     print('\n')
     print('*'*60)
     print('\n')

def header(head_name):
    print('\n')
    print('*'*40)
    print('**********', head_name ,'*******************')
    print('*'* 40)
    print('\n')

header('OOP')

# OOP   # Everything in Python is an Object 
# and averything is an object becouse is build by the class key word 
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))


# Now, everything here is an object because in Python, everything is built by this class keyword.
# And we're able to use different methods on our objects like this to perform some actions on them.

# Objects have methods like these and attributes that you can access with the DOT method.


# how do we create an Object ?

# is by using the class key word 



# Let's say we're working for Amazon.
# And Amazon recently decides that, hey, you know what, we're going to have delivery drones that are
# going to deliver our customers packages a lot faster.
# But we need to code this drone, right?
# And up to this point, we've learned that we can do that with basic functions, conditional logic,
# and just writing our code on a dot pi file.
# But the problem is as code gets bigger and bigger and bigger.
# It's not just a one file.
# It's not just ten lines of code.
# It becomes hundreds and thousands and millions of lines of code divided into different files.
# Code gets more and more complicated because we live in a world where technology's everywhere, and programming
# something like a drone is quite complicated, especially when it's a delivery drone.
# So how can we use object oriented programming to make this code more manageable?
# Well, OP is what we call a paradigm.
# That is, it's a way for us to think about our code and structure our code in a way that is easier to
# maintain, extend and write.



# The main takeaway is that OP is a paradigm, a way to think about our code, a way for us to structure
# our code so that as it gets bigger and bigger, we're able to be organized because we're not writing
# silly ten line codes.
# We're writing millions and lines of codes.


###########################################################################
#                           OOP
############################################################################
header('oop 2')

#  the introduction of object oriented paradigms.
# This changed a bit.
# We started saying, Hey, let's model something in our code that represents a real world object.


# This idea of objects and modeling and we've seen this when we use the type, we see that everything
# is an object because we use this class keyword.
# But what is this class keyword in Python?
# I can create my own data, type my own class by simply saying class,

# crate object use camelcase 

class BigObject:
    pass

print(type(BigObject))
#  and then afterwards I can name
# it whatever I want.
# Let's say class Big Object

obj1 = BigObject()     

print(type(obj1))

# Now, a class is this.
# It's the blueprint.
# The blueprint of what we want to create.

#                  (action )
#  CLASS      ->   INSTATIANTE  ->   INSTANCES 
# BLUEPRINT   ->   STEPS        ->   OBJECTS 
# CAR DRAWING ->   FACTORY      ->   (NISAN), (BENZ), (Volkswagen)

# Hey, I just instantiated a class.
# It means, hey, I just created a new instance, a new object.


class BigObject:    #Class
    #Code
    pass

obj1 = BigObject()  #double barcket Instaciate the clas. use whatever you have coded and create a new object 

# The class is going to be stored in memory.
# So Python interpreter is going to say, hey, big object is going to be the blueprint for this.
# So I'm going to store all that code in memory.
# But every time I create an object, I don't have to rewrite the code or do anything like that.
# I can simply say, Hey, go in memory to where big object is and just run that code so that again we're
# keeping our code dry.


###########################################################################
#                           CREATING OBJECTS
############################################################################
header('CREATING OBJECTS')

# WE WANT TO CREATE A WIZARD FOR A GAMING COMPANY

# RULE  So player character, single in singular.

# #  __init__     => is a special method , dunder method 
# But when we're building a class, you usually see this at the top.
# And this is what's often called a constructor method or an init method.


class PlayerCharacter:                # CREATING A BLUEPRINT
    def __init__(self, name,age):         # Self refers to playercharacter , default param is slef 
        self.name = name              # i gave name to self ,  self referes to player1 or to whatever obj you wanna create 
        self.age = age


    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Ardit', 27)    # __main__.PlayerCharacter object at 0x0000000280CAB####

player2 = PlayerCharacter('Alkend',20)
player2.attack = 50


print(player1)
print(player2.attack)


###########################################################################
#                           ATRIBUTES & METHODS
############################################################################
header('ATRIBUTES & METHODS')

# Object oriented programming allows us to create objects that have their own methods, like run.
# And attributes. Properties.
# It's a great way to add more functionality to a language and mimic the real world.

# OOP Alow us to write code that is repeatable , well organised and memory efficient 


# In order to play this game, you have to have played or you have to have gotten a membership.

class PlayerCharacter:
    membership = True #Class Object Attribute / it`s not dynamic . it`s static / this it`s not going to change all the object will inherit this attribute 
    def __init__(self, name,age): 
        if (self.membership):     
            self.name = name          #atttibutes  , self keword to make the attributes dynamic
            self.age = age


    def shout(self):
        result = print(f'my name is {self.name} and my age is {self.age}')
        return result
    def run(self,hello):
        result =  print(f'my name is {self.name}')
        return result
    
#DECORATR

    @classmethod              
    def adding_things(cls,num1,num2):
        return cls('Teddy', num1 + num2)
 
    @staticmethod
    def add_things(num1,num2):
        return num1 + num2

player1 = PlayerCharacter('Ardit', 27)    

player2 = PlayerCharacter('Alkend',20)
player2.attack = 50

print(player1.run('helooo'))
print(player1.adding_things(2,3))

player3 = PlayerCharacter.adding_things(3,5)  # it`s a methond in the actual class
print(player3.age)
# all the objects that we instaciate will have access to it 

# help(player1)    # ---->  show`s the blue print of the object



###########################################################################
#                           ENCAPSULATION
############################################################################
header('ENCAPSULATION')

# 4 PILLARS OF OOP    
  # 1 - encapsualtion is the first one 

# Encapsulation is the binding of data and functions that manipulate that data.
# And we encapsulate into one big object so that we keep everything in this box that users or code or
# other machines can interact with.


class PlayerCharacter:               
    def __init__(self, name,age):          
        self.name = name               
        self.age = age
        

    def run(self):
        print('run')
        return 'done'

    def speak(self):
        print(f'my name is {self.name} and i am {self.age} years old')
        
    def greet(self):
        print(f'Welcome to the game {self.name}')


player1 = PlayerCharacter('Ardit', 27)   

player2 = PlayerCharacter('Alkend',20)
player2.attack = 50


print(player1)
print(player2.attack)

player1.speak()

player1.run()

player1.greet()

# the way you access info from the objest is by usiong .name or .age or .whatever yoy are tryuing to retrive
print(player1.name)
# Because of encapsulation, I have all this functionality available to me, all these methods that I
# can access so that if I do, let's say capitalize, it will capitalize all my strengths.
# I have all this functionality encapsulated for me to use.


# on a dictionary for example 

player4 = { 'name':'Alkend', 'age': 20}

# and the way i access the data is :
print(player4['name'])  


###########################################################################
#                           ABSTRACTION
############################################################################
header('ABSTRACTION')

