#Kieren Singh Gill
#09/28/2020
#Python Fall 2020, Section 1
#GillKieren_assign3_problem3.py


#The date is before the beginning of the semester (before Sep 1, 2020)
#The date is after the end of the semester (after Dec 10, 2020)

#Prompt the user to input a date in YYYYMMDD format
date = int(input("Enter a date in YYYYMMDD format (i.e. 20200128 for January 28th, 2020): "))

#isolate the values for the month
#isolate the values for the day
month = (date - (date//10000*10000))//100
day = (date - (date//100*100))


#if the day value is less than 1
#that is impossible in a calendar format
#let the user know it is not a valid date
if day < 1:
    print ("That's not a valid date!")


#we have 12 months in a year
#if the month value is less than 1 or more than 12
#that is impossible in a calendar format
#let the user know it is not a valid date
elif month > 12 or month < 1:
    print ("That's not a valid date!")

#the months January, March, May, July, August, October or December
#have 31 days
#if the value for day is more than 31 in these months
#that is impossible in a calendar format
#let the user know it is not a valid date
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day >31:
        print ("That's not a valid date!")

    #if the date is before the beginning of the semester (before Sep 1, 2020)
    #let the user know
    elif date < 20200901:
        print ("This date is before the semester begins")
            
    #if the date is after the end of the semester (after Dec 10, 2020)
    #let the user know    
    elif date > 20201210:
        print ("This date is after the semester ends")

    #if the date is on one of the class dates
    #let the user know they have class
    elif date == 20200903 or 20200908 or 20200910 or 20200915 or 20200917 or 20200922 or 20200924 or 20200929 or 20201001 or 20201006 or 20201008 or 20201013 or 20201015 or 20201020 or 20201022 or 20201027 or 20201029 or 20201103 or 20201105 or 20201110 or 20201112 or 20201117 or 20201119 or 20201124 or 20201126 or 20201201 or 20201203 or 20201208 or 20201210:
        print ("You have class today")

    #otherwise
    #let the user know they do not have class
    else:
        print("You do not have class today")


#the months April, June, September and November
#have 30 days
#if the value for day is more than 30 in these months
#that is impossible in a calendar format
#let the user know it is not a valid date
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day >30:
        print ("That's not a valid date!")

    #if the date is before the beginning of the semester (before Sep 1, 2020)
    #let the user know
    elif date < 20200901:
        print ("This date is before the semester begins")
            
    #if the date is after the end of the semester (after Dec 10, 2020)
    #let the user know    
    elif date > 20201210:
        print ("This date is after the semester ends")

    #if the date is on one of the class dates
    #let the user know they have class
    elif date == 20200903 or 20200908 or 20200910 or 20200915 or 20200917 or 20200922 or 20200924 or 20200929 or 20201001 or 20201006 or 20201008 or 20201013 or 20201015 or 20201020 or 20201022 or 20201027 or 20201029 or 20201103 or 20201105 or 20201110 or 20201112 or 20201117 or 20201119 or 20201124 or 20201126 or 20201201 or 20201203 or 20201208 or 20201210:
        print ("You have class today")

    #otherwise
    #let the user know they do not have class
    else:
        print("You do not have class today")    

#the month of February
#has 28 days
#if the value for day is more than 28 in February
#that is impossible in a calendar format
#let the user know it is not a valid date
elif month == 2:
    if day > 28:
        print ("That's not a valid date!")

    #if the date is before the beginning of the semester (before Sep 1, 2020)
    #let the user know
    elif date < 20200901:
        print ("This date is before the semester begins")
            
    #if the date is after the end of the semester (after Dec 10, 2020)
    #let the user know    
    elif date > 20201210:
        print ("This date is after the semester ends")

    #if the date is on one of the class dates
    #let the user know they have class
    elif date == 20200903 or 20200908 or 20200910 or 20200915 or 20200917 or 20200922 or 20200924 or 20200929 or 20201001 or 20201006 or 20201008 or 20201013 or 20201015 or 20201020 or 20201022 or 20201027 or 20201029 or 20201103 or 20201105 or 20201110 or 20201112 or 20201117 or 20201119 or 20201124 or 20201126 or 20201201 or 20201203 or 20201208 or 20201210:
        print ("You have class today")

    #otherwise
    #let the user know they do not have class
    else:
        print("You do not have class today")
