import tkinter as tk
from project import clear_entry  # Assuming this is a valid function

root = tk.Tk()
root.title("3x3 Button Grid - pack()")
root.geometry("500x500")

# Entry field
entry = tk.Entry(root, font=("Arial", 20), justify="right", width=25)
entry.pack(pady=20, ipady=10)

# Button functions
def insert(value):
    entry.insert(tk.END, value)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def percent():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(value / 100))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)
    entry.insert(tk.END, "clean")

# Button layout
buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", "%", "=", "/"],
    ["Clear"]
]

# Button rendering
button_frame = tk.Frame(root)
button_frame.pack()

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(pady=5)
    for label in row:
        if label == "=":
            cmd = calculate
        elif label == "%":
            cmd = percent
        elif label == "Clear":
            cmd = clear_entry  # From project module
        else:
            cmd = lambda val=label: insert(val)
        tk.Button(row_frame, text=label, width=10, height=3, command=cmd).pack(side="left", padx=5)

root.mainloop()
