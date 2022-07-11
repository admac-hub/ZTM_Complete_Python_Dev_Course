# built a counter 
# What I want you to do is using looping to loop over 
# this iterable list and sum up the total of the list.


my_list = [1,2,3,4,5,6,7,8,9,10] 

# for i in my_list:
#     print('c')
print(sum(my_list))   # i found my way was more simple 


counter = 0
for item in my_list:  # [1,2,3,4,5,6,7,8,9,10]
    counter = counter + item  #  0 +  1 
print(counter)                #  1 +  1
                              #  2 +  2
                              #  4 +  3 
                              #  7 +  4
                              # 11 +  5
                              # 16 +  6
                              # 21 +  7
                              # 28 +  8 
                              # 36 +  9
                              # 45 +  10
                              # print(55)

