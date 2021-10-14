#Kieren Singh Gill
#11/16/2020
#Python Fall 2020, Section 1
#GillKieren_Assign9_problem2.py

#import the turtle module
#setup the canvas so it is 500 by 500
import turtle
turtle.setup(500,500)

#list with the instructions for the turtle 
secret = ['S',-204,198,'P',-204,198,'P',-204,198,'P',-201,135,'P',-199,104,'P',-199,104,'E',-199,104,'S',-199,140,'P',-199,140,'P',-187,140,'P',-176,144,'P',-165,147,'E',-165,147,'S',-168,205,'P',-168,205,'P',-168,149,'P',-165,87,'P',-164,74,'E',-164,74,'S',-141,91,'P',-141,98,'P',-141,161,'P',-128,150,'P',-104,99,'P',-100,93,'E',-100,93,'S',-140,116,'P',-132,116,'P',-115,116,'P',-115,116,'E',-115,116,'S',-96,152,'P',-94,139,'P',-72,50,'P',-71,44,'E',-71,44,'S',-95,147,'P',-95,147,'P',-85,152,'P',-61,143,'P',-77,108,'P',-87,104,'E',-87,104,'S',-48,148,'P',-48,148,'P',-46,130,'P',-26,42,'P',-26,42,'E',-26,42,'S',-48,147,'P',-48,147,'P',-31,147,'P',-16,138,'P',-17,125,'P',-36,110,'P',-41,107,'P',-41,107,'E',-41,107,'S',-5,152,'P',-5,152,'P',-3,125,'P',14,117,'P',22,139,'P',22,151,'P',31,121,'P',34,94,'P',30,67,'P',13,65,'E',13,65,'S',-194,-23,'P',-194,-23,'P',-173,-22,'P',-127,-15,'E',-127,-15,'S',-156,-24,'P',-156,-25,'P',-155,-89,'P',-153,-103,'E',-153,-103,'S',-140,-35,'P',-140,-47,'P',-140,-91,'P',-140,-96,'E',-140,-96,'S',-140,-75,'P',-140,-75,'P',-127,-69,'P',-119,-78,'P',-119,-96,'E',-119,-96,'S',-87,-68,'P',-87,-68,'P',-103,-70,'P',-110,-87,'P',-98,-95,'P',-89,-82,'P',-87,-70,'P',-80,-93,'P',-79,-97,'E',-79,-97,'S',-65,-99,'P',-65,-99,'P',-65,-79,'P',-65,-71,'P',-40,-100,'P',-30,-91,'P',-30,-65,'E',-30,-65,'S',-19,-20,'P',-18,-51,'P',-18,-87,'P',-18,-99,'E',-18,-99,'S',5,-53,'P',5,-57,'P',-13,-74,'P',-18,-77,'P',8,-95,'P',13,-101,'E',14,-101,'S',42,-57,'P',35,-57,'P',22,-58,'P',31,-76,'P',46,-82,'P',37,-106,'P',30,-100,'E',30,-100,'S',81,-64,'P',80,-64,'P',68,-68,'P',67,-93,'P',83,-85,'P',82,-71,'P',85,-88,'P',91,-132,'P',60,-129,'E',59,-128,'S',92,-67,'P',92,-89,'P',92,-97,'E',92,-97,'S',103,-68,'P',103,-68,'P',105,-88,'P',107,-93,'P',110,-85,'P',114,-70,'E',114,-69,'S',127,-68,'P',127,-71,'P',127,-96,'E',127,-96,'S',144,-96,'P',144,-96,'P',144,-77,'P',144,-69,'P',169,-101,'P',174,-74,'P',174,-71,'E',174,-71,'S',200,-69,'P',191,-69,'P',188,-87,'P',202,-90,'P',202,-72,'P',205,-82,'P',216,-127,'P',198,-136,'P',181,-143,'E',181,-143]

#I commented this out because it is unnecessary but I used this method
#and it worked too
#I split up the list secret into three smaller lists
#I used those three smaller lists to create a larger list
#with nested lists inside
#each nested list should look like: ['Command', 'X', 'Y']

##commands = []
##x_coords = []
##y_coords = []
##for i in range(0,len(secret)):
##    if (i+3)%3 == 0:
##        commands += [secret[i]]
##        
##for i in range(0,len(secret)):
##    if (i+2)%3 == 0:
##        x_coords += [secret[i]]
##         
##for i in range(0,len(secret)):
##    if (i+1)%3 == 0:
##        y_coords += [secret[i]]        
##
##
##biglist =[]
##sublist =[]
##for i in range(0,len(commands)):
##    c0=commands[i]
##    x0=x_coords[i]
##    y0=y_coords[i]
##    sublist=[c0,x0,y0]
##    biglist+=[sublist]

#instead of using the method above, I found a simpler method
#which helps me create the big list with nested lists that I want

#create a while loop with counter i
    #set counter i to zero
#create a new_list
#the while loop will run as long as i is less than the length
    #of the list 'secret'
i = 0
new_list=[]
while i<len(secret):
    #for each loop, splice the list 'secret' three values at a time
    #append those values to the new_list
    #add 3 to counter i so that the next loop will skip the values that were
        #already spliced, and will splice the next three values
    new_list.append(secret[i:i+3])
    i+=3
#after this while loop, new_list should consist of multiple lists
#each nested list in new_list should look like: ['Command', 'X', 'Y']

#create a for loop
    #loop will iterate over the length of the new list
for i in range(len(new_list)):
    #splice out the nested list at i position in the new_list
    nestedlist = new_list[i]
    #splice out the command, x coordinate, and y coordinate
    #store them in variables c, x, and y respectively
    c = nestedlist[0]
    x = nestedlist[1]
    y = nestedlist[2]

    #if the command is 'S'
    #turtle lifts up the pen
    #turtle goes to x,y coordinates
    if c == 'S':
        turtle.penup()
        turtle.goto(x,y)

    #if the command is 'P'
    #turtle puts down pen
    #turtle goes to x,y coordinates
    if c == 'P':
        turtle.pendown()
        turtle.goto(x,y)
        
    #if the command is 'E'
    #turtle lifts up pen
    #turtle goes to x,y coordinates
    if c == 'E':
        turtle.penup()
        turtle.goto(x,y)

#Happy Thanksgiving to you too Professor Hasan!
