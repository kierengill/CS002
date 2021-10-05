#Kieren Singh Gill
#09/21/2020
#Python Fall 2020, Section 1
#GillKieren_assign2_problem3.py

#Print the name of the program and an extra line for formatting
print("Minecraft block distance calculator")
print()

#Prompt user to input individal x, y, and z coordinates of block 1 and block 2
#Store input value in respective variables
x1 = int(input("Block #1 x: "))
y1 = int(input("Block #1 y: "))
z1 = int(input("Block #1 z: "))
x2 = int(input("Block #2 x: "))
y2 = int(input("Block #2 y: "))
z2 = int(input("Block #2 z: "))


#Calculate straight line distance using straight line distance formula
#Format the straight line distance to 2d.p.
straightline = (((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))**0.5
f_straightline = format(straightline, '.2f')

#Calculate the x distance, y distance, and z distance
#Use the absolute value function to make sure distance returned is positive
x_distance = abs(x2-x1)
y_distance = abs(y2-y1)
z_distance = abs(z2-z1)


#Print final output to user
#This shows the X distance, Y distance, Z distance, and the Straight Line Distance
print()
print("X distance:",x_distance)
print("Y distance:",y_distance)
print("Z distance:",z_distance)
print("Straight line distance:",f_straightline)
