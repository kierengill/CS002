#Kieren Singh Gill
#10/06/2020
#Python Fall 2020, Section 1
#GillKieren_assign4_part1.py

#Number of sticks
stick_num=int(input('How many sticks (10-100)? '))


#While the number of sticks is outside 10-100
#Continue looping
#Let user know if the number of sticks is too high or too low
#Ask the user to input the number of sticks again
while stick_num < 10 or stick_num > 100:
    if stick_num < 10:
        print("Sorry, that's too few sticks. Try again.")
    else:
        print("Sorry, that's too many sticks. Try again.")
    stick_num=int(input('How many sticks (10-100)? '))


#Once the number of sticks is inside the desired range
#Carry on with the program
print("Great! Let's play ...")
print()

#Print the number of sticks on the table
#Ask user how many sticks they want to take
print("There are", stick_num , "sticks on the table.")
take_sticks=int(input('How many sticks do you want to take (1, 2 or 3)? '))

#While the number of sticks to take is out of the range 1-3
#Continue looping
#Let the user know number isn't valid
#Ask the user to input a new number
while take_sticks > 3 or take_sticks < 1:
    print("Sorry, that's not a valid number.")
    print()
    print("There are", stick_num , "sticks on the table.")
    take_sticks=int(input('How many sticks do you want to take (1, 2 or 3)? '))

#While the number of sticks to take out is in the range 1-3
#Continue looping
while take_sticks in range(1,4):
    #create a new variable to keep track of the remaining number of sticks
    #number of sticks = previous number of sticks - sticks removed
    stick_num = stick_num - take_sticks

#now, depending on the number of sticks left, there are a few different outcomes for the program

    #if the number of sticks is more than 1
    #let the user know how many sticks remaining
    if stick_num > 1:
        print()
        print("There are",stick_num, "sticks on the table.")
        
    #if the number of sticks is 1
    #let the user know how many sticks remaining
    elif stick_num == 1:
        print()
        print("There is",stick_num, "stick on the table.")

    #if the number of sticks is below zero
    #tell the user, and tell them that they should try again
    elif stick_num < 0:
        print("Sorry, that would bring the total # of sticks below 0. Try again.")
        print()
        #add the deducted value back to return to the number of sticks before it went below zero
        #let the user know how many sticks are remaining
        stick_num = stick_num+take_sticks
        #if the number of sticks is more than 1
        #let the user know how many sticks remaining
        if stick_num > 1:
            print("There are",stick_num, "sticks on the table.")
        #if the number of sticks is 1
        #let the user know how many sticks remaining
        elif stick_num == 1:
            print("There is",stick_num, "stick on the table.")
    #if the number of sticks is zero
    #break the loop
    elif stick_num == 0:
        break

    #Ask the user how many more sticks they would like to take
    take_sticks=int(input('How many sticks do you want to take (1, 2 or 3)? '))

    #While the number of sticks to take is out of the range 1-3
    #Continue looping
    #Let the user know number isn't valid
    #Ask the user to input a new number
    while take_sticks > 3 or take_sticks < 1:
        print("Sorry, that's not a valid number.")
        print()
        #if the number of sticks is more than 1
        #let the user know how many sticks remaining
        if stick_num > 1:
            print("There are",stick_num, "sticks on the table.")
        #if the number of sticks is 1
        #let the user know how many sticks remaining
        elif stick_num == 1:
            print("There is",stick_num, "stick on the table.")
        take_sticks=int(input('How many sticks do you want to take (1, 2 or 3)? '))

#once the number of sticks is zero, the loop should be broken
#Let the user know the game is over!
print()
print('There are no sticks left on the table!  Game over.')
