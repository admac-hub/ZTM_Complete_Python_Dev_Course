
# def super_func(*args):       # use our star args to have a function that can accept any number of arguments.
#     print(args)
#     return sum(args)

# print(super_func(1,2,3,4,5,6))

# # What about **kwargs ?   this allows us yo use Allows us to use keyword arguments.
# def super_func(*args, **kwargs):       # *args is a parameter that is gettins his values from the arguments when invoking the function, & **kwargs allow as to grab any number in the kew workd and create a dictionary
#     total = 0
#     print(args)
#     print(kwargs)                    
#     for items in kwargs.values():      # our case we are looping over the values 
#         total += items                 # add the kewards values 
#     return sum(args) + total           # and here add all the valeus of args and kwargs 

# print(super_func(1,2,3,4,5,6, num1=5,num2=10))

# # *args -> can be anything it`s a variable that we created 
# # the standart is  *args &  **kwargs

# # Rule:  params , *args , default param , **kwargs 
# # if we want to define a function
# def ard_func(name,*args, i = 'hi', **kwargs):
#     pass

# print('\n')
# print('*'*60)
# print('\n')


a = 'heloooofdwedfo'

# if (( len(a)) >10):               
#     print(f"too long {len(a)} elements")

# with walrus 

# if ((n := len(a)) >10):               # i assign a value to the variable     
#     print(f"too long {n} elements")

print('*'*60)
print('\n')


while ((n:= len(a)) >1):
    print(n)
    a = a[:-1]