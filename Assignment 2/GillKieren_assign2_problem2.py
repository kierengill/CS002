#Kieren Singh Gill
#09/21/2020
#Python Fall 2020, Section 1
#GillKieren_assign2_problem2.py

#Prompt user to input number1 and number2
num1 = int(input("Enter a number between 0 and 999: "))
num2 = int(input("Enter another number between 0 and 999: "))

#To get the ones digit
#Perform the modulo operation on the number
ones_num1 = num1%10
ones_num2 = num2%10

#To get the tens digit
#Divide the number by 10 and convert it to an integer
#Then perform the modulo operation
tens_num1 = (int(num1/10))%10
tens_num2 = (int(num2/10))%10

#To get the hundreds digit
#Divide the number by 100 and convert it to an integer
#Then perform the modulo operation
hund_num1 = (int(num1/100))%10
hund_num2 = (int(num2/100))%10

#Calculate the sums of the ones, tens, and hundreds
sum_ones = ones_num1 + ones_num2
sum_tens = tens_num1 + tens_num2
sum_hund = hund_num1 + hund_num2

#Print the final output to the reader
#Show the sums of ones, sums of tens, and sums of hundreds
print("Sum of ones     =",ones_num1,"+",ones_num2,"=",sum_ones)
print("Sum of tens     =",tens_num1,"+",tens_num2,"=",sum_tens)
print("Sum of hundreds =",hund_num1,"+",hund_num2,"=",sum_hund)

