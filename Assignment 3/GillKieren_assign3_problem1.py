#Kieren Singh Gill
#09/28/2020
#Python Fall 2020, Section 1
#GillKieren_assign3_problem1.py

#print the title of the program
print ("Valid triangle tester")
print()


#prompt user to input x and y coordinates for Point #1, #2 and #3
#store value as float
x1 = float(input("Enter Point #1 - x position: "))
y1 = float(input("Enter Point #1 - y position: "))
x2 = float(input("Enter Point #2 - x position: "))
y2 = float(input("Enter Point #2 - y position: "))
x3 = float(input("Enter Point #3 - x position: "))
y3 = float(input("Enter Point #3 - y position: "))


#distance formula to calculate the length of the different sides
side1 = (((x1-x2)**2 + (y1-y2)**2)**0.5)
side2 = (((x1-x3)**2 + (y1-y3)**2)**0.5)
side3 = (((x2-x3)**2 + (y2-y3)**2)**0.5)


#format the sides to floating point values up to 2 decimal places
#this is to ensure that there will not be floating point inaccuracies 
f_s1 = ("{:.2f}".format(side1))
f_s2 = ("{:.2f}".format(side2))
f_s3 = ("{:.2f}".format(side3))


#print the length of each side of the test shape
print()
print("The length of each side of your test shape is: ")
print()
print ("Side 1:", f_s1)
print ("Side 2:", f_s2)
print ("Side 3:", f_s3)

print()

#to verify that the triangle is valid, it must follow the following 3 conditions
#Side 1 + Side 2 must be longer than Side 3
#Side 2 + Side 3 must be longer than Side 1
#Side 3 + Side 1 must be longer than Side 2

#if statement to verify these conditions
if f_s1 + f_s2 > f_s3 and f_s2 + f_s3 > f_s1 and f_s1 + f_s3 > f_s2:
    
    #if all conditions are true
    #let the user know that it is a valid triangle
    print("This is a valid triangle!")


    #check if it is an equilateral triangle
    if f_s1 == f_s2 and f_s2 == f_s3:
        
        #if all conditions are true
        #let the user know that it is an equilateral triangle
        print("This is an equilateral triangle")


    #if triangle isn't equilateral
    #check if it is an isoceles triangle
    elif f_s1 == f_s2 or f_s2 == f_s3 or f_s1 == f_s3:
        
        #if any one of the conditions are true
        #let the user know that it is an isoceles triangle
        print("This is an isoceles triangle")


    #if triangle isn't equilateral and isoceles
    #then it must be scalene
    #let the user know it is a scalene triangle
    else:
        print("This is a scalene triangle")


    #turtle graphics to draw the triangle

    #import the turtle graphics module
    import turtle

    #I chose to hide the turtle so that it won't show up in the drawing of the triangle
    turtle.hideturtle()

    #set up the canvas for the turtle to draw
    turtle.setup(500,500)

    #if the triangle is equilateral
    #pen color is green
    if f_s1 == f_s2 and f_s2 == f_s3:
        turtle.pencolor("green")

    #if the triangle is isoceles
    #pen color is blue
    elif f_s1 == f_s2 or f_s2 == f_s3 or f_s1 == f_s3:
        turtle.pencolor("blue")

    #if the triangle is not equilateral or isoceles
    #then it must be scalene
    #pen color is red
    else:
        turtle.pencolor("red")

    #lift up the pen so it doesn't draw
    #move the turtle to the first point (x1,y1)
    #put the pen down
    #begin drawing the triangle
    #move the turtle to the second point (x1,y1)
    #move the turtle to the third point (x1,y1)
    #move the turtle back to the first point (x1,y1)

    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()

    turtle.goto(x2,y2)

    turtle.goto(x3,y3)

    turtle.goto(x1,y1)



#if it isn't a valid triangle
#let the user know it isn't valid
else:
    print("This is not a valid triangle")
