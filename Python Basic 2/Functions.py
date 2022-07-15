###########################################################################
#                       FUNCTIONS  
###########################################################################
print('*'*40)
print('**********','FUNCTIONS','*******************')
print('*'* 40)
print('\n')

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
print('*'*40)
print('**********','ARGUMENTS VS PARAMETERS','*******************')
print('*'* 40)
print('\n')

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
print('*'*60)
print('**********','defautl ARGUMENTS & keywords PARAMETERS','*********')
print('*'* 60)
print('\n')

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
print('*'*60)
print('**********','RETURN','*********')
print('*'* 60)
print('\n')

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