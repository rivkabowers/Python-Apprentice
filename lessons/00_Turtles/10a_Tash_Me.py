""" Tash Me

Write a program that:
1) Load an emoji image as the background
2) Make the turtle shape a moustach
3) Move the moustache to the right spot on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""


import turtle 

def set_backround_image(window, image_name):

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

import turtle
turtle.setup(width=600, height=600)    

tina = turtle.Turtle()                  

screen = turtle.Screen()                
set_backround_image(screen, "emoji2.png")

def set_turtle_image(turtle, image_name):

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

screen = turtle.Screen()
screen.setup(width=600, height=600)

t = turtle.Turtle()
set_turtle_image(t, 'moustache1.gif')      

turtle.exitonclick()

