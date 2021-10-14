#You have been asked to write a username validation program for a small website.
#The website has specific rules on what constitutes a valid username, including:

#All usernames must be between 8 and 15 characters long
#Usernames can only contain alphabetic (a-z and A-Z) and numeric characters (0-9) -no special characters or spaces are allowed.
#The first and last characters in a username cannot be a digit
#Usernames must contain at least one uppercase character  - True
#Usernames must contain at least one lowercase character - True
#Usernames must contain at least one numeric character - True

#length > 8 , < 15
#alphanumeric = True
#first and last not digit = True
#counter>=1
#counter2>=1
#counter3>=1

username = input("Enter username here: ")
length = len(username)
alphanumeric = username.isalnum()

x = username[0]
y = username [-1]
first_last = (not((x.isnumeric()))) and (not(y.isnumeric()))
print("Length of username:", length)
print("All characters are alpha-numeric:", username.isalnum())
x=username[0]
y=username[-1]
print("First & last characters are not digits:",(not((x.isnumeric()))) and (not(y.isnumeric())))
counter = 0 
for i in username:
    if i.isupper():
        counter +=1

print("# of uppercase characters in the username:", counter)

counter2 = 0 
for i in username:
    if i.islower():
        counter2 +=1

print("# of lowercase characters in the username:", counter2)


counter3 = 0 
for i in username:
    if i.isnumeric():
        counter3 +=1
        
print("# of digits in the username:", counter3)

def username_valid():
    if (((length > 8) and (length < 15)) and (alphanumeric) and (first_last) and (counter>=1) and (counter2>=1) and (counter3>=1)):
        return True
    else:
        return False

username_valid() == False
while username_valid()== False:
    print("Username is invalid, please try again")
    print()

    username = input("Enter username here: ")
    length = len(username)
    alphanumeric = username.isalnum()

    x = username[0]
    y = username [-1]
    first_last = (not((x.isnumeric()))) and (not(y.isnumeric()))
    print("Length of username:", length)
    print("All characters are alpha-numeric:", username.isalnum())
    x=username[0]
    y=username[-1]
    print("First & last characters are not digits:",(not((x.isnumeric()))) and (not(y.isnumeric())))
    counter = 0 
    for i in username:
        if i.isupper():
            counter +=1

    print("# of uppercase characters in the username:", counter)

    counter2 = 0 
    for i in username:
        if i.islower():
            counter2 +=1

    print("# of lowercase characters in the username:", counter2)


    counter3 = 0 
    for i in username:
        if i.isnumeric():
            counter3 +=1
            
    print("# of digits in the username:", counter3)
