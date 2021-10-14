#Kieren Singh Gill
#11/23/2020
#Python Fall 2020, Section 1
#GillKieren_Assign10.py

#prompt user to search for a file to grade
filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")

#create a while loop which loops infinitely
while True:
    #try to open the file
    try:
        f = open(filename+'.txt' , 'r')
    #if the file doesn't exist, let the user know
    #reprompt the user
    except:
        print ("Sorry, I can't find this filename")
        print()
        filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
    #if it does exist, let the user know the file is successfully opened!
    #break the infinite while loop
    else:
        print("Successfully opened", filename+".txt")
        break

#read the lines in the file and split the lines
#the splitlines() function is different from the readlines() function
    #because the readlines() function has a \n at the back of each line
#i don't want the \n, so I'm using the splitline function
#close the file
lines = f.read().splitlines()
f.close()
#answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
#put the answerkey into a list instead of leaving it as string
answerkey = ["B","A","D","D","C","B","D","A","C","C","D","B","A","B","A","C","B","D","A","C","A","A","B","D","D"]

#the number of students are the number of lines
total_students =(len(lines))

#turn the list with all the data into a nested list
#for each element in the list
    #split it by ','
    #and make a separate list for each student
    #put all the student lists in a big list called student data
#nested list [[student_1,A,B,C,D],[student_2,A,B,C,D]]
student_data =[]
for i in lines:
    student = i.split(",")
    student_data += [student]

#create a counter for unusable lines
#create a for loop
#if a length of a student list is not equal to 26
    #the data is unsuable
    #add to counter
unusable = 0
for i in student_data:
    if len(i) != 26:
        unusable +=1

#create an empty list to store names and scores
#and another one only to store scores
scorelist = []
score_only = []

#create a for loop
#set scores to zero before the nested for loop starts
for student in student_data:
    scores = 0
    #create a for loop
    #if the data is usable (len(student) == 26)
        #if the scores match add 4 points
        #if the answer is blank add zero
        #if it is wrong -1 point
    for i in range(1,len(student)):
        if len(student) == 26:
            if student[i] == answerkey[i-1]:
                scores +=4
            elif student[i]=='':
                scores +=0
            elif student[i]!= answerkey[i-1]:
                scores -=1
                
    #if the data is usable (len(student) == 26)
        #append their score and their name to the scorelist list
        #append their score to the score_only list
    if len(student) == 26:
        scorelist.append([student[0],scores])
        score_only.append(scores)

#find the highest score
highest_score = max(score_only)
#find the lowest score
lowest_score = min(score_only)
#find the mean
#format to 2 decimal places
mean_score = format(sum(score_only)/len(score_only),'.2f')

#sort the scores in ascending order
ascending_scores = sorted(score_only)
#find the median
#if there is an even number of scores average the middle 2 scores
#otherwise take the middle score
if len(ascending_scores)%2 == 0:
    middle1 = ascending_scores[int(len(ascending_scores)/2-1)]
    middle2 = ascending_scores[int(len(ascending_scores)/2)]
    median = (middle1+middle2)/2
else:
    median = ascending_scores[int((len(ascending_scores)-1)/2)]

#find the range
range_final = highest_score-lowest_score

#to find the mode
#create an empty list
unique = []
#create a for loop
#if a number is unique add it to the list
for i in ascending_scores:
    if i not in unique:
        unique.append(i)
#create an empty list
seen = []
#make not of how many times each unique number is seen
for z in unique:
    counter = 0
    for y in ascending_scores:
        if z == y:
            counter +=1
    seen.append(counter)

#the mode is the number that is seen the most
#get the index number of the most frequently seen number
#and use that to find the corresponding number from the unique list
most = max(seen)
index = seen.index(most)
mode = unique[index]

#let user know the statistical indo
print()
print("Grade Summary:")
print("Total students:", total_students)
print("Unusable lines in the file:", unusable)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Mean score:", mean_score)
print("Median score:", median)
print("Mode:", mode)
print("Range:", range_final)

#EXTRA CREDIT! The CURVE
#ask the user if they would like to curve
to_curve = input("Would you like to curve the exam? 'y' or 'n': ")
#if the input isn't y or n
    #reprompt!
while (to_curve != 'y') and (to_curve != 'n'):
    print("Invalid input! Try again.")
    print()
    to_curve = input("Would you like to curve the exam? 'y' or 'n': ")

#if the user wants to curve
if to_curve == 'y':
    #ask the user what they want their new mean to be
    n_mean = (input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0): "))
    #if the user doesn't enter a number, reprompt!
    while not n_mean.isdecimal():
        print("Invalid input! Try again.")
        print()
        n_mean = (input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0): "))
    #convert user input to float
    new_mean = float(n_mean)
    #if the new mean isn't more than the old mean
    #let the user know and reprompt!
    while (new_mean < float(mean_score)) or (new_mean == float(mean_score)):
        print("Invalid curve, try again.")
        print()
        new_mean = float(input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0): "))

    #find the difference between the new mean and old mean
    difference = new_mean - float(mean_score)
    #add that difference to each current score and append it for each student in the scorelist
    for i in scorelist:
        new_val=i[1]+difference
        formatted_val = format(new_val,'.2f')
        i.append(formatted_val)
        
#if the user chose to curve            
if to_curve == 'y':
    #open the file
    newfile = open(filename+"_grades.txt","w")

    #create an empty string
    string = ''
    #concatenate the items in the scorelist into the empty string, including the new grades after curve
    for i in scorelist:
        for j in i:
            if i.index(j) == 0:
                x = str(j)
                string += x + ', '
            elif i.index(j) == 1:
                x = str(j)
                string += x + ', '
            else:
                x = str(j)
                string += x + '\n'
    #let user know that the program is done!
    print("Done! Check your grade file!")


else:
    #open the file
    newfile = open(filename+"_grades.txt","w")

    #create an empty string
    string = ''
    #concatenate the items in the scorelist into the empty string
    for i in scorelist:
        for j in i:
            if i.index(j) == 0:
                x = str(j)
                string += x + ', '
            else:
                x = str(j)
                string += x + '\n'
    #thank user for using the program
    print("Thank you for using the program!")

#write the string into the new file
#close the file
newfile.write(string)
newfile.close()
