"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Background Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""


import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)

t = turtle.Turtle()

def set_turtle_image():turtle, "boy_yellow.gif"()

from pathlib import Path
image_dir = Path(__file__).parent / "boy_yellow.gif"
image_path = str(image_dir / "boy_yellow.gif")

screen = turtle.getscreen()
screen.addshape(image_path)
turtle.shape(image_path)


set_turtle_image(t, "boy_yellow.gif")

def set_background_image()window, "emoji2.png"():
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "emoji2.png"
    image_path = str(image_dir / "emoji2.png")

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)




t.penup()
t.speed(1)

t.penup()
t.goto(300,-235)
t.pendown
t.goto(300,300)
t.goto(-300,300)
t.goto(-300,-235)
t.goto(300,-235)

turtle.exitonclick()


