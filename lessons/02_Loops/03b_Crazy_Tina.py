"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=570, height=570)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(20)                           # Make the turtle move as fast, but not too fast. 


forwards = [200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200]
lefts = [157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157,157]
colors = [ 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green','red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green','red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green','red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green','red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green','red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green','red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green','red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green','red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green','red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green','red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green']

for  i in range(160):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]


    tina.color(color)
    tina.forward(forward)
    tina.left(left)

turtle.exitonclick()  

