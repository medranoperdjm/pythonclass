import sys

size = 5

def print_square(square):
    print("-"*(2*size))
    for y in range(len(square)):
       for x in range(len(square[y])):
           print("{:6}".format(square[x][y]), end="")
       print()
    print("-"*(2*size))


square = [[f"{x}.{y}" for x in range(size)] for y in range(size)]

print_square(square)
# I believe the code you provided was a tip on how to create the matrix, but I don't know what's wrong/missing in line 14
# I don't know how to code this, but I'll try to explain the steps
# after the matrix is created, I'd make each row into a array. you can probably store the arrays in a dictionary.
# in the first and last array I'd take the 1st and last indexes in each array, 2nd/2nd  to last arrays I'd take the 2nd and 2nd to last indexes, and keep doing that for the 501 by 501 array until you reach 1 ( the center of the matrix)
# after collecting all those numbers, you can sum all of the numbers up because those are your diagonal numbers
# you probably want to use some type of loop statment(s)