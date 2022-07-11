# Let's say that we want to create a script that
# enumerates a list of numbers one through ten.

from numpy import char


my_list = range(100)

for i, _ in enumerate(my_list):
    print(i,_)


# I want to know where 50 is in the list.

for i , _ in enumerate(range(100)):
    if _ == 50:
        print(f'index of 50 is {i}' )

