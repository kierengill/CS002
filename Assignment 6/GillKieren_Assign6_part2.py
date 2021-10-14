#Kieren Singh Gill
#10/26/2020
#Python Fall 2020, Section 1
#GillKieren_Assign6_part2.py

#create the print_number function
#three input variables for the function
#a is the number to print
#b is the width of the printed number
#c is the character that will be printed
def print_number(a,b,c):
    #if the number is 0
    if a == 0:
        print(c*b)
        print(c+(" "*(b-2))+c)
        print(c+(" "*(b-2))+c)
        print(c+(" "*(b-2))+c)
        print(c*b)

    #otherwise, if the number is 1    
    elif a==1:
        print((" "*(b-1))+c)
        print((" "*(b-1))+c)
        print((" "*(b-1))+c)
        print((" "*(b-1))+c)
        print((" "*(b-1))+c)

    #otherwise, if the number is 2
    elif a==2:
        print(c*b)
        print((" "*(b-1))+c)
        print(c*b)
        print(c+(" "*(b-1)))
        print(c*b)

    #otherwise, if the number is 3
    elif a==3:
        print(c*b)
        print((" "*(b-1))+c)
        print(c*b)
        print((" "*(b-1))+c)
        print(c*b)

    #otherwise, if the number is 4
    elif a==4:
        print(c+(" "*(b-2))+c)
        print(c+(" "*(b-2))+c)
        print(c*b)
        print((" "*(b-1))+c)
        print((" "*(b-1))+c)

    #otherwise, if the number is 5
    elif a==5:
        print(c*b)
        print(c+(" "*(b-1)))
        print(c*b)
        print((" "*(b-1))+c)
        print(c*b)

    #otherwise, if the number is 6
    elif a==6:
        print(c*b)
        print(c+(" "*(b-1)))
        print(c*b)
        print(c+(" "*(b-2))+c)
        print(c*b)

    #otherwise, if the number is 7
    elif a==7:
        print(c*b)
        print((" "*(b-1))+c)
        print((" "*(b-1))+c)
        print((" "*(b-1))+c)
        print((" "*(b-1))+c)

    #otherwise, if the number is 8
    elif a==8:
        print(c*b)
        print(c+(" "*(b-2))+c)
        print(c*b)
        print(c+(" "*(b-2))+c)
        print(c*b)

    #otherwise, if the number is 9
    elif a==9:
        print(c*b)
        print(c+(" "*(b-2))+c)
        print(c*b)
        print((" "*(b-1))+c)
        print((" "*(b-1))+c)

    #print a line break  
    print()


print_number(0,5,'*')
print_number(1,6,'*')
print_number(2,7,'*')
print_number(3,8,'*')
print_number(4,9,'*')
print_number(5,10,'*')
print_number(6,11,'*')
print_number(7,12,'*')
print_number(8,13,'*')
print_number(9,14,'*')
