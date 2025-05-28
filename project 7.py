
import tkinter as tk
from tkinter import messagebox
import requests

# URL for Google Apps Script Web App
url = "https://script.google.com/macros/s/AKfycbwNUSVL0J7ZYUJaFkntxIDQ8FX2qybXveknc5-q7gI0UlRcEm4v5Kyk78vY643CGMgd/exec"

# Task list
tasks = ["Wake up", "running", "school", "tution"]

# Functions
def add_task():
    task = entry.get()
    if task != "":
        # Add to GUI
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

        # Send to Google Script
        form_data = {"task": task}
        try:
            print("Sending data:", form_data)
            response = requests.post(url, json=form_data)
            print("Response status code:", response.status_code)
            print("Response content:", response.text)

            if response.status_code == 200:
                messagebox.showinfo("Success", "Task submitted to Google Sheet!")
            else:
                messagebox.showerror("Error", f"Failed to submit task.\nStatus code: {response.status_code}\nResponse: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            print("Full error details:", e)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
        tasks.pop(task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

def clear_list():
    listbox.delete(0, tk.END)
    tasks.clear()

# UI Setup
root = tk.Tk()
root.configure(bg="pink")
root.title("Task Manager")

entry = tk.Entry(root, width=40)
entry.pack(padx=100, pady=20)

add_button = tk.Button(root, text="Add Task", font=("arial", 10, "bold"), bg="red", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", font=("arial", 10, "bold"), bg="red", command=remove_task)
remove_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All", font=("arial", 10, "bold"), bg="red", command=clear_list)
clear_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Load initial tasks
for item in tasks:
    listbox.insert(tk.END, item)

# Run the app
root.mainloop()

