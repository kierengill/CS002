#Kieren Singh Gill
#11/03/2020
#Python Fall 2020, Section 1
#GillKieren_Assign7_problem3.py


#define string_length function
def string_length(string):
    #set up a counter and make it equal to zero
    counter = 0
    #set up a for loop
    #the loop will iterate across each character of the string
    #and will add 1 to the counter for each character
    for i in string:
        counter+=1
    #return the value of the counter
    return counter

#define string_isalpha function
def string_isalpha(string):
    #if there is an empty string, return False
    if string == '':
        return False
    
    #set up a counter and make it equal to zero
    counter = 0
    #set up a for loop
    #the loop will iterate across each character of the string
    #and will add 1 to the counter for each character that isn't in the list, and break the for loop
    #the list contains a-z, A-Z
    #if a character is in a-z, A-Z, 0 is added to the counter
    for i in string:
        if i not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            counter += 1
            break
        else:
            counter+=0
    #if the counter isn't equal to zero
        #return False
    if counter !=0:
        return False
    #otherwise
        #return True
    else:
        return True


#define string_isupper function
def string_isupper(string):
    #if there is an empty string, return False
    if string == '':
        return False
    #set up a counter and make it equal to zero
    counter = 0
    #set up a for loop
    #the loop will iterate across each character of the string
    #and will add 1 to the counter for each character that isn't in the list, and break the for loop
    #the list contains A-Z
    #if a character is in A-Z, 0 is added to the counter
    for i in string:
        if i not in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            counter += 1
            break
        else:
            counter+=0
    #if the counter isn't equal to zero
        #return False
    if counter !=0:
        return False
    #otherwise
        #return True
    else:
        return True


#define string_isdigit function
def string_isdigit(string):
    #if there is an empty string, return False
    if string == '':
        return False
    #set up a counter and make it equal to zero
    counter = 0
    #set up a for loop
    #the loop will iterate across each character of the string
    #and will add 1 to the counter for each character that isn't in the list, and break the for loop
    #the list contains A-Z
    #if a character is in A-Z, 0 is added to the counter
    for i in string:
        if i not in ['1','2','3','4','5','6','7','8','9','0']:
            counter += 1
            break
        else:
            counter+=0
    #if the counter isn't equal to zero
        #return False
    if counter !=0:
        return False
    #otherwise
        #return True
    else:
        return True


#define string_swapcase function
def string_swapcase(string):
    #create a variable to store the swapped string
    #make it empty
    swapped = ''
    #create a for loop that iterates across the string
    #if i is a lowercase character, add the uppercase version of the character to the 'swapped' variable
    #and vice versa for uppercase characters
    #if there are any other characters that aren't letters, just add them to the 'swapped' variable
    for i in string:
        if i == 'a':
            swapped += 'A'
        elif i == 'b':
            swapped += 'B'
        elif i == 'c':
            swapped += 'C'
        elif i == 'd':
            swapped += 'D'
        elif i == 'e':
            swapped += 'E'    
        elif i == 'f':
            swapped += 'F'
        elif i == 'g':
            swapped += 'G'
        elif i == 'h':
            swapped += 'H'
        elif i == 'i':
            swapped += 'I'
        elif i == 'j':
            swapped += 'J'
        elif i == 'k':
            swapped += 'K'
        elif i == 'l':
            swapped += 'L'
        elif i == 'm':
            swapped += 'M'
        elif i == 'n':
            swapped += 'N'
        elif i == 'o':
            swapped += 'O'
        elif i == 'p':
            swapped += 'P'
        elif i == 'q':
            swapped += 'Q'
        elif i == 'r':
            swapped += 'R'
        elif i == 's':
            swapped += 'S'
        elif i == 't':
            swapped += 'T'
        elif i == 'u':
            swapped += 'U'
        elif i == 'v':
            swapped += 'V'
        elif i == 'w':
            swapped += 'W'
        elif i == 'x':
            swapped += 'X'
        elif i == 'y':
            swapped += 'Y'
        elif i == 'z':
            swapped += 'Z'
        elif i == 'A':
            swapped += 'a'
        elif i == 'B':
            swapped += 'b'
        elif i == 'C':
            swapped += 'c'
        elif i == 'D':
            swapped += 'd'
        elif i == 'E':
            swapped += 'e'    
        elif i == 'F':
            swapped += 'f'
        elif i == 'G':
            swapped += 'g'
        elif i == 'H':
            swapped += 'h'
        elif i == 'I':
            swapped += 'i'
        elif i == 'J':
            swapped += 'j'
        elif i == 'K':
            swapped += 'k'
        elif i == 'L':
            swapped += 'l'
        elif i == 'M':
            swapped += 'm'
        elif i == 'N':
            swapped += 'n'
        elif i == 'O':
            swapped += 'o'
        elif i == 'P':
            swapped += 'p'
        elif i == 'Q':
            swapped += 'q'
        elif i == 'R':
            swapped += 'r'
        elif i == 'S':
            swapped += 's'
        elif i == 'T':
            swapped += 't'
        elif i == 'U':
            swapped += 'u'
        elif i == 'V':
            swapped += 'v'
        elif i == 'W':
            swapped += 'w'
        elif i == 'X':
            swapped += 'x'
        elif i == 'Y':
            swapped += 'y'
        elif i == 'Z':
            swapped += 'z'
        else:
            swapped += i
    #return the string in the swapped variable
    return swapped


#define string_lower function
def string_lower(string):
    #create a variable to store the lowercase string
    #make it empty
    lower = ''
    #create a for loop that iterates across the string
    #if i is a uppercase character, add the lowercase version of the character to the 'lower' variable
    #for everything else, just add them to the 'lower' variable
    for i in string:
        if i == 'A':
            lower += 'a'
        elif i == 'B':
            lower += 'b'
        elif i == 'C':
            lower += 'c'
        elif i == 'D':
            lower += 'd'
        elif i == 'E':
            lower += 'e'    
        elif i == 'F':
            lower += 'f'
        elif i == 'G':
            lower += 'g'
        elif i == 'H':
            lower += 'h'
        elif i == 'I':
            lower += 'i'
        elif i == 'J':
            lower += 'j'
        elif i == 'K':
            lower += 'k'
        elif i == 'L':
            lower += 'l'
        elif i == 'M':
            lower += 'm'
        elif i == 'N':
            lower += 'n'
        elif i == 'O':
            lower += 'o'
        elif i == 'P':
            lower += 'p'
        elif i == 'Q':
            lower += 'q'
        elif i == 'R':
            lower += 'r'
        elif i == 'S':
            lower += 's'
        elif i == 'T':
            lower += 't'
        elif i == 'U':
            lower += 'u'
        elif i == 'V':
            lower += 'v'
        elif i == 'W':
            lower += 'w'
        elif i == 'X':
            lower += 'x'
        elif i == 'Y':
            lower += 'y'
        elif i == 'Z':
            lower += 'z'
        else:
            lower += i
    #return the string in the lower variable
    return lower
