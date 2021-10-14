#Kieren Singh Gill
#11/10/2020
#Python Fall 2020, Section 1
#GillKieren_Assign8_problem2.py

#define listlen function, input is list x
#create a counter and set it to zero
def listlen(x):
    counter=0
    #create a for loop
    #loop iterates throughout list x
    #for each item in list x, add 1 to the counter
    #return the counter
    for i in x:
        counter+=1
    return counter

#define listmax function, input is list x
def listmax(x):
    #set largest value to None, in the event that the list is empty
    largest_value = None
    for i in x:
        #the first if statement will always run
        #this makes sure that if the list isn't empty
        #the largest_value will be changed
        #to the first item in the list
        if largest_value is None:
            largest_value = i
        #this statement will run if i is bigger than largest_value
        #it will make i the new largest_value
        elif i > largest_value:
            largest_value = i
    #return the largest_value
    return largest_value

#define listcopy function, input is the old_list
def listcopy(old_list):
    #make a copy of the old_list in the new_list variable
    new_list = list(old_list)
    #return the new_list which is the copy
    return new_list

#define listappend function, x is the list, y is the input to append
def listappend(x,y):
    #l is y stored in a list
    #z is a new list with the original list and the l list appended
    l = list([y])
    z = x+l
    #return z
    return z

#define listinsert function
#lst is the list
#index is the location
#data is the data element to be inserted
def listinsert(lst,index,data):
    #put the data element in list l
    #create a copy of lst in variable z
    #insert l in the location in z using index splicing
    l = list([data])
    z = list(lst)
    z[index:index] = l
    #return z
    return z

#define listremove function
#lst is the list
#x is the element to remove
def listremove(lst,x):
    #create empty list z, like an empty counter
    z=[]
    #create a for loop that iterates across the list
    #if i is in x
        #nothing happens, continue with the loop
    #if i isn't in x
    #add it to empty list z like a counter would
    for i in lst:
        if i == x:
          continue  
        else:
            z+=[i]
    #return list z
    return z

#define listreverse function
#lst is the list
def listreverse(lst):
    #create empty list z, like an empty counter    
    z=[]
    #create a for loop that iterates across the list
    for i in lst:
        #add i to the beginning of list z
        #by doing this, the later elements in the original list
        #will end up in front
        #this will end up reversing the original list
        z[:0]+=[i]
    #return list z
    return z
