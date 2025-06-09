import tkinter as tk
from tkinter import messagebox
import requests

CORRECT_PASSWORD = "NITISH@2006"

def show_main_form():
    root = tk.Tk()
    gender_var = tk.StringVar(value="Male")
    stream_label = tk.StringVar(value="PCM")
    terms_var = tk.BooleanVar()

    root.title("School Form")
    root.geometry("500x700")
    root.configure(bg='lightblue')
    root.config(padx=20, pady=20)

    def submit_form():
        name = nameEntry.get()
        email = emailEntry.get()
        gender = gender_var.get()
        stream = stream_label.get()

        form_data = {
            "name": name,
            "email": email,
            "gender": gender,
            "stream": stream
        }

        url = "https://script.google.com/macros/s/AKfycbzWlN7iBSibQ2cTni5-H4psFnNcCly33J5fEWMG9z5IlNuHDSO-Aephmj4PoV_ShWby/exec"

        try:
            response = requests.post(url, json=form_data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Form submitted successfully!")
                nameEntry.delete(0, tk.END)
                emailEntry.delete(0, tk.END)
                gender_var.set("Male")
                stream_label.set("PCM")
            else:
                messagebox.showerror("Error", f"Failed to submit form.\nStatus code: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # --- UI Elements ---
    tk.Label(root, text="Student Name", font=("Arial", 14), bg="lightblue").grid(row=0, column=0, sticky="w")
    nameEntry = tk.Entry(root, width=30)
    nameEntry.grid(row=1, column=0, pady=5)

    tk.Label(root, text="Email", font=("Arial", 14), bg="lightblue").grid(row=2, column=0, sticky="w")
    emailEntry = tk.Entry(root, width=30)
    emailEntry.grid(row=3, column=0, pady=5)

    tk.Label(root, text="Gender", font=("Arial", 14), bg="lightblue").grid(row=4, column=0, sticky="w")
    tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", bg="lightblue").grid(row=5, column=0, sticky="w")
    tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", bg="lightblue").grid(row=6, column=0, sticky="w")

    tk.Label(root, text="Stream", font=("Arial", 14), bg="lightblue").grid(row=7, column=0, sticky="w")
    tk.Radiobutton(root, text="PCM", variable=stream_label, value="PCM", bg="lightblue").grid(row=8, column=0, sticky="w")
    tk.Radiobutton(root, text="Commerce", variable=stream_label, value="COMMERCE", bg="lightblue").grid(row=9, column=0, sticky="w")
    tk.Radiobutton(root, text="Art", variable=stream_label, value="ART", bg="lightblue").grid(row=10, column=0, sticky="w")
    tk.Radiobutton(root, text="PCB", variable=stream_label, value="PCB", bg="lightblue").grid(row=11, column=0, sticky="w")

    tk.Checkbutton(root, text="I accept the Terms and Conditions", variable=terms_var, bg="lightblue").grid(row=12, column=0, pady=10, sticky="w")

    tk.Button(root, text="Submit", command=submit_form, bg="green", fg="white").grid(row=13, column=0, pady=10)

    root.mainloop()

def password_prompt():
    cm_window = tk.Tk()
    cm_window.title("Enter Password")
    cm_window.geometry("300x150")
    cm_window.configure(bg="pink")

    tk.Label(cm_window, text="Enter password to access form:", bg="pink").pack(pady=10)
    cm_entry = tk.Entry(cm_window, show="*")
    cm_entry.pack(pady=5)

    def check_password():
        if cm_entry.get() == CORRECT_PASSWORD:
            cm_window.destroy()
            show_main_form()
        else:
            messagebox.showerror("Access Denied", "Incorrect password. Access denied.")

    tk.Button(cm_window, text="Submit", command=check_password).pack(pady=10)
    cm_window.mainloop()

# Start the app
password_prompt()
