

from tkinter import messagebox, simpledialog, Tk ;room = messagebox.showinfo("Hotel" , "Welcome to the hotel")
window = Tk()     # Create a window object
window.withdraw()


name = simpledialog.askstring("Hello" , "What is your name?")

a = simpledialog.askstring("What do you want to do?" , "Do you want to Check in or Check out?")# Ask the user for the first number   


if a == 'Check in':
    room = messagebox.showinfo("Rooms", "0: Open, 1: Open, 2: Open, 3: Open, 4: Open, 5: Open, 6: Open, 7: Open, 8: Open, 9: Open, 10: Open")
    b = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
    days = simpledialog.askinteger("Stay" , "How many days will you be staying for?")


elif a == 'Check out':
    room = messagebox.showinfo("Rooms", "0: Open, 1: Open, 2: Open, 3: Open, 4: Open, 5: Open, 6: Open, 7: Open, 8: Open, 9: Open, 10: Open")
    b = simpledialog.askinteger("Rooms" , "Which room did you stay in?")

else:
    messagebox.showinfo("Hmmmmm" , "I'm sorry I don't understand.")

if b in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  messagebox.showinfo("Cost",f"${100 * days}")
  pay = simpledialog.askinteger("Please Pay",f"${100 * days}")

else:
   messagebox.showinfo("Hmmmmm" , "I'm sorry I don't understand.")

if pay == 100 * days:
    messagebox.showinfo("Thank you", "Have a nice day, " + name)

else:
    simpledialog.askinteger(f"${100 * days}" , "Please pay the right amount")
    messagebox.showinfo("Thank you", "Have a nice day " + name)

window.mainloop()