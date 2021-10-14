#import time module
import time

#save the start time
time_start = time.time()

#create an empty dictionary
wordbank = {}

#open the movie review file
f = open('movie_reviews.txt', 'r')

#read the data and convert it to lowercase
data = f.read().lower()
#store the data in lines
lines = data.splitlines()

#close the file
f.close()

#forbidden characters (numbers and punctuation)
forbidden ="""1234567890!()-[]{};:'"\,<>./?@#$%^&*_~"""

#let user know that we are initializing sentiment database
print("Initializing sentiment database")

#create a for loop
#put the rating in a new counter
for line in lines:
    newline =line[0]
    #remove the forbidden characters by not adding them to the new counter
    for character in line:
        if character not in forbidden:
            newline +=character
    #replace the line in lines with the new line we created without the
            #forbidden characters
    n = lines.index(line)
    lines[n] = newline

#make a new empty list
newlines=[]
#split each line by ' ' to create a nested list of each line separated by words
for line in lines:
    x = line.split(' ')
    newlines.append(x)

#for each line in the newline list
    #if a word isn't in the wordbank dictionary
        #add it to the dictionary and store the rating as the value in a list
    #if a word is already in the dictionary
        #append the new rating to the value list
for line in newlines:
    for word in line[1:]:
        if word not in wordbank:
            wordbank[word] = [int(line[0])]
        else:
            wordbank[word].append(int(line[0]))

#remove \t from the wordbank
del wordbank['\t']

#save the end time
#compute how long it took to initialize the sentiment database
time_end = time.time()
timeDiff = time_end-time_start

#let user know the initialization is complete
#let user know total unique words, how long the analysis took
print("Sentiment database initialization complete")
print("Total unique words analyzed:",len(wordbank))
print("Analysis took", format(timeDiff,'.3f'),"seconds to complete")
print()

#let user input a test phrase and convert it to lowercase
test_phrase = input("Enter a phrase to test: ")
low_phrase = test_phrase.lower()

#remove forbidden characters from the test phrase and store it in
    #new phrase
new_phrase = ''
for character in test_phrase:
    if character not in forbidden:
        new_phrase+=character
        
#split up the new phrase
phrasewords = new_phrase.split(' ')

#iterate through the new phrase and obtain the values of:
    #how many times the word was repeated
    #the average rating of the word

#create an empty list for each word's average rating
#append each word's average rating to the list

#if the word doesn't exist in the wordbank, let the user know
rating = []
for word in phrasewords:
    if word in wordbank:
        length = len(wordbank.get(word))
        average = sum(wordbank.get(word))/length
        print("'"+word+"' appears", length ,"times with an average rating of",average)
        rating.append(average)
    else:
        print("'"+word+"'", "does not have a rating")


#let the user know if their phrase is positive or negative
if len(rating) > 0:
    average_rating = sum(rating)/len(rating)
    if average_rating >= 2:
        print("Average score for this phrase is:", average_rating)
        print("This is a POSITIVE phrase")
    else:
        print("Average score for this phrase is:", average_rating)
        print("This is a NEGATIVE phrase")
#if all words don't exist in the wordbank, let the user know
else:
    print("Not enough data to compute sentiment")
