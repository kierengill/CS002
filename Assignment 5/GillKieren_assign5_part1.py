#Kieren Singh Gill
#10/12/2020
#Python Fall 2020, Section 1
#GillKieren_assign5_part1.py

#prompt user to input number of students
stu_class = int(input("How many students are in your class? "))

#create a while loop
#as long as the number of students is less than 1
#let user know there is an invalid number of students
#prompt user to try again
while stu_class < 1:
    print("Invalid # of students, try again.")
    print()
    stu_class = int(input("How many students are in your class? "))

#prompt user to input number of tests
num_tests = int(input("How many tests in this class? "))

#create another while loop
#as long as the number of tests is less than 1
#let user know there is an invalid number of tests
#prompt user to try again
while num_tests < 1:
    print("Invalid # of tests, try again.")
    print()
    num_tests = int(input("How many tests in this class? "))

#let the user know the program is starting!
print()
print("Here we go!")
print()

#create the variable for the counter for the total scores of everyone in the class
#set counter to zero
bigtotal=0

#create a for loop for all the students in the class
for students in range(1,stu_class + 1):

    #print the header
    print("**** Student #",students,"****",sep='')

    #create the variable for the counter for the total scores of each person
    #set it to zero
    total=0

    #create another for loop for all the tests
    for tests in range(1,num_tests + 1):
        #prompt user to enter score for their test
        score=int(input("Enter score for test #"+str(tests)+": "))
        #create a while loop
        #if the score is below zero or over 100, prompt user to reenter score
        while score < 0 or score > 100:
            print("Invalid score, try again")
            score=int(input("Enter score for test #"+str(tests)+": "))

        #counter for the total scores of each person
        total += score
        #counter for the total scores of everyone in the class
        bigtotal += score
        #average for each person
        avg = total/num_tests

    #print the average score for each student
    print("Average score for student #",students," is: ",'{0:.2f}'.format(avg),sep='')

    print()

#average for all the scores in the class
bigavg= bigtotal/(stu_class*num_tests)
#print the average scores for everyone in the class
print("Average score for all students is:",'{0:.2f}'.format(bigavg))
