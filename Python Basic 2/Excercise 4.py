#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!

from cmath import pi
from email.mime import image

   
picture = [
  [0,0,0,1,0,0,0],  # image ['','','','i','','','']  \n
  [0,0,1,1,1,0,0],  # image ['','','i','i','i','','',] \n
  [0,1,1,1,1,1,0],  # image ['','i','i','i','i','i','',]
  [1,1,1,1,1,1,1],  # image ['i','i','i','i','i','i','i',]
  [0,0,0,1,0,0,0],  # image ['','','','i','','','',]
  [0,0,0,1,0,0,0]   # image ['','','','i','','','',]
]
# the best practice is to crate this two variables in case we are going to run multiple line`s of print 
fill = '$'
empty = ' '

def code():
    for image in picture:                 # image is lookin in list 
        for i in image:                   # we looking inside the list now / inside the image 
            if i:                         # if the value is true (1) we know 1 is true / so we are saying it you encounter a i == 1
                print(fill, end='')       # give the 1 the value == '*' / so why we use end='' parameter here ?
            else:                         # by deafult print(value, end='\n') end='\n' = move to new line when you encounter a true value , 
                print(empty,end="")       # in our case we have ['false','false','false','true','false','false','false',]
        print(end='\n')                   # so we don`t want that print to end in true we want to return the false values as well 
                                          # and print() in the end is saying , after you checked all te values in the first list , then start a new line 


# and ideally if we wan`t to run the same code multiple times we can simply wrap into a function and call the same funsction how many times we want 

i=0
while i < 6:
    code()   # calling the function 6 times // i wan`t 6 tree
    i += 1