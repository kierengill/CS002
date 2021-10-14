#Kieren Singh Gill
#10/12/2020
#Python Fall 2020, Section 1
#GillKieren_assign5_part2c.py

#prompt user to input start value
start=int(input("Start number: "))
#prompt user to enter end value
end=int(input("End number: "))

#create a while loop
#as long as the starting number or ending number is less than zero
#the loop will repeat

#as long as the end number is before the start number
#the loop will repeat
while (start <0 or end <0) or (end <= start):
    #if the start or end number is below zero
    #let user know input is invalid
    #prompt them to try again
    if start <0 or end <0:
        print("Start and end must be positive")
        print()
        start=int(input("Start number: "))
        end=int(input("End number: "))
        
    #if the start number is bigger than start number
    #let user know that end number must be bigger
    #prompt them to try again
    elif end <= start:
        print("End number must be greater than start number")
        print()
        start=int(input("Start number: "))
        end=int(input("End number: "))



print()
#create a variable to determine if a number is prime
prime=0

#create a for loop
#for numbers in the range of (start value) to (end value)
for num in range(start,end+1):
    #create a for loop
    #the iterator will be used to test if the number is prime
    #divide the number by the iterator
    for i in range(2,num):
        #if the number has no divisors
        #it is prime
        if (num%i)!=0:
            prime=1
            
        #otherwise
        #it isn't prime
        #break the loop so the next number can be tested
        else:
            prime=0
            break
    #if the number is prime
    #print the prime numbers out
    if prime ==1:
        print(num)

