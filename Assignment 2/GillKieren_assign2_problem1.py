#Kieren Singh Gill
#09/21/2020
#Python Fall 2020, Section 1
#GillKieren_assign2_problem1.py


#Print a description of the program and an empty line
print ("This program will project how much you can earn by investing money in a high-yield savings account over a 3 month period.")
print()

#Prompt user to input their starting balance and interest rate
start_bal = float(input("To begin, enter how much money you would like to initially invest (i.e. 500): "))
interest_rate = float(input("Next, enter your projected annual interest rate. For example, enter 5 for 5%: "))


#Calculations for monthly interest rates and ending balances
#Ending balances are reused as the next month's starting balance
interest1 = start_bal*(interest_rate/12/100)
end_bal1 = start_bal+interest1
interest2 = end_bal1*(interest_rate/12/100)
end_bal2 = end_bal1+interest2
interest3 = end_bal2*(interest_rate/12/100)
end_bal3 = end_bal2+interest3

#Format the variables to 2d.p. (float)
#Add characters behind them for formatting
f_start_bal = format (start_bal,'.2f')
f2_start_bal = format(f_start_bal, '<20s')

f_interest1 = format (interest1,'.2f')
f2_interest1 = format(f_interest1, '<10s')

f_end_bal1 = format (end_bal1,'.2f')
f2_end_bal1 = format (f_end_bal1,'<20s')

f_interest2 = format (interest2,'.2f')
f2_interest2 = format(f_interest2, '<10s')

f_end_bal2 = format (end_bal2,'.2f')
f2_end_bal2 = format (f_end_bal2,'<20s')

f_interest3 = format (interest3,'.2f')
f2_interest3 = format(f_interest3, '<10s')

f_end_bal3 = format (end_bal3,'.2f')


#Print the final output using the formatted variables
#Output shows monthly starting balance, interest rate, and ending balance
print()
print("------- Calculating --------")
print()
print("Month Starting Balance     Interest   Ending Balance")
print("1    ",f2_start_bal,f2_interest1,f_end_bal1)
print("2    ",f2_end_bal1,f2_interest2,f_end_bal2)
print("3    ",f2_end_bal2,f2_interest3,f_end_bal3)



