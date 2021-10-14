#Kieren Singh Gill
#09/28/2020
#Python Fall 2020, Section 1
#GillKieren_assign3_problem2.py

#import the python random module
import random

#generate a random integer between 1 and 10 and assign it to the 'num' variable
num = random.randint(1,10)

#print a brief introduction
#prompt the user to guess a number between 1 and 10
#store user input as an integer
print("I'm thinking of a number between 1 and 10!")
guess = int(input ("What's your guess?: "))

#if the first guess is more than the random number
if guess > num:

    #let the user know their guess was too high
    #prompt the user to guess again
    print ("Too high, try again.")
    guess = int(input ("What's your guess?: "))        

    #if the second guess is more than the random number
    if guess > num:
        #let the user know their guess was too high
        #prompt the user to guess again
        print ("Too high, try again.")
        guess = int(input ("What's your guess?: "))

        #if the third guess is not equal to the number
        #let the user know their guess is incorrect
        #tell them the secret number
        if guess != num:
            print ("The secret number was ",num,".",sep='')
            print ("You didn't guess the number.")

        #if the third guess is equal to the number
        #let the user know their guess is correct
        #tell them the secret number
        #let the user know how many tries they took to guess the number (3)
        elif guess == num:
            print ("You got it!")
            print ("The secret number was ",num,".",sep='')
            print ("It took you 3 tries to guess the number.")


    #if the second guess is less than the random number
    elif guess < num:
        #let the user know their guess was too low
        #prompt the user to guess again
        print ("Too low, try again.")
        guess = int(input ("What's your guess?: "))

        #if the third guess is not equal to the number
        #let the user know their guess is incorrect
        #tell them the secret number
        if guess != num:
            print ("The secret number was ",num,".",sep='')
            print ("You didn't guess the number.")

        #if the third guess is equal to the number
        #let the user know their guess is correct
        #tell them the secret number
        #let the user know how many tries they took to guess the number (3)
        elif guess == num:
            print ("You got it!")
            print ("The secret number was ",num,".",sep='')
            print ("It took you 3 tries to guess the number.")
            
    #if the second guess is equal to the number
    #let the user know their guess is correct
    #tell them the secret number
    #let the user know how many tries they took to guess the number (2)
    elif guess == num:
        print ("You got it!")
        print ("The secret number was ",num,".",sep='')
        print ("It took you 2 tries to guess the number.")

#if the first guess is less than the random number    
elif guess < num:

    #let the user know their guess was too low
    #prompt the user to guess again
    print ("Too low, try again.")
    guess = int(input ("What's your guess?: "))        

    #if the second guess is more than the random number
    if guess > num:
        #let the user know their guess was too high
        #prompt the user to guess again
        print ("Too high, try again.")
        guess = int(input ("What's your guess?: "))

        #if the third guess is not equal to the number
        #let the user know their guess is incorrect
        #tell them the secret number
        if guess != num:
            print ("The secret number was ",num,".",sep='')
            print ("You didn't guess the number.")

        #if the third guess is equal to the number
        #let the user know their guess is correct
        #tell them the secret number
        #let the user know how many tries they took to guess the number (3)
        elif guess == num:
            print ("You got it!")
            print ("The secret number was ",num,".",sep='')
            print ("It took you 3 tries to guess the number.")
            
    #if the second guess is less than the random number       
    elif guess < num:
        #let the user know their guess was too low
        #prompt the user to guess again
        print ("Too low, try again.")
        guess = int(input ("What's your guess?: "))
        
        #if the third guess is not equal to the number
        #let the user know their guess is incorrect
        #tell them the secret number
        if guess != num:
            print ("The secret number was ",num,".",sep='')
            print ("You didn't guess the number.")
            
        #if the third guess is equal to the number
        #let the user know their guess is correct
        #tell them the secret number
        #let the user know how many tries they took to guess the number (3)
        elif guess == num:
            print ("You got it!")
            print ("The secret number was ",num,".",sep='')
            print ("It took you 3 tries to guess the number.")
            
    #if the second guess is equal to the number
    #let the user know their guess is correct
    #tell them the secret number
    #let the user know how many tries they took to guess the number (2)
    elif guess == num:
        print ("You got it!")
        print ("The secret number was ",num,".",sep='')
        print ("It took you 2 tries to guess the number.")


#if the second guess is equal to the number
#let the user know their guess is correct
#tell them the secret number
#let the user know how many tries they took to guess the number (1)
elif guess == num:
    print ("You got it!")
    print ("The secret number was ",num,".",sep='')
    print ("It took you 1 try to guess the number.")
