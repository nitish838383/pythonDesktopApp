import tkinter as tk
from tkinter import messagebox
import requests


def calculate_totals():
    try:
        quantity = float(quantityEntry.get())
        price = float(priceEntry.get())
        discount_percent = float(discountEntry.get())


        subtotal = quantity * price

        discount_amount = subtotal * (discount_percent / 100)
        discounted_total = subtotal - discount_amount

        gst = discounted_total * 0.18
        grand_total = discounted_total + gst

        # Subtotal
        subtotalEntry.delete(0, tk.END)
        subtotalEntry.insert(0, f"{subtotal:.2f}")

        # Total after discount
        totalEntry.delete(0, tk.END)
        totalEntry.insert(0, f"{discounted_total:.2f}")

        # GST
        gstEntry.delete(0, tk.END)
        gstEntry.insert(0, f"{gst:.2f}")

        # Grand Total
        grandtotalEntry.delete(0, tk.END)
        grandtotalEntry.insert(0, f"{grand_total:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for quantity, price, and discount.")


def submit_form():
    # Get form data
    productname = productnameEntry.get()
    productcode = productcodeEntry.get()
    quantity = quantityEntry.get()
    price = priceEntry.get()
    discount = discountEntry.get().strip()  # Fixed the error
    subtotal = subtotalEntry.get().strip()  # Fixed the error
    total = totalEntry.get()
    gst = gstEntry.get()
    grandtotal = grandtotalEntry.get()

    # Prepare data for API
    form_data = {
        "productname": productname,
        "productcode": productcode,
        "quantity": quantity,
        "price": price,
        "discount": discount,
        "subtotal": subtotal,  # new
        "total": total,
        "gst": gst,
        "grandtotal": grandtotal,
    }

    # Google Apps Script Web App URL
    url = "https://script.google.com/macros/s/AKfycbwuC7l5_07TZOcKg9yETZSZh1QPiqxzp-MfRNjzQCx2YDOU8Tfix9xxdlnZrnhe3BlM/exec"

    try:
        print("Sending data:", form_data)
        response = requests.post(url, json=form_data)
        print("Response status code:", response.status_code)
        print("Response content:", response.text)

        if response.status_code == 200:
            messagebox.showinfo("Success", "Form submitted successfully!")
            # Clear form
            productnameEntry.delete(0, tk.END)
            productcodeEntry.delete(0, tk.END)
            quantityEntry.delete(0, tk.END)
            priceEntry.delete(0, tk.END)
            totalEntry.delete(0, tk.END)
            gstEntry.delete(0, tk.END)
            grandtotalEntry.delete(0, tk.END)
        else:
            messagebox.showerror("Error",
                                 f"Failed to submit form.\nStatus code: {response.status_code}\nResponse: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        print("Full error details:", e)


# GUI Setup
root = tk.Tk()

root.title("GROCERY CHECKOUT")
root.geometry("900x800")
root.config(pady="5", padx="5")
root.configure(bg="yellow")

title_label = tk.Label(root, text="GROCERY CHECKOUT", fg="white", bg="green", font=("Helvetica", 24, "bold"))
title_label.grid(pady=20)

# Labels and Entries
productnameLabel = tk.Label(root, text="PRODUCT NAME", font=("Arial", 10, "bold"), fg="red")
productnameLabel.grid(row=1, column=0, sticky="w")

productnameEntry = tk.Entry(root, width=30)
productnameEntry.grid(row=1, column=1, pady=(20, 20))

productcodeLabel = tk.Label(root, text="PRODUCT CODE", font=("Arial", 10, "bold"), fg="red")
productcodeLabel.grid(row=2, column=0, sticky="w")

productcodeEntry = tk.Entry(root, width=30)
productcodeEntry.grid(row=2, column=1, pady=(20, 20))

quantityLabel = tk.Label(root, text="QUANTITY NUMBER", font=("Arial", 10, "bold"), fg="red")
quantityLabel.grid(row=3, column=0, sticky="w")

quantityEntry = tk.Entry(root, width=30)
quantityEntry.grid(row=3, column=1, pady=(20, 20))

priceLabel = tk.Label(root, text="PRODUCT PRICE", font=("Arial", 10, "bold"), fg="red")
priceLabel.grid(row=4, column=0, sticky="w")

priceEntry = tk.Entry(root, width=30)
priceEntry.grid(row=4, column=1, pady=(20, 20))

discountLabel = tk.Label(root, text="DISCOUNT", font=("Arial", 10, "bold"), fg="red")
discountLabel.grid(row=5, column=0, sticky="w")

discountEntry = tk.Entry(root, width=30)
discountEntry.grid(row=5, column=1, pady=(20, 20))


totalLabel = tk.Label(root, text="TOTAL", font=("Arial", 10, "bold"), fg="red")
totalLabel.grid(row=6, column=0, sticky="w")

totalEntry = tk.Entry(root, width=30)
totalEntry.grid(row=6, column=1, pady=(20, 20))

subtotalLabel = tk.Label(root, text="SUBTOTAL", font=("Arial", 10, "bold"), fg="red")
subtotalLabel.grid(row=7, column=0, sticky="w")

subtotalEntry = tk.Entry(root, width=30)
subtotalEntry.grid(row=7, column=1, pady=(10, 0))

gstLabel = tk.Label(root, text="GST", font=("Arial", 10, "bold"), fg="red")
gstLabel.grid(row=8, column=0, sticky="w")

gstEntry = tk.Entry(root, width=30)
gstEntry.grid(row=8, column=1, pady=(20, 20))

grandtotalLabel = tk.Label(root, text="GRAND TOTAL", font=("Arial", 10, "bold"), fg="red")
grandtotalLabel.grid(row=9, column=0, sticky="w")

grandtotalEntry = tk.Entry(root, width=30)
grandtotalEntry.grid(row=9, column=1, pady=(20, 20))

calculate_Button = tk.Button(root, text="Calculate", font=("Arial", 12, "bold"), bg="#00796b", fg="white", padx=10,
                             pady=5, command=calculate_totals)
calculate_Button.grid(row=10, column=0, pady=10)

submit_btn = tk.Button(root, text="Submit", font=("Arial", 12, "bold"), bg="#00796b", fg="white", padx=10, pady=5,
                       command=submit_form)
submit_btn.grid(row=10, column=1, pady=20)

root.mainloop()
