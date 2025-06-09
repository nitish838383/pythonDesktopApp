import tkinter as tk

from tkinter import messagebox


from datetime import datetime

def calculate_totals():
    try:
        # Get values from entries
        name = nameEntry.get()
        year = int(yearEntry.get())
        month = int(monthEntry.get())
        day = int(dayEntry.get())

        birthdate = datetime(year, month, day)
        today = datetime.today()

        # Calculate age
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        # Display result
        messagebox.showinfo("Age Calculator", f"{name}, you are {age} years old.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for year, month, and day.")



root = tk.Tk()
root.title("age calculator")
root.geometry("400x600")
root.configure(bg="green")

tk.Label(root,text="name",font=("arial",10,"bold"),bg="pink").pack(pady=10)
nameEntry=tk.Entry(root)
nameEntry.pack()

tk.Label(root,text="year",font=("arial",10,"bold"),bg="pink").pack(pady=10)
yearEntry=tk.Entry(root)
yearEntry.pack()

tk.Label(root,text="month",font=("arial",10,"bold"),bg="pink").pack(pady=10)
monthEntry=tk.Entry(root)
monthEntry.pack()

tk.Label(root,text="day",font=("arial",10,"bold"),bg="pink").pack(pady=10)
dayEntry=tk.Entry(root)
dayEntry.pack()
#buttom
tk.Button(root,text="calculator",command=calculate_totals,font=("arial",10,"bold"),bg="pink").pack(pady=10)













root.mainloop()