#Kieren Singh Gill
#10/12/2020
#Python Fall 2020, Section 1
#GillKieren_assign5_part2b.py

#create a variable to determine if number is prime
prime=0

#let user know 1 isn't a prime number
print("1 is technically not a prime number.")

#create a for loop
#for numbers in the range 2 to 1000
for num in range(2,1001):
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
    #let the user know
    if prime ==1:
        print(num, "is a prime number!")
