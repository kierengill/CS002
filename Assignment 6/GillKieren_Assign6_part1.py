#Kieren Singh Gill
#10/26/2020
#Python Fall 2020, Section 1
#GillKieren_Assign6_part1.py

#create the is_even function
def is_even(x):
    #if input is divisible by zero
    #it is even! so return True
    #otherwise, return False
    if (x % 2 == 0):
        return True
    else:
        return False
    
#create the is_odd function
def is_odd(x):
    #if input is not divisible by zero
    #it is odd! so return True
    #otherwise, return False
    if (x % 2 != 0):
        return True
    else:
        return False
    
#create the is_prime function
def is_prime(x):
    #create a for loop in the range of 2 to number before input value
    #test to see if input is divisible by all numbers in desired range
    #if input is divisible, it isn't prime
        #so return False
    #otherwise, it is prime!
        #so return True
    for i in range(2,x):
        if (x % i) == 0:
            return False
    else:
        return True

#create the is_perfect function
def is_perfect(x):
    #initialize counter to zero
    #create a for loop in the range of 1 to number before input value
    #test to see if input is divisible by all numbers in desired range
    #if input is divisible by i, i is a factor!
        #so add it the counter
    #if the counter is equal to the number itself
        #the number is perfect! so return True
    #otherwise, return False
    counter = 0
    for i in range(1,x):
        if (x % i) == 0:
            counter+=i
    if counter == x:
        return True
    else:
        return False


#create the is_abundant function            
def is_abundant(x):
    #initialize counter to zero
    #create a for loop in the range of 1 to number before input value
    #test to see if input is divisible by all numbers in desired range
    #if input is divisible by i, i is a factor!
        #so add it the counter
    #if the counter is more than the number itself
        #the number is abundant! so return True
    #otherwise, return False
    counter = 0
    for i in range(1,x):
        if (x % i) == 0:
            counter+=i
    if counter > x:
        return True
    else:
        return False

#starting number
#prompt user to input starting value
#convert it to an integer value
start = int(input("Enter starting number: "))

#create a while loop
#as long as the start number is less than 1
#let user know input is invalid
#prompt user to input start number again
while start < 1:
    print ("Invalid, try again")
    start = int(input("Enter starting number: "))

#ending number
#prompt user to input ending value
#convert it to an integer value
end = int(input("Enter ending number: "))

#create a while loop
#as long as the end number is less than the start number
#let user know input is invalid
#prompt user to input end number again
while end <= start:
    print ("Invalid, try again")
    end = int(input("Enter ending number: "))

#create a for loop
#for the numbers in the range of the starting to the ending number
#check if the numbers are even, odd, prime, perfect, and abundant
#if so, let user know!
#the end seperator is set to nothing, so a line break is only printed after each number
for i in range (start,end+1):
    print(i,"is ... ",end='')
    if (is_even(i)):
        print("even ",end='')
    if (is_odd(i)):
        print("odd ",end='')
    if (is_prime(i)):
        print("prime ",end='')
    if (is_perfect(i)):
        print("perfect ",end='')
    if (is_abundant(i)):
        print("abundant ",end='')
    print()
