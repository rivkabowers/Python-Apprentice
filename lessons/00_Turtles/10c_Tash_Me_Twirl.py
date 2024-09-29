
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

... # Your code here

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
set_backround_image(screen, "emoji.png")
  
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
set_turtle_image(t, 'moustache3.gif')    

def screen_clicked(x, y):
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    print('You pressed: x=' + str(x) + ', y=' + str(y))

    t.goto(x, y)

t.penup()
screen.onclick(screen_clicked) 

def turtle_clicked(t, x, y):
    """Function that gets called when the user clicks on the turtle

    This function will make the turtle tilt 20 degrees 18 times, making a full
    circle. It is called by the turtle when the user clicks on it.

    Args:
        t (Turtle): The turtle object that was clicked
        x (int): The x coordinate of the click
        y (int): The y coordinate of the click
    """

    print('turtle clicked!')
    
    for i in range(0,360, 20): # Full circle, 20 degrees at a time
        t.tilt(90) # Tilt the turtle 20 degrees

# Connect the turtle to the turtle_clicked function
t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))

turtle.done() 