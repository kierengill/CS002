#Kieren Singh Gill
#09/21/2020
#Python Fall 2020, Section 1
#GillKieren_assign2_problem4.py


#print the title of the mL Conversion Calculator
print("--------------------------------------------------------------")
print("		mL Conversion Calculator")
print("--------------------------------------------------------------")
print()


#prompt user to input ml for conversion
#store value as float
ml = float(input("How many mL would you like to convert? "))

#format ml value to 2d.p
f_ml = format(ml, '.2f')

#conversion calculations
tsp = ml*0.202884
tbsp = tsp/3
ul = ml*1000
nl = ml*1000000

#add comma separator and convert to 2d.p.
comma_tsp = "{:,.2f}".format(tsp)
comma_tbsp = "{:,.2f}".format(tbsp)
comma_ul = "{:,.2f}".format(ul)
comma_nl = "{:,.2f}".format(nl)

#justify the numbers to the right
f_tsp = format(comma_tsp, '>22s')
f_tbsp = format(comma_tbsp, '>20s')
f_ul = format(comma_ul, '>20s')
f_nl = format(comma_nl, '>21s')


#print the rest of the output to the user
#this will show the ml in teaspoons, tablespoons, microliters, and nanoliters
#units will be displayed as well
print (f_ml,"mL ...")
print()
print("... in teaspoons",f_tsp,"tsp")
print("... in tablespoons",f_tbsp,"tbsp")
print("... in microliters",f_ul,"uL")
print("... in nanoliters",f_nl,"nL")


#WAYS TO CRASH PROGRAM

#Value Error: Program will crash if you input a string when the 
#input in the file is stored as a float value. For example:
#ml = float(input("How many mL would you like to convert? "))
#If a user inputs a string value here, it will lead to a value error

#Syntax Error: Program will crash if I forget to delimit a string literal
#For example:
#print(How are you doing today?)
#This will lead to a syntax error

#Syntax Error: Program will crash if I have an indentation error
#For example:
#if dog==('4'):
#    print ("woof")
#    else:
#        print ("meow")
#This will lead to a syntax error

#Logic Error: This happens when the logic behind the algorithm is incorrect,
#but there are no syntax and runtime errors. For example, let's say I am
#trying to write a program to give me the difference between two numbers:
#number1 = 30
#number2 = 15
#difference = number1 + number2
#Here, the program will run fine, but I will not get the desired result.
#This is because I should have used the minus sign instead of the plus sign
#to obtain the difference


#Runtime Error: If I store data in a variable and misspell the variable later on,
#I will face a runtime error. For example:
#subtotal = input("Enter total value here:")
#tax = 0.2 * subTotal
#This will lead to a runtime error


