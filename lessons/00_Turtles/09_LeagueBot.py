""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle 
turtle.setup(width=10, height=10)

t = turtle.Turtle()

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

def set_turtle_image(turtle, image_name):

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

screen = turtle.Screen()
screen.setup(width=600, height=600)

set_turtle_image(t, 'leaguebot_bolt.gif')


def draw_polygon(sides, t):
    for i in range(sides):
        t.forward(50)
        t.left(360/ sides)

t.speed(2)

t.pencolor('blue')

draw_polygon(6, t)

turtle.exitonclick()
