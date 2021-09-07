#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Maggie Paul
Sep 7, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======




#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()

turtle.Turtle()


turtle.up()
turtle.goto(-40,185)
turtle.down()
turtle.color('red3')

turtle.begin_fill()
turtle.backward(40)
turtle.left(60)
turtle.forward(40)
turtle.right(120)
turtle.forward(40)
turtle.end_fill()


turtle.up()
turtle.goto(10,185)
turtle.down()
turtle.begin_fill()
turtle.left(60)
turtle.forward(40)
turtle.left(120)
turtle.forward(40)
turtle.left(120)
turtle.forward(40)
turtle.end_fill()

turtle.up()
turtle.goto(85,-160)
turtle.down()
turtle.left(30)
turtle.pensize(10)
turtle.backward(120)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(60)

turtle.pensize(5)
turtle.left(90)
turtle.forward(20)
turtle.right(120)
turtle.forward(40)
turtle.right(120)
turtle.forward(40)
turtle.right(120)
turtle.forward(20)


turtle.up()
turtle.forward(60)
turtle.down()
turtle.forward(20)
turtle.right(120)
turtle.forward(40)
turtle.right(120)
turtle.forward(40)
turtle.right(120)
turtle.forward(20)
turtle.left(90)
turtle.pensize(10)
turtle.forward(60)
turtle.left(90)
turtle.forward(30)


turtle.up()
turtle.goto(85,-160)
turtle.pensize(5)
turtle.color('black')
turtle.begin_fill()
turtle.down()
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.end_fill()




