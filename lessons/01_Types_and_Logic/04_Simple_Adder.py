"""4
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.
.showinfo("A number" , "Type some numbers")
In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

from tkinter import messagebox, simpledialog, Tk ;number = messagebox.showinfo("Number" , "Type some numbers")
window = Tk()     # Create a window object33
window.withdraw()# Import the required module56# Create a window object# Hide the window, hint: use the withdraw method

a = simpledialog.askinteger("First number" , "Type in a number")# Ask the user for the first number   

b = simpledialog.askinteger("Second number" , "Type in another number")# Ask the user for the second number

messagebox.showinfo("Answer" , a + b)# Display the sum of the two numbers

window.mainloop()# Keep the window open