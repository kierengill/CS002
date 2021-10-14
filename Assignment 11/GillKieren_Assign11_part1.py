#open the movie reviews text file
f = open('movie_reviews.txt', 'r')

#read the file data and store it in lowercase
#split it by lines and store it as lines
#split it by spaces and store it as words
data = f.read().lower()
lines = data.splitlines()
words = data.split()

#close the file
f.close()

#prompt user to input a word to test and convert it to lowercase
test = input('Enter a word to test: ')
test_word =test.lower()

#create a counter and set it to zero
counter=0
#create a for loop that iterates throughout the words
#if the word is the same as the test word, add 1 to the counter
for i in words:
    if i == test_word:
        counter +=1

#create 2 different counters
#one for the sum of the ratings
#one for the number of reviews the word is in
total=0
new_counter=0

#create a for loop which iterates through each line
#if the test word is in each line, add the score of the rating to the total counter
#add 1 to the new_counter 
for line in lines:
    if ' '+test_word+' ' in line:
        rating = int(line[0])
        total +=rating
        new_counter+=1
        

#let user know how many times the test word has appeared
print("'"+test_word+"'",'appears',counter,'times')

#if the word has appeared before, the counter will not be zero
#if the counter is zero, let the user know there is no average score
#otherwise, let the user know the average score
if counter == 0:
    print('There is no average score for reviews containing the word',"'"+test_word+"'")
else:
    average = total/new_counter
    print("The average score for reviews containing the word","'"+test_word+"'","is",average)

#if the counter is zero, let the user know that the word can't be determined as
    #a positive or negative word
#otherwise, if the average is more than or equal to 2,
    #let user know that the word is positive
#if the average is less than 2,
    #let user know the word is negative
if counter ==0:
    print("Cannot determine if this word is positive or negative")
elif average >= 2:
    print("This is a positive word")
else:
    print("This is a negative word")

