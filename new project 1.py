
import tkinter as tk



from tkinter import messagebox
import os

attempts_left=3


def login_Button():
    global attempts_left

    username =usernameEntry.get()
    password = passwordEntry.get()

    if username == "" and password == "":
        messagebox.showinfo("Error", "Blank fields not allowed")

    elif username == "Nitish" and password == "1234":
        messagebox.showinfo("Success", "Login success")
        try:
            os.system("pdf2.pdf")

        except Exception as e :
            messagebox.showerror("Error", f"Could not open PDF file: {e}")
            root.destroy()

        else:
            attempts_left -= 1
            if attempts_left > 0:
                messagebox.showwarning("Warning", f"Incorrect credentials!\nAttempts left: {attempts_left}")

            else:
                messagebox.showerror("Blocked", "Too many failed attempts. Access denied.")
                login_button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("login")
root.geometry("300x600")
root.configure(bg="pink")

tk.Label(root,text="username",bg="blue").pack(pady=10)
usernameEntry = tk.Entry(root,show="*")
usernameEntry.pack()

tk.Label(root,text="password",bg="blue").pack(pady=10)
passwordEntry = tk.Entry(root,show="*")
passwordEntry.pack()

#login_Buttom
login_button = tk.Button(root, text="Login", command=login_Button)
login_button.pack(pady=10)





root.mainloop()

