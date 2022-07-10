###########################################################################
                          # MATRIX
###########################################################################
# A matrix is a way to describe a multidementinal list 
#usually are called matrix 
# And is an arrey with more than one array inside on it 

matrix = [
    [1,2,3],
    [3,4,5],
    [7,8,9]
]

# Well, it's a two dimensional array.
# We have the main array.
# And then we have sub arrays, three arrays to be exact.


# But why is this important?
# These type of matrices come up a lot in topics like machine learning or image processing.
# For example, a computer doesn't really know what a photo of a dog is.
# The only thing it understands is zeros and ones.
# So a lot of photos.
# For example, let's say we had a very simple photograph of a giant X, maybe this letter x.

image_of_x = [
    [1,0,1],
    [0,1,0],
    [1,0,1]
]


# Well, a computer can understand an image based on pixels on the screen, so maybe we can have zero,
# And if this represented, let's say, a tiny little pixel here or maybe a pixel here on my screen,
# the computer is going to say, oh, there's a one here.
# So that means I should make this green in this corner, then dark here, then green, then dark green,
# dark green, dark green.
# And a computer is able to draw, let's say, an X.
# And this is a simple example.


# But the reason I wanted to talk about this here is when you want to access a multi dimensional list,
# well, you would do something like this, let's say matrix.
# Access the first item.
# In The Matrix, which in this case will be this first array because it's the first item.

print(matrix[0][1])

# So it's accessing the first list in matrix.
# So it's going to look at the first order array, grab the first item which is right here, and then
# grab the second item in that array.
# So zero one, which is two.