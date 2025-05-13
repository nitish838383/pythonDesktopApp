import tkinter as tk

from tkinter import messagebox

import requests

import json


def submit_form():
    if not terms_var.get():
        messagebox.showwarning("Warning", "THIS INFORMATION IS ONLY FOR TOKEN NUMBER.")
        return
    # Get form data
    name = nameEntry.get()
    disease = diseaseEntry.get()
    address = addressEntry.get()
    mobile=mobileEntry.get()
    blood = blood_label.get()
    token=tokenEntry.get()

    # Basic input validation (optional)
    if not name or not mobile or not token:
        messagebox.showerror("Error", "Name, Mobile Number, and Token Number are required.")
        return

    # Validate inputs

    # Prepare data for API
    form_data = {
        "name": name,
        "blood": blood,
        "disease":disease,
        "address":address,
        "mobile":mobile,
        "Token":token,
    }

    # Google Apps Script Web App URL
    url="https://script.google.com/macros/s/AKfycbxyhSoRApZ16sHdilFxS4DOC1hp7LldcYPD0_W6DXsF7yUTMim2K0U8wUz3mqndDDPacw/exec"

    try:
        print("Sending data:", form_data)  # Debug print
        response = requests.post(url, json=form_data)
        print("Response status code:", response.status_code)  # Debug print
        print("Response content:", response.text)  # Debug print

        if response.status_code == 200:
            messagebox.showinfo("Success", "Form submitted successfully!")
            # Clear form
            nameEntry.delete(0, tk.END)
            diseaseEntry.delete(0, tk.END)
            blood_label.set("A+")  # Reset to default
        else:
            messagebox.showerror("Error", f"Failed to submit form.\nStatus code: {response.status_code}\nResponse: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        print("Full error details:", e)  # Debug print




root = tk.Tk()


root.title("Medical Enquring Form")
root.geometry("500x500")
root.config(padx=30, pady=30)

root.geometry("900x900")
root.configure(bg="blue")



nameLabel = tk.Label(root, text="Patient Name",font=("Arial",10,"bold"),fg="red")
nameLabel.grid(row=0, column=0, sticky="w")

nameEntry = tk.Entry(root, width=30)
nameEntry.grid(row=0, column=1, pady=(20, 20))


diseaseLabel = tk.Label(root, text="Disease",font=("Arial",10,"bold"),fg="red")
diseaseLabel.grid(row=2, column=0, sticky="w")

diseaseEntry = tk.Entry(root, width=30)
diseaseEntry.grid(row=2, column=1, pady=(20, 20))

addressLabel = tk.Label(root, text="Address",font=("Arial",10,"bold"),fg="red")
addressLabel.grid(row=3, column=0, sticky="w")

addressEntry = tk.Entry(root, width=30)
addressEntry.grid(row=3, column=1, pady=(20, 20))

mobileLabel = tk.Label(root, text="Mobile Number",font=("Arial",10,"bold"),fg="red")
mobileLabel.grid(row=4, column=0, sticky="w")

mobileEntry = tk.Entry(root, width=30)
mobileEntry.grid(row=4, column=1, pady=(20, 20))

emergenceLabel = tk.Label(root, text="Emergence Number",font=("Arial",10,"bold"),fg="red")
emergenceLabel.grid(row=5, column=0, sticky="w")

emergenceEntry = tk.Entry(root, width=30)
emergenceEntry.grid(row=5, column=1, pady=(20, 20))


tokenLabel = tk.Label(root, text="Token Number",font=("Arial",10,"bold"),fg="red")
tokenLabel.grid(row=6, column=0, sticky="w")

tokenEntry = tk.Entry(root, width=30)
tokenEntry.grid(row=6, column=1, pady=(20, 20))

# Variable to hold selected stream
blood_label = tk.StringVar()


radio_frame = tk.Label(root, text="Blood Group",font=("Arial",10,"bold"),fg="red")
radio_frame.grid(row=7, column=0,sticky="w",pady="10")

blood_radio_op = tk.Radiobutton(root, text="O+", variable=blood_label, value="O+", )
blood_radio_op.grid(row=7, column=1, padx=5, pady=5, sticky="w")

blood_radio_op = tk.Radiobutton(root, text="O-", variable=blood_label, value="O-")
blood_radio_op.grid(row=7, column=2, padx=5, pady=5, sticky="w")

blood_radio_op = tk.Radiobutton(root, text="B+", variable=blood_label, value="B+")
blood_radio_op.grid(row=7, column=3, padx=5, pady=5, sticky="w")

blood_radio_op = tk.Radiobutton(root, text="B-", variable=blood_label, value="B-")
blood_radio_op.grid(row=7, column=4, padx=5, pady=5, sticky="w")

style={"fg": "#000000",
    "bg": "#FFECA1",
       }
terms_var = tk.BooleanVar()
terms_check = tk.Checkbutton(root, text="   THIS INFORMATION IS ONLY FOR TOKEN NUMBER",**style,font=("Arial", 10, "bold"),variable=terms_var)
terms_check.grid(row=21, column=0, padx=20, pady=(20, 0), sticky="w")

# Submit button to show selection
style={"fg": "#000000",
    "bg": "#FFECA1",
       }
submit_button = tk.Button(root, text="Submit",**style, command=submit_form)
submit_button.grid(row=22, column=0, pady=(20, 20))

root.mainloop()
