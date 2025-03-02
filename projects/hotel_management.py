from tkinter import messagebox, simpledialog, Tk ;room = messagebox.showinfo("Hotel" , "Welcome to the hotel")
window = Tk()     # Create a window object
window.withdraw()


name = simpledialog.askstring("Hello" , "What is your name?")

wantodo = simpledialog.askstring("Check in", "Would you like to Check in?")# Ask the user for the first number   

room = {
    0:'Open',
    1:'Open',
    2:'Open',
    3:'Open',
    4:'Open',
    5:'Open',
    6:'Open',
    7:'Open',
    8:'Open',
    9:'Open',
    10:'Open',
}

if wantodo == 'no':
    messagebox.showinfo('TOO BAD', 'Too bad')

elif wantodo == 'Yes' or 'yes':
    messagebox.showinfo('room', room)
    stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
    days = simpledialog.askinteger("Stay" , "How many days will you be staying for?")
    room[stayroom] == f'{name}'

else:
    messagebox.showinfo("Hmmmmm" , "I'm sorry I don't understand.")


if stayroom == 0:
    pay = 50
    messagebox.showinfo("Cost" , "That will cost you " f"${50*days}")
    cost = simpledialog.askinteger("Pay", "Please Pay " f"${50*days}")

elif stayroom == 1:
    pay = 60
    messagebox.showinfo("Cost" , "That will cost you " f"${60*days}")
    cost = simpledialog.askinteger("Pay", "Please Pay " f"${60*days}")  

elif stayroom == 2:
    pay = 70
    messagebox.showinfo("Cost" , "That will cost you " f"${70*days}")
    cost = simpledialog.askinteger("Pay", "Please Pay " f"${70*days}")

elif stayroom == 3:
    pay = 80
    messagebox.showinfo("Cost" , "That will cost you " f"${80*days}")
    cost = simpledialog.askinteger("Pay", "Please Pay " f"${80*days}")

elif stayroom == 4:
    pay = 90
    messagebox.showinfo("Cost" , "That will cost you " f"${90*days}")
    cost = simpledialog.askinteger("Pay", "Please Pay " f"${90*days}")

elif stayroom == 5:
    pay = 100
    messagebox.showinfo("Cost" , "That will cost you " f"${100*days}")
    cost = simpledialog.askinteger("Pay", "Please Pay " f"${100*days}")

elif stayroom == 6:
    pay = 110
    messagebox.showinfo("Cost" , "That will cost you " f"${110*days}")
    cost = simpledialog.askinteger("Pay", "Please Pay " f"${110*days}")

elif stayroom == 7:
    pay = 120
    messagebox.showinfo("Cost" , "That will cost you " f"${120*days}")
    cost = simpledialog.askinteger("Pay", "Please Pay " f"${120*days}")

elif stayroom == 8:
    pay = 130
    messagebox.showinfo("Cost" , "That will cost you " f"${130*days}")
    cost = simpledialog.askinteger("Pay", "Please Pay " f"${130*days}")

elif stayroom == 9:
    pay = 140
    messagebox.showinfo("Cost" , "That will cost you " f"${140*days}")
    cost = simpledialog.askinteger("Pay", "Please Pay " f"${140*days}")

elif stayroom == 10:
    pay = 150
    messagebox.showinfo("Cost" , "That will cost you " f"${150*days}")
    cost = simpledialog.askinteger("Pay", "Please Pay " f"${150*days}")
        
else:
   messagebox.showinfo("Hmmmmm" , "I'm sorry I don't understand.")

if cost == pay*days:
    messagebox.showinfo("Thank you", "Have a nice day, " + name)

else:
    simpledialog.askinteger( "Payment Error" , "Please pay the right amount")
    messagebox.showinfo("Thank you", "Have a nice day " + name)


if wantodo == 'Check out' or 'out':
    simpledialog.askstring("Check out", "Can I Check you out?")
    simpledialog.askstring("Name", "What is your name?")
    messagebox.showinfo("Occupied rooms", "Occupied rooms: #" + f"{stayroom}")
    roomstayed = simpledialog.askinteger("Room" , "Which room did you stay in " + name + "?")
    messagebox.showinfo("Thank you", "Thank you for staying at our Hotel, have a nice day, " + name + "!")
    messagebox.showinfo("Occupied rooms", "Rooms that are occupied: None")


window.mainloop()