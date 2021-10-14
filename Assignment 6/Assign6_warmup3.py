# write a function called 'simple_sort_version1' that accepts two values.
# you can assume
# that your three values will always be the same data type
# (all ints, all floats or all strings).
# sort these two values in ascending order and return them in that order. 
# you may use any function that you've written so far in this assignment
# if you'd like to (maximum, minimum, etc)

# your function should work perfectly with the following lines of code

def maximum (x,y,z):
    if x >= y and x >= z:
        return x
    if y >= x and y >= z:
        return y
    if z >= x and z >= y:
        return z    


def minimum (x,y,z):
    if x <= y and x <= z:
        return x
    if y <= x and y <= z:
        return y
    if z <= x and z <= y:
        return z


def middle (x,y,z):
    if (x >= y and x <= z) or (x >= z and x <= y):
        return x
    if (y >= x and y <= z) or (y >= z and y <= x):
        return y
    if (z >= x and z <= y) or (z > y and z <= y):
        return z


def simple_sort_version2(x,y,z):
    return minimum(x,y,z),middle(x,y,z),maximum(x,y,z)

# your function should work perfectly with the following lines of code
a,b,c = simple_sort_version2(10,20,30)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(10,30,20)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,10)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,20)
print (a,b,c) # 20 20 30
