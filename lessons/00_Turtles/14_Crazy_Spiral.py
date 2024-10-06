"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""

import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "pink", "blue", "purple", "orange"]

turtle.setup (width=600, height=600) 
window = turtle.Screen()

t = turtle.Turtle() 

t.shape("turtle") 

t.width(2) 

t.speed(0)  

t.penup()
t.goto(100,100)

# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.

t.pendown()
def make_a_shape(t):
    """Make a shape with turtle t. Make it go left or right or forward"""    
    t.left(10)
    t.forward(94)
    t.right(50)
    t.forward(20)
    t.right(450)
    t.left(30)
# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

num_shapes = 100

for i in range(20):
    make_a_shape(t)
    t.right(360/num_shapes)

t.pencolor('blue')
for i in range(20):
    make_a_shape(t)
    t.right(360/num_shapes)

t.pencolor('purple')
for i in range(20):
    make_a_shape(t)
    t.right(360/num_shapes)

t.pencolor('pink')
for i in range(20):
    make_a_shape(t)
    t.right(360/num_shapes)

t.pencolor('yellow')
for i in range(20):
    make_a_shape(t)
    t.right(360/num_shapes)

turtle.exitonclick()
