#Kieren Singh Gill
#11/03/2020
#Python Fall 2020, Section 1
#GillKieren_Assign7_problem2.py


#prompt user to enter 6 digit seed number
seed = input("Enter a six digit seed: ")

#create a while loop
#as long as the input isn't all digits or isn't 6 characters
#tell user input is invalid
#prompt user to input again!
while (str.isdigit(seed)== False) or (len(seed) != 6):
    print("Invalid seed, please try again")
    print()
    seed = input("Enter a six digit seed: ")

#prompt user to input start and end values
start = input("Enter lowest possible random integer: ")
end = input("Enter highest possible random integer: ")

#create a continuous while loop
#loop only breaks if certain conditions are met:
    #start and end values have to be numeric
    #end value has to be greater than start value
while True:
    if (str.isnumeric(start)) and (str.isnumeric(end))and((int(start))<(int(end))):
        break
    #if it doesn't meet the conditions
    #let user know their values are invalid
    #prompt them to try again
    else:
        print("Invalid low/high values, please try again.")
        print()
        start = input("Enter lowest possible random integer: ")
        end = input("Enter highest possible random integer: ")


#ask user how many random numbers they want to generate
print()
random_numbers = input("How many random numbers do you want to generate? ")

#create a continuous while loop
#loop only breaks if certain conditions are met:
    #value has to be a positive integer
while True:
    if (str.isnumeric(random_numbers)) and ((int(random_numbers))>0):
        break
    #if it doesn't meet the conditions
    #let user know their value is invalid
    #prompt them to try again
    else:
        print("Invalid, try again")
        print()
        random_numbers = input("How many random numbers do you want to generate? ")

print()


#define a middle square function
#function will use the seed value, start value, and end value as inputs
def middle_square(seed,start,end):
    #print seed value
    #convert seed to an integer
    #find the square of the seed, print it so the user knows
    print("Seed value:", seed)
    seed_int = int(seed)
    square = seed_int*seed_int
    print("Square of seed:", square)

    #find middle 6 digits of square
        #convert the square value to a string
        #find the length of the square
        #find the beginning of the middle 6 digits and the end of the middle 6 digits
        #use those values to slice the middle 6 digits
    square_str = str(square)
    length=len(square_str)
    start_middle = int((length/2)-3)
    end_middle = start_middle + 6
    middle_six = square_str[start_middle:end_middle]

    #calculate percentage
    #convert middle six digits to integer
    #show the user
    middle_six_int = int(middle_six)
    percentage = middle_six_int/999999
    print("Percentage =",middle_six+"/999999 =", percentage)

    #scale up to a number between the start and end values
    #for calculations, convert numbers in string format to integers
    #let user know
    scale = (int(end)-int(start))*percentage + int(start)
    print("Scaling up to a number between", start , "and", end)
    print("("+end+" - "+start+") *",percentage,"+",start,"=",scale)


    #convert to an integer
    #let user know
    #return the middle 6 digits to the user
    int_scale=int(scale)
    print("Converted to an integer:",int_scale)
    return middle_six

#create a for loop
#make the loop iterate for the number of random numbers we want to generate
#the loop will run the middle square function
#this will return the value of the middle 6 digits to be stored in the seed variable
#and the middle 6 digits will be used in the next iteration of the loop
for i in range(int(random_numbers)):
    seed = middle_square(seed,start,end)
    print()


#EXTRA CREDIT
#if repeated enough times, the middle-square method will either
    #begin repeatedly generating the same number
    #or cycle to a previous number in the sequence and loop indefinitely
#for example:
    #if we arrive at a number where the middle 6 digits of the square are all zeros
    #all subsequent numbers will be zeros again, and the random sequence gets stuck
#another example:
    #seed value is 776000,          square is 602(176000)000
    #next seed value is 176000,     square is 30(976000)000
    #next seed value is 976000,     square is 952(576000)000
    #next seed value is 576000,     square is 331(776000)000
    #next seed value is 776000
    #and the cycle repeats itself

#to improve the middle-square method
    #create a list which stores all previous seed values
    #verify that the new seed value isn't in the list
    #if new seed value is in the list, add a specified number to it(example: +1)
    #verify that new seed value isn't in the list
    #once new seed value isn't in the list, continue with the middle square method
