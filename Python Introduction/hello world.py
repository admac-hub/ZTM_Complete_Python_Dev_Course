from modulefinder import LOAD_CONST


print('hello world')

# What`s happening behing the scennes :
#interpreter convertions

# 0 LOAD_GLOBAL     0(print)
# 2 LOAD_CONST      1('hello world')
# 4 CALL_FUNCTION   1
# 6 POP_TOP
# 8 LOAD_CONST      0(None)
# 10 RETURN_VALUE



name = input('what is your name ?')
print('your name is:' ,name)

a = 'hello Ardit'   #give a value to the variable 
print(a)            # print the varaible 
