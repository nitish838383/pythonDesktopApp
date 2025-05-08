import tkinter as tk


from tkinter import messagebox

import requests
import json

def submit_form():
    # Get form data
    name = nameEntry.get()
    email = emailEntry.get()
    gender = gender_var.get()
    stream = stream_label.get()

    # Validate inputs


    # Prepare data for API
    form_data = {
        "name": name,
        "email": email,
        "gender":gender,
        "stream":stream
    }

    # Google Apps Script Web App URL
    url ="https://script.google.com/macros/s/AKfycbzWlN7iBSibQ2cTni5-H4psFnNcCly33J5fEWMG9z5IlNuHDSO-Aephmj4PoV_ShWby/exec"

    try:
        print("Sending data:", form_data)  # Debug print
        response = requests.post(url, json=form_data)
        print("Response status code:", response.status_code)  # Debug print
        print("Response content:", response.text)  # Debug print

        if response.status_code == 200:
            messagebox.showinfo("Success", "Form submitted successfully!")
            # Clear form
            nameEntry.delete(0, tk.END)
            emailEntry.delete(0, tk.END)
            gender_var.set("Male")  # Reset to default
        else:
            messagebox.showerror("Error", f"Failed to submit form.\nStatus code: {response.status_code}\nResponse: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        print("Full error details:", e)  # Debug print






root = tk.Tk()
gender_var = tk.StringVar()
gender_var.set("Male")


root.title("School Form")
root.geometry("500x500")
root.config(padx=20, pady=20)

root.configure(bg='lightblue')
root.geometry("300x200")

nameLabel = tk.Label(root, text="Student Name",font=("Arial",20,"bold"),fg="blue")
nameLabel.grid(row=0, column=0, sticky="w")

nameEntry = tk.Entry(root, width=30)
nameEntry.grid(row=1, column=0, pady=(10, 10))

emailLabel = tk.Label(root, text="Email",font=("Arial",10,"bold"),fg="red")
emailLabel.grid(row=2, column=0, sticky="w")

emailEntry = tk.Entry(root, width=30)
emailEntry.grid(row=3, column=0, pady=(10, 10))

classLabel = tk.Label(root, text="Class",font=("Arial",10,"bold"),fg="red")
classLabel.grid(row=4, column=0, sticky="w")

classEntry = tk.Entry(root, width=30)
classEntry.grid(row=5, column=0, pady=(10, 10))

sectionLabel = tk.Label(root, text="Section",font=("Arial",10,"bold"),fg="red")
sectionLabel.grid(row=6, column=0, sticky="w")

sectionEntry = tk.Entry(root, width=30)
sectionEntry.grid(row=7, column=0, pady=(10, 10))

RollNoLabel = tk.Label(root, text="Roll.NO",font=("Arial",10,"bold"),fg="red")
RollNoLabel.grid(row=8, column=0, sticky="w")

RollNoEntry = tk.Entry(root, width=30)
RollNoEntry.grid(row=9, column=0, pady=(10, 10))

genderLabel = tk.Label(root, text="gender",font=("Arial",10,"bold"),fg="red")
genderLabel.grid(row=8, column=0, sticky="w")


male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=10, column=0, padx=10, pady=5,sticky="w")

female_radio = tk.Radiobutton(root, text="feMale", variable=gender_var, value="feMale")
female_radio.grid(row=11, column=0, padx=10, pady=5,sticky="w")





# Variable to hold selected stream
stream_label = tk.StringVar()
stream_label.set("pcm")

streamLabel = tk.Label(root, text="Stream",font=("Arial",10,"bold"),fg="red")
streamLabel.grid(row=15, column=0, sticky="w")




#


# Common style settings
style = {
    "fg": "white",
    "bg": "#4a7a8c",
    "selectcolor": "#2f4f4f",
    "activebackground": "#355e72",
    "activeforeground": "white"
}

# Radiobuttons with color
tk.Radiobutton(root, text="pcm", variable=stream_label, value="PCM", **style).grid(row=17, column=0, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="commerce", variable=stream_label, value="COMMERCE", **style).grid(row=18, column=0, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="art", variable=stream_label, value="ART", **style).grid(row=19, column=0, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="pcb", variable=stream_label, value="PCB", **style).grid(row=20, column=0, padx=10, pady=5, sticky="w")



terms_var = tk.BooleanVar()
terms_check = tk.Checkbutton(root, text="I accept the Terms and Conditions",font=("Arial", 10, "bold"),variable=terms_var)
terms_check.grid(row=21, column=0, padx=10, pady=(10, 0), sticky="w")

# Submit button to show selection
style={"fg": "white",
    "bg": "#4a7a8c",
 }
submit_button = tk.Button(root, text="Submit",**style, command=submit_form)
submit_button.grid(row=22, column=0, pady=(10, 10))

root.mainloop()
