"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

from tkinter import messagebox, simpledialog, Tk ;number = messagebox.showinfo("Calculator" , "Type in some numbers")
window = Tk()     # Create a window object
window.withdraw()# Import the required module
# Create a window object
# Hide the window, hint: use the withdraw method

a = simpledialog.askinteger("First number" , "Type in the first number")# Ask the user for the first number   

b = simpledialog.askinteger("Second number" , "Type in the second number")# Ask the user for the second number# Import the required modules

c = simpledialog.askstring("Math symbol" , "Type in your math symbol")

if c == ('*'):
   messagebox.showinfo("Answer" ,a * b) # Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

elif c == ('+'):
   messagebox.showinfo("Answer" ,a + b)

elif c == ('-'):
   messagebox.showinfo("Answer" ,a - b)

elif c == ('/'):
   messagebox.showinfo("Answer" ,a / b)

else: 
   messagebox.showerror("Error" , "I don't know what that means")# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

window.mainloop()# Keep the window open
