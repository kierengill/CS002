#Kieren Singh Gill
#10/12/2020
#Python Fall 2020, Section 1
#GillKieren_assign5_part2a.py


#create a variable to determine if a number is prime
prime = 0

#prompt user to enter a positive number
num = int(input("Enter a positive number to test: "))
print()

#create a while loop
#as long as user input is less than 1
#let user know their input is invalid
#prompt them to reenter input
while num < 1:
    print("Invalid number. Try again!")
    num = int(input("Enter a positive number to test: "))
    print()

#if the number entered is more than 1
if num > 1:
    #create for loop
    #to test if the number is prime
    #divide the user input by all the numbers in the range of 2 to the number itself
    for i in range(2,num):
        #if a number isn't a divisor of the user input
        #let the user know
        if (num%i)!=0:
            print(str(i),"is NOT a divisor of",num,"... continuing")
            #if the number has no divisors in the range
            #this means the number is prime
            #set the prime variable to 1
            prime=1

        #if a number is a divisor of the user input
        #let the user know
        #that means the user input isn't prime, so break the loop
        else:
            print(str(i),"is a divisor of",num,"... stopping")
            #set the prime variable to zero
            #because number isn't prime
            prime=0
            break

    print()

    #depending on the prime variable
    #let the user know if their input is prime or not 
    if prime ==1:
        print(num, "is a prime number!")
    else:
        print(num, "is not a prime number.")

#if the number is 1, let them know it isn't a prime number
else:
    print(num,"is not a prime number.")
