#Kieren Singh Gill
#11/03/2020
#Python Fall 2020, Section 1
#GillKieren_Assign7_problem1b.py


#import the string and random modules
import string
import random


#create the add_letters function
#word is the word to scramble, num is number of letters
def add_letters(word,num):
    #create a local variable to store the scrambled word
    #set it equal to nothing
    scrambled_word=''
    #create a for loop that iterates across the word to scramble
    for i in word:
        #add each character of the original word to the scrambled word
        #this acts similar to a counter, except it is concatenating string
        scrambled_word += i
        #create a second for loop
        #this loop will run for each character of the original word
        #this loop will iterate for the number of letters (num) to add after each character
        for j in range(num):
            #create a local variable called random_letter
            #the "random.choice" function returns a single, random element from a sequence
            #the "string.ascii_letters" function returns a string containing lower case and upper case letters
            random_letter =(random.choice(string.ascii_letters))
            #add the random letter to the scrambled word
            scrambled_word += random_letter

    #return the scrambled_word
    return scrambled_word


#create the remove_letters function
#word is the word to unscramble, num is number of letters
def remove_letters(word,num):
    #create a local variable to store the unscrambled word
    #set it equal to nothing
    unscrambled_word=''    
    #create a for loop that iterates across the word to unscramble
    #create a step so that it does not iterate across the random letters
    for i in range (0,len(word),num+1):
        #add the spliced characters together to form the unscrambled word 
        unscrambled_word += word[i]

    #return the unscrambled word
    return unscrambled_word



#create the shift_characters function
#word is the word to be shifted and num is the number of characters by which to shift the word
def shift_characters(word,num):
    #create a local variable to store the shifted word
    #set it equal to nothing    
    shifted_word=''
    #create a for loop that iterates across the word to be shifted    
    for i in word:
        #find the ascii value for each character using the ord function
        #shift the ascii value by the number we entered as num, we will have a new ascii value
        #obtain the shifted character by using the chr function with the new ascii value
        #add the shifted character to the shifted word variable
        ascii_value=ord(i)
        shift = ascii_value+num
        final_char = chr(shift)
        shifted_word+=final_char

    #return the shifted word
    return shifted_word


#make a continuous while loop
while True:
    #choice for user to input if they want to encode, decode or quit
    choice=input("(e)ncode, (d)ecode or (q)uit: ")
    #if the user chooses to quit
    #break the loop
    if choice == 'q':
        break

    #if the user chooses to encode
    if choice == 'e':
        #prompt user to input a number between 1 and 5
        user_number = (input("Enter a number between 1 and 5: "))

        #create a while loop
        #while the user number is not between 1 and 5
        #reprompt them
        #keep the input values as string so that an error message won't return if user inputs string        
        while user_number not in ['1','2','3','4','5']:
            user_number = (input("Enter a number between 1 and 5: "))

        #prompt user to enter a phrase
        #use add_letters function to add letters to the phrase
        #use shift_characters function to shift characters up
        #print the encoded word
        phrase = input("Enter a phrase to encode: ")
        added_phrase = add_letters(phrase,(int(user_number)))
        shifted_up = shift_characters(added_phrase,(int(user_number)))
        print("Your encoded word is:", shifted_up)
        print()

    #if the user chooses to decode
    if choice == 'd':
        #prompt user to input a number between 1 and 5
        user_number = (input("Enter a number between 1 and 5: "))

        #create a while loop
        #while the user number is not between 1 and 5
        #reprompt them
        #keep the input values as string so that an error message won't return if user inputs string        
        while user_number not in ['1','2','3','4','5']:
            user_number = (input("Enter a number between 1 and 5: "))
            
        #prompt user to enter a phrase
        #use remove_letters function to remove letters from the phrase
        #use the shift_characters function to shift characters down
        #print the decoded word    
        phrase = input("Enter a phrase to decode: ")
        shortened_phrase = remove_letters(phrase,(int(user_number)))
        shifted_down = shift_characters(shortened_phrase,-(int(user_number)))
        print("Your decoded word is:", shifted_down)
        print()        
