from tkinter import messagebox, simpledialog, Tk ;room = messagebox.showinfo("Hotel" , "Welcome to the hotel")
window = Tk()     # Create a window object
window.withdraw()

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

def check_in():
    name = simpledialog.askstring("Hello" , "What is your name?")

    wantodo = simpledialog.askstring('day', 'Are you having a nice day?')# Ask the user for the first number   
    if wantodo == 'no':
        messagebox.showinfo('Bye', 'ok')
        
    
    elif wantodo == 'Yes' or 'yes':
        messagebox.showinfo('room', room)
        many = simpledialog.askinteger("Rooms" , "How many rooms would you like? Maximum 5.")
        if many == 1:
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
        
        elif many == 2:
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")

        elif many == 3:
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")

        elif many == 4:
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")

        elif many == 5:
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")
            stayroom = simpledialog.askinteger("Rooms" , "Which room do you want to stay in?")



        days = simpledialog.askinteger("Stay" , "How many days will you be staying for?")
        extra = simpledialog.askstring('Extras', 'Do you want pool or gym access?')

    if room[stayroom] == 'Open':
        room[stayroom] = f'{name}'
        messagebox.showinfo('room', room)

    else:
        messagebox.showinfo("Hmmmmm" , "I'm sorry I don't understand.")

    if extra == 'pool':
        extra = 30

    elif extra == 'gym':
        extra = 30

    elif extra == 'both':
        extra = 60

    elif extra == 'pool, gym':
        extra = 60

    elif extra == 'pool and gym':
        extra = 60

    elif extra == 'yes':
        extra = 30
    
    elif extra == 'no':
        extra = 0

    else:
        extra = 0


    if stayroom == 0:
        pay = 50
        messagebox.showinfo("Cost" , "That will cost you " f"${50*days*many+extra}")
        cost = simpledialog.askinteger("Pay", "Please Pay " f"${50*days*many+extra}")

    elif stayroom == 1:
        pay = 60
        messagebox.showinfo("Cost" , "That will cost you " f"${60*days*many+extra}")
        cost = simpledialog.askinteger("Pay", "Please Pay " f"${60*days*many+extra}")  

    elif stayroom == 2:
        pay = 70
        messagebox.showinfo("Cost" , "That will cost you " f"${70*days*many+extra}")
        cost = simpledialog.askinteger("Pay", "Please Pay " f"${70*days*many+extra}")

    elif stayroom == 3:
        pay = 80
        messagebox.showinfo("Cost" , "That will cost you " f"${80*days*many+extra}")
        cost = simpledialog.askinteger("Pay", "Please Pay " f"${80*days*many+extra}")

    elif stayroom == 4:
        pay = 90
        messagebox.showinfo("Cost" , "That will cost you " f"${90*days*many+extra}")
        cost = simpledialog.askinteger("Pay", "Please Pay " f"${90*days*many+extra}")

    elif stayroom == 5:
        pay = 100
        messagebox.showinfo("Cost" , "That will cost you " f"${100*days*many+extra}")
        cost = simpledialog.askinteger("Pay", "Please Pay " f"${100*days*many+extra}")

    elif stayroom == 6:
        pay = 110
        messagebox.showinfo("Cost" , "That will cost you " f"${110*days*many+extra}")
        cost = simpledialog.askinteger("Pay", "Please Pay " f"${110*days*many+extra}")

    elif stayroom == 7:
        pay = 120
        messagebox.showinfo("Cost" , "That will cost you " f"${120*days*many+extra}")
        cost = simpledialog.askinteger("Pay", "Please Pay " f"${120*days*many+extra}")

    elif stayroom == 8:
        pay = 130
        messagebox.showinfo("Cost" , "That will cost you " f"${130*days*many+extra}")
        cost = simpledialog.askinteger("Pay", "Please Pay " f"${130*days*many+extra}")

    elif stayroom == 9:
        pay = 140
        messagebox.showinfo("Cost" , "That will cost you " f"${140*days*many+extra}")
        cost = simpledialog.askinteger("Pay", "Please Pay " f"${140*days*many+extra}")

    elif stayroom == 10:
        pay = 150
        messagebox.showinfo("Cost" , "That will cost you " f"${150*days*many+extra}")
        cost = simpledialog.askinteger("Pay", "Please Pay " f"${150*days*many+extra}")
        
    else:
        messagebox.showinfo("Hmmmmm" , "I'm sorry I don't understand.")

    if cost == pay*days*many+extra:
        messagebox.showinfo("Thank you", "Have a nice day, " + name)
        messagebox.showinfo("Information", f"{name}" ', Room #' f"{stayroom}")

    else:
        simpledialog.askinteger( "Payment Error" , "Please pay the right amount")
        messagebox.showinfo("Thank you", "Have a nice day " + name)
        messagebox.showinfo("Information", f"{name}" ', Room #' f"{stayroom}")
    
    messagebox.showinfo('room', room)





def check_out():  
    nameroo = simpledialog.askstring("Name", "What is your name?")
    stayroo = simpledialog.askstring("Room" , "Which room did you stay in " + nameroo + "?")
    messagebox.showinfo("Information", f"{nameroo}" ', Room #' f"{stayroo}")
    messagebox.showinfo("CHeck out", "Successful check out!")
    messagebox.showinfo("Thank you", "Thank you for staying at our Hotel, have a nice day, " + name + "!")

    if room[stayroo] == f"{nameroo}":
        room[stayroo] = 'Open'

for i in range (2):
    stuff = simpledialog.askstring("Want to do", 'Do you want to check out or check in?')

    if stuff == 'check out':
        check_out()

    if stuff == 'check in':
        check_in()

window.mainloop()