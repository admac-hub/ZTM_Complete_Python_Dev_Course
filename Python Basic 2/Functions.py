###########################################################################
#                       FUNCTIONS  
###########################################################################

from email.header import Header

from requests import head


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

header('functions')

# def  - we are going to defin a functino

# We use the same naming case as we do with variables to define our functions.
# So let's create a function again.
# We'll call it Say Hello.
# Just a variable that I created.
# But this time it's a function because we use the def keyword now in here and say hello.
# We also add the brackets to let the interpreter know that this is something that we're going to take\
# action on or this is going to perform an action on a data type.
# We use the colon and then within this block of code, we can say print.

def say_hello():
    print('hello world')    # if we run it now , nothing print`s . untill now we just created this function in memory 

say_hello()                 #However, in order to use a function, remember, just like we use the print function, we have to call it with the brackets.


# why functions are powerfull is becouse of DRY - do not repeat yourself


# But if in our program we want to say hello multiple times and you can imagine this actually being a
# lot more complicated, maybe ten lines of code.
# Instead of writing those ten lines of code over and over, I can just define it as a function and use
# it anywhere I want in my program.


picture = [
  [0,0,0,1,0,0,0],  # image ['','','','i','','','']  \n
  [0,0,1,1,1,0,0],  # image ['','','i','i','i','','',] \n
  [0,1,1,1,1,1,0],  # image ['','i','i','i','i','i','',]
  [1,1,1,1,1,1,1],  # image ['i','i','i','i','i','i','i',]
  [0,0,0,1,0,0,0],  # image ['','','','i','','','',]
  [0,0,0,1,0,0,0]   # image ['','','','i','','','',]
]

fill = '$'
empty = ' '

def tree():  # when you create a function , identation is important , whatever is indetet here is part of that function
    for image in picture:                 # image is lookin in list 
        for i in image:                   # we looking inside the list now / inside the image 
            if i:                         # if the value is true (1) we know 1 is true / so we are saying it you encounter a i == 1
                print(fill, end='')       # give the 1 the value == '*' / so why we use end='' parameter here ?
            else:                         # by deafult print(value, end='\n') end='\n' = move to new line when you encounter a true value , 
                print(empty,end="")       # in our case we have ['false','false','false','true','false','false','false',]
        print(end='\n')

print(tree)  # < function tree at 0x0000001f34######    this prit give`s me the location where my functino is stored in memory 

# we want to run the christmas tree multiple times 
tree()
tree()
tree()



###########################################################################
#                       ARGUMENTS VS PARAMETERS   
###########################################################################
header('ARGUMENTS VS PARAMETERS')

# The power of functions beyond just being able to call this multiple times because it only lives in one 
# location in memory is this ability for us to make it dynamic?
# For example, in these brackets I can give it what we call parameters.
# So in here we give it parameters.
# Inside of the bracket.

#def say_hello(parameters):
                                     # paramenters are variable that we just made up & we can give as many parameters as we want 
def say_hello(name, emmoji):    #PARAMETERS
    print(f'hello {name} {emmoji}')             # we will be able to use this variables inside this function
#DEFINE

# this parameters allow was to give the functino when we call it some arguments 
# Arguments are used as the actual values we provide to a function.
say_hello('Ardit',':)')  #ARGUEMENTS    # this function is able to revive this two paramters 
#CALL    OR INVOKE                      # say_hello(name,emoji)  

# Argumemnts are the actual values that we give to the function 

# Now, these arguments are the actual value we provide to the function and the name of the variables that we use that
# we receive are called parameters.
# So parameters are used when we define the function and arguments are used when we call the function.
# Define and call.
# And by the way, some people also like saying call or invoking the function or invoke the function.



# And this is a when functions get really powerful because we're able to not just make generic functions
# that always do the same thing, but we can create functions that do things based on what parameters
# we give it.
# Or what arguments we call it with.
# So that now I can use the say hello function to say hello to my friend Dan and also my friend Emily.

say_hello('Anxhela', '<3')
say_hello('Alkend', '<3')




# if we're designing a game, well, we've just used this to greet our users.
# And based on the user name, I can use the same function over and over.

###########################################################################
#                       defautl ARGUMENTS & keywords PARAMETERS   
###########################################################################
header('defautl ARGUMENTS & keywords PARAMETERS')

# default parameters
def say_hello(name='user001fm', emmoji='(^^^)'):    #PARAMETERS
    print(f'hello {name} {emmoji}')             

# positional arguements      # becouse the position matters how they are defined in the function 
say_hello('Ardit')

# however there is smth that is called a key word argument , that allow us not to worry mutch for the position

say_hello(':)','Aristir')   # now becouse i used the keyword i`m saying i want the emoji to be this and the name to be this 
say_hello(emmoji='<3', name='asdfas')
# the best practice is to use the code flow and keep it standart 

say_hello()  # now as we defined the default parameters values if invoke this code with no arguments i get in return the defaul parametes value 
say_hello('Toby')


###########################################################################
#                       RETURN
###########################################################################
header('RETURN')

# Return It's a key word in Python that we are going to see a lot when working with functions.

def sum(num1,num2):
    return num1 + num2  # I want you to exit this function. And when you exit this function, I want you to return whatever this expression gives us.
  
sum(4,5)                # Return empty field
print(sum(4,5))         # Return None 


# functinos they allways have to return smth and if they don`t have anything to return it will return none 

# So a function either modifies something in our program or returns something.

[2,3,4,5].clear()

# the rule of thumb with the functions is 
# Should do one thing really well 
# Should return something 

total = sum(10,4)   #  I want a variable total and I want that total variable to equal some ten five.

print(sum(10,total))

                                   # i know what sum is , you defined i`m going to keep it in memory
# def sum(num1,num2):              # hey num1 = 10, hey num2 = 5 now 
#      return num1 + num2          # hey i want you to add 10 + 5 and return 

# total = sum(10,5)                # calling sum , done calling sum it`s says ok now assingn the returned value to the variable total 
# print(sum(10,total))             # hey i want to print something . i want to print sum ! i know what sum is i have it in memory so num1 = 10 , num2 = total 
                                   # total ?  hmmm , oh yeah i have it in memory it`s 15 
print('\n')

def sum(num1,num2):
    def another_func(num1, num2):
      return num1 + num2
    return another_func
total = sum(10,20)
print(total)



###########################################################################
#                       METHOD VS FUNCTIONS
###########################################################################
header('METHOD VS FUNCTIONS')
# Functions 
# list()
# print()
# max()
# min()
# input()

# in python we have this build in functions that we use 
# but we also can create our functions 

def do_nothing():
    pass



# But we also learned about methods and methods were different because the way we use them was using the
# dot notation.

# We said dot something for example, if we had a string.
# Hello?
# And I do dot.

'hello'.capitalize


# Methonds has to be owned by something 

# whatever is to the left of .dot  
# in our case the string own the method capitalize 


# And that's what methods are.
# They're built in objects that have methods such as strings, dictionaries, sets, tuples, all the
# They're owned by an object or a data type.

# But at the end of the day, both methods and functions allow us to take actions, right, to take actions
# on our data types, to have our programs do something.

###########################################################################
#                       DOC STRINGS
###########################################################################
header('DOC STRINGS')

def test(a):           # this is called doc strings
    '''         
    Info 4 the functinon ,this function prints param a 
    '''
    print(a)

# test("!!!!!!!")   

#test()     # coment inside the functions to be able to document what the function does to be able to find inforamtion later on

# help(test)  # we can use help to find out what a function does

# print(test.__doc__)  #One other way to do this is to use what we call a magic method or a dunder method,


# This is a very usefull feature becouse now you can document the porpuse of your functions 

###########################################################################
#                       Clean Code
###########################################################################
header('Clean Code')

def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False

print(is_odd_or_even(5))

print('\n')
# how can we clean this code 

def is_odd_or_even(num):   # we have a bolean expression that is evaluatin true or false 
    return num % 2 == 0    # and we know that return expression evalute is it`s true or if it`s false
                           # this way we cleaned our code 

print(is_odd_or_even(5))

###########################################################################
#                       Args & Kwargs
###########################################################################
header('Args & Kwargs')

# from ast import arg

# def super_func(*args):
#     print(args)
#     return sum(args)

# print(super_func(1,2,3,4,5,6))

###########################################################################
#                       Walrus 
###########################################################################
header('WALRUS')
# walrus is an antique animal := 

# Now let's just focus on the walrus operator because it is useful and also kind of fun to learn about

# Now let's just focus on the walrus operator because it is useful and also kind of fun to learn about
# what this new syntax does is it assigns value to variables as part of a larger expression.\
# So usually you use it in an expression when something is being evaluated like in an if statement may
# be a while statement.

# we are going to use this in a statement usually when something is going to be evaluated 

a = 'heloooofdwedfo'

if (( len(a)) >10):               
    print(f"too long {len(a)} elements")

# with walrus 

if ((n := len(a)) >10):               # i assign a value to the variable     
    print(f"too long {n} elements")



divide_content()


while (( n:=len(a)) >1):
    print(n)
    a = a[:-1]

print(a)

# There you have it, the walrus operator.
# You might not see it a very often.
# It's essentially a way for us to minimize doing calculations that are similar, let's say, inside of
# an if statement or a wall statement where we want to do something based on a condition and then calculate
# that value again


###########################################################################
#                       SCOPE 
###########################################################################
header('SCOPE')

# Scope - what variables do i have access to ?
# if i run the below code 
# print(name())
# i get an error name id not defined , becouse it doesn`t exist

# this error is becouse of scope
# Or variable is not defined here and scope in python has what we call functional scope or function scope.

# python interpreter says , hey what do i have access to ? do i have access to name ? if not return an error

total = 1000    #global scope (global variable) means anyone in the files has access to this varibale , i can use it anywhere inside a condition or inside a loop 

def some_func():
    allval = 100
          
# print(allval)     # i will get an errorr becise the variable is not global 


# So think of scope as a new world that we create.
# In our case, when we create a function, we create a new world that anything that's indented inside
# of the function is its own world that we don't really have access to.
# We can only use total if we indent print.
# And it's part of this world.
# That's what scope is.

if True: 
    x = 10
print(x)

###########################################################################
#                       SCOPE  rules
###########################################################################
header('SCOPE')

# Global variable / indentation of nothing , whatever the file has that`s that`s global 

a = 1
def parent():
    a =10
    def confusion():
        return a 
    return confusion

print(a)
print(parent())

# what is defined inside the function is another universe , another world , another timeLine

# the rules are 

# 1- Start with local .... Hey does confusion know where a is ?  
# 2 - Paret locat     .... Hey parert do you have a ?
# 3 - Global          .... Hey File do you have a ?  
# 4 - Built in python .... Hey Python do tyou have a in your libraries ?

###########################################################################
#                       Global KeyWords
###########################################################################
header('Global KeyWords')

a = 10

def confusion(b):
    print(b)
    a = 90

confusion(300)

divide_content()


total = 0
def count():
    global total    # to be able to use a global variable we need to use the key word global 
    total += 1
    return total

print(count())

divide_content()

# A better way of Coding is something called dependency injection 


# But the idea is that instead of accessing variables outside of the function like this, which can get
# really, really complicated as files get bigger and bigger, is to do instead.
# This.
# Total.
# Like this, we create a parameter and then we pass in that parameter.
# Or argument in here.

total = 0
def count(total):
    total += 1
    return total

print(count(total))
print(count(count(count(total))))

###########################################################################
#                       NONLOCAL KEYWORD
###########################################################################
header('NONLOCAL KEYWORD')

def outer():
    x = 'local'
    def inner():
        nonlocal x             # this keyword is used to refered to the paret local
        x = 'nonlocal'         # i wan`t to use a variable that is outside of my local scope 
        print("inner:",x)
    
    inner()
    print("outer:", x)

outer()


divide_content()


def outer():
    x = 'aborm'
    def inner():
        nonlocal x             # this keyword is used to refered to the paret local
        x = 'lura'         # i wan`t to use a variable that is outside of my local scope 
        print("inner:",x)
    
    inner()
    print("outer:", x)

outer()

print(x)     # --->  this will not run , becouse in python after you done with a function , python destroyied that from his memory 
# That`s why the scpope is useful
#                  AVOID USING THIS // MAKE THE CODE PREDICTIBLE AND CLEAN 

