#Kieren Singh Gill
#10/06/2020
#Python Fall 2020, Section 1
#GillKieren_assign4_extra.py

import time
import random
import turtle

time_start=time.time()

turtle.setup(800,500)
turtle.speed(10)
turtle.hideturtle()
turtle.tracer(0)

turtle.pencolor("blue")
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

blue_circle_x=0
blue_circle_y=100



turtle.penup()
turtle.goto(-50,-50)
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.pendown()
turtle.goto(50,-50)
turtle.goto(50,-200)
turtle.goto(-50,-200)
turtle.goto(-50,-50)
turtle.end_fill()

red_block_x=0
red_block_y=-125

turtle.penup()
turtle.goto(-250,0)
turtle.pencolor("light gray")
turtle.fillcolor("light gray")
turtle.begin_fill()
turtle.pendown()
turtle.circle(50)
turtle.end_fill()


turtle.penup()
turtle.goto(-250,-150)
turtle.pencolor("dim gray")
turtle.fillcolor("dim gray")
turtle.begin_fill()
turtle.pendown()
turtle.circle(100)


turtle.penup()
turtle.goto(-250,0)
turtle.pendown()
turtle.circle(50)
turtle.end_fill()


turtle.penup()
turtle.goto(150,200)
turtle.pencolor("lime")
turtle.fillcolor("lime")
turtle.begin_fill()
turtle.pendown()
turtle.goto(350,200)
turtle.goto(350,-200)
turtle.goto(150,-200)
turtle.goto(150,200)
turtle.end_fill()


turtle.penup()
turtle.goto(200,0)
turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
turtle.pendown()
turtle.goto(200,-50)
turtle.goto(250,-50)
turtle.goto(250,0)
turtle.goto(200,0)
turtle.end_fill()


turtle.penup()
turtle.goto(250,-100)
turtle.begin_fill()
turtle.pendown()
turtle.goto(250,-150)
turtle.goto(300,-150)
turtle.goto(300,-100)
turtle.goto(250,-100)
turtle.end_fill()


turtle.penup()
turtle.goto(200,50)
turtle.begin_fill()
turtle.pendown()
turtle.goto(200,150)
turtle.goto(300,150)
turtle.goto(300,50)
turtle.goto(200,50)
turtle.end_fill()


turtle.update()


throws=int(input("Number of throws: "))

while throws < 0:
    print("Invalid, try again!")
    throws=int(input("Number of throws: "))

print()

time_end=time.time()
time_elapsed=time_end - time_start
print("Total time elapsed:",'{0:.2f}'.format(time_elapsed),"seconds")

points_in_blue_circle = 0
points_in_red_block = 0
for i in range (throws+1):
    turtle.penup()
    point_x = random.randint(-400,400)
    point_y = random.randint(-200,200)
    turtle.goto(point_x,point_y)

    distance_to_blue_center = ((point_x-blue_circle_x)**2+(point_y-blue_circle_y)**2)**(1/2)
    
    if distance_to_blue_center < 100:
        points_in_blue_circle += 1
   
    turtle.pencolor("orange")
    turtle.begin_fill()
    turtle.pendown()
    turtle.dot(5)
    turtle.end_fill()
    
print("Blue:", points_in_blue_circle,"("+str(points_in_blue_circle/throws*100)+"%)")
