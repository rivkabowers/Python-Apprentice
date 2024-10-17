
"""
Am I Big Yet?

Ask the user's age then use an if-elif-else statement to 
tell the user what age groups the user is in. The groups are:

0-2: Baby
3-5: Toddler
6-12: Child
13-18: Teen
19-54: Adult
54+: Senior

Except, if the user is the same age as you, print "You are pretty awesome!"

Here is how you ask the user's age in integer format.  The first argument is 
the title of the window, the second is the message to the user.

age = simpledialog.askinteger("Your Age", "How old are you?") 

Or, you could ask the user for a float with simpledialog.askfloat() 

age =  simpledialog.askfloat("Your Age", "How old are you?")


Here is how you show the user a message window. The first parameter is the title of the window, 
the second is the message to show the user.

messagebox.showinfo('What you are', "You are a baby.")

"""

from tkinter import messagebox, simpledialog, Tk ;age = simpledialog.askinteger("Your Age", "How old are you?")

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

messagebox.showinfo('How old are you')# Ask the user's age

if age >=0 and age <=2: 
    messagebox.showinfo('What you are', 'You are a Baby')
if age >=3 and age <=5: 
    messagebox.showinfo('What you are', 'You are a Toddler')
if age >=6 and age <=12: 
    messagebox.showinfo('What you are', 'You are a Child')
if age >=13 and age <=18: 
    messagebox.showinfo('What you are', 'You are a Teen')
if age >=19 and age <=54: 
    messagebox.showinfo('What you are', 'You are a Adult')
if age >=54 and age <=1000: 
    messagebox.showinfo('What you are', 'You are a Senior')
# Use if statements to determine the age group
# and create a message
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
#REMEBER TO SIGN OUT OR ELSE
# Show the message to the user
window.mainloop()  # Keeps the window open


# TODO: 
# Try to write your program so you only need to use one messagebox.showinfo() function.
