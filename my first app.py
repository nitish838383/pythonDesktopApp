import	tkinter	as	tk

from project import clear_entry

root = tk.Tk()
root.title("3x3 Button Grid - pack()")
root.geometry("500x500")

# Frame to hold the Entry at the top
top_frame = tk.Frame(root)
top_frame.pack(pady=10)


entry = tk.Entry(top_frame, font=("Arial", 20), justify="left", width=30,)
entry.pack(padx=10, pady=10, ipady=20)

def insert1():
    entry.insert(tk.END,"1")
def insert2():
    entry.insert(tk.END,"2")
def insert3():
    entry.insert(tk.END,"3")
def insert4():
    entry.insert(tk.END, "4")
def insert5():
    entry.insert(tk.END,"5")
def insert6():
    entry.insert(tk.END,"6")
def insert7():
    entry.insert(tk.END,"7")
def insert8():
    entry.insert(tk.END,"8")
def insert9():
    entry.insert(tk.END,"9")



# Frame to hold all button frames
button_frame = tk.Frame(root)
button_frame.pack()

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))
    entry.delete(0, tk.END)
    entry.insert(tk.END, "clear")
def percent():
    current = entry.get()
    if current:
            result = str(eval(current) / 100)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            entry.delete(0, tk.END)
            entry.insert(tk.END, "%")


# Create button rows
for i in range(6):
    row_frame = tk.Frame(button_frame)
    row_frame.pack(pady=5)

    for j in range(3):
        # Operator and control buttons
        if i == 3 and j == 0:
            btn_text = "+"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert1)
            button.pack(side="left", padx=5)
        elif i == 3 and j == 0:
            btn_text = "-"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert2)
            button.pack(side="left", padx=5)
        elif i == 3 and j == 0:
            btn_text = "*"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert3)
            button.pack(side="left", padx=5)
        elif i == 4 and j == 0:
            btn_text = "/"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert4)
            button.pack(side="left", padx=5)
        elif i == 4 and j == 0:
            btn_text = "Clear"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert5)
            button.pack(side="left", padx=5)
        elif i == 4 and j == 0:
            btn_text = "="
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert6)
            button.pack(side="left", padx=5)
        elif i == 6 and j == 0:
            btn_text = "%"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert7)
            button.pack(side="left", padx=5)
            for row in button:
                row_frame = tk.Frame(button_frame)
                row_frame.pack(pady=5)
                for label in row:
                    if label == "Clear":
                        cmd = clear_entry

                    elif label == "=":
                        cmd = calculate
                    elif label == "%":
                        cmd = percent
                    else:
                        cmd = lambda val=label: entry.insert
                    button = tk.Button(row_frame, text=label, width=10, height=3, command=cmd)
                    button.pack(side="left", padx=5)

            root.mainloop()