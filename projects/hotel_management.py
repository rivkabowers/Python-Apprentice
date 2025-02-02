

from tkinter import messagebox, simpledialog, Tk ;room = messagebox.showinfo("Hotel" , "Welcome to the hotel")
window = Tk()     # Create a window object
window.withdraw()


a = simpledialog.askstring("What do you want to do?" , "Do you want to Check in or Check out?")# Ask the user for the first number   


if a == 'Check in':
    messagebox.showinfo("Rooms", "0: Open, 1: Open, 2: Open, 3: Open, 4: Open, 5: Open, 6: Open, 7: Open, 8: Open, 9: Open, 10: Open")
    room = simpledialog.askinteger("Rooms" , "Which room do you want?")
    days = simpledialog.askinteger("Stay" , "How many days will you be staying for?")

elif a == 'Check out':
    messagebox.showinfo("Rooms", "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
    b = simpledialog.askinteger("Rooms" , "Which room did you stay in?")

else:
    messagebox.showinfo("Hmmmmm" , "I'm sorry I don't understand.")

######################################################################

if room == 0:
    messagebox.showinfo("Cost",100 * days)
    simpledialog.askinteger("Please Pay",100 * days)

elif room == 1:
    messagebox.showinfo("Cost",110 * days)
    simpledialog.askinteger("Please Pay",110 * days)

elif room == 2:
    messagebox.showinfo("Cost",120 * days)
    simpledialog.askinteger("Please Pay",120 * days)

elif room == 3:
    messagebox.showinfo("Cost",130 * days)
    simpledialog.askinteger("Please Pay",130 * days)

elif room == 4:
    messagebox.showinfo("Cost",140 * days)
    simpledialog.askinteger("Please Pay",140 * days)

elif room == 5:
    messagebox.showinfo("Cost",150 * days)
    simpledialog.askinteger("Please Pay",150 * days)

elif room == 6:
    messagebox.showinfo("Cost",160 * days)
    simpledialog.askinteger("Please Pay",160 * days)

elif room == 7:
    messagebox.showinfo("Cost",170 * days)
    simpledialog.askinteger("Please Pay",170 * days)

elif room == 8:
    messagebox.showinfo("Cost",180 * days)
    simpledialog.askinteger("Please Pay",180 * days)

elif room == 9:
    messagebox.showinfo("Cost",190 * days)
    simpledialog.askinteger("Please Pay",190 * days)

elif room == 10:
    messagebox.showinfo("Cost",200 * days)
    pay = simpledialog.askinteger("Please Pay",200 * days)

else:
    messagebox.showinfo("Hmmmmm" , "I'm sorry I don't understand.")


window.mainloop()