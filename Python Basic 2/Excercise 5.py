# Check for duplicates in list :



from multiprocessing.reduction import duplicate


some_list = ['a','b','c','b','d','m','n','n']


duplicates =[]                           # create an empty containter to dump the duplicates 
for value in some_list:                  # we wanna iterate over the list to we say that we have vaule in that list that we wana go through them 
     if some_list.count(value) > 1:      # .count() is a method that returns the number of how many times the value does axist in the list , so we are sayng if the value exist more the once 
         if value not in duplicates:     # and if that value is not in the duplicates containter 
             duplicates.append(value)    # dump those values there 


print(duplicates)                        # and tell me what values you dumped 
    
print(some_list.count(value))



