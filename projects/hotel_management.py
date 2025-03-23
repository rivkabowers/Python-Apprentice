from tkinter import messagebox, simpledialog, Tk


window = Tk()
window.withdraw()

room = {i: 'Open' for i in range(11)}

guest_info = {}

def check_in():
    name = simpledialog.askstring("Hello", "What is your name?")
    
    wantodo = simpledialog.askstring('Day', 'Are you having a nice day?')
    if wantodo.lower() == 'no':
        messagebox.showinfo('Bye', 'Ok, have a nice day!')
        return
    
    elif wantodo.lower() == 'yes':
        messagebox.showinfo('Rooms', str(room))

        many = simpledialog.askinteger("Rooms", "How many rooms do you want? Maximum 11.")
        if many > 11:
            messagebox.showinfo("Error", "You can only book up to 11 rooms.")
            return

        stayrooms = []  
        for i in range(many):
            stayroom = simpledialog.askinteger("Rooms", "Which room do you want to stay in?")
            if room.get(stayroom) == 'Open':
                stayrooms.append(stayroom)
                room[stayroom] = 'Occupied'
            else:
                messagebox.showinfo("Error", f"Room {stayroom} is already occupied.")
                continue 

        days = simpledialog.askinteger("Stay", "How many days will you be staying for?")
        extra = simpledialog.askstring('Extras', 'Do you want pool or gym access?')


        extra_cost = 0
        if extra == 'pool':
            extra_cost = 30
        elif extra == 'gym':
            extra_cost = 30
        elif extra == 'both' or extra == 'pool, gym' or extra == 'pool and gym':
            extra_cost = 60
        elif extra == 'no':
            extra_cost = 0

        total_cost = 0
 
        for room_num in stayrooms:
            if room_num == 0:
                total_cost += 50 * days + extra_cost
            elif room_num == 1:
                total_cost += 60 * days + extra_cost
            elif room_num == 2:
                total_cost += 70 * days + extra_cost
            elif room_num == 3:
                total_cost += 80 * days + extra_cost
            elif room_num == 4:
                total_cost += 90 * days + extra_cost
            elif room_num == 5:
                total_cost += 100 * days + extra_cost
            elif room_num == 6:
                total_cost += 110 * days + extra_cost
            elif room_num == 7:
                total_cost += 120 * days + extra_cost
            elif room_num == 8:
                total_cost += 130 * days + extra_cost
            elif room_num == 9:
                total_cost += 140 * days + extra_cost
            elif room_num == 10:
                total_cost += 150 * days + extra_cost

        messagebox.showinfo("Cost", f"Your total cost is ${total_cost}")
        

        cost = simpledialog.askinteger("Pay", f"Please Pay ${total_cost}")
        
        if cost == total_cost:
            guest_info[name] = stayrooms 
            messagebox.showinfo("Thank you", f"Have a nice day, {name}")
            messagebox.showinfo("Information", f"{name}, Rooms: {stayrooms}")
        else:
            simpledialog.askinteger("Error", "Please pay the right amount.")
            messagebox.showinfo("Bye", f"Have a nice day {name}")
            messagebox.showinfo("Information", f"{name}, Rooms: {stayrooms}")

        messagebox.showinfo('Rooms', str(room))

def check_out():
    names = simpledialog.askstring("Name", "What is your name?")
    
    if names not in guest_info:
        messagebox.showinfo("Error", "Hmmm I'm sorry I don't understand")
        return

    stayrooms = guest_info[names]
    messagebox.showinfo("Information", f"{names}, Rooms: {stayrooms}")

    messagebox.showinfo("Check out", "Successful check out!")
    messagebox.showinfo("Thank you", f"Thank you for staying at the hotel, have a nice day, {names}!")
    
    for room_num in stayrooms:
        room[room_num] = 'Open'
    
    del guest_info[names]


for i in range(4):
    messagebox.showinfo("Welcome", 'Welcome to the hotel!')
    stuff = simpledialog.askstring("Want to do", 'Do you want to check in or check out?')

    if stuff == 'check out':
        check_out()
    elif stuff == 'check in':
        check_in()