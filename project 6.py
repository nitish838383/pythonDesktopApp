import tkinter as tk
from tkinter import messagebox
import requests
def submit_form():
    if not terms_var.get():
        messagebox.showwarning("Warning", "THIS INFORMATION IS ONLY FOR PROJECT OF DEPARTMENT  .")
        return
    studentname = studentnameEntry.get()
    lastschoolname = lastschoolnameEntry.get(),
    schoolid = schoolidEntry.get(),
    dateofbirth = dateofbirthEntry.get(),
    addressname = addressnameEntry.get().strip(),  # Fixed the error
    emailid = emailidEntry.get().strip(),  # Fixed the error
    markpercent = markpercentEntry.get()
    admissionformno = admissionformnoEntry.get()  # fixed variable name
    phoneno = phonenoEntry.get()

    # Prepare data for API
    form_data = {
        "studentname": studentname,
        "lastschoolname": lastschoolname,
        "schoolid": schoolid,
        "dateofbirth": dateofbirth,
        "addressname": addressname,
        "emailid": emailid,
        "markpercent": markpercent,
        "admissionformno": admissionformno,
        "phoneno": phoneno,
    }

    # Google Apps Script Web App URL
    url="https://script.google.com/macros/s/AKfycbzWTzhPAVAsUCzFGpHK_KPxwxh_MTrQVi2sMTYjl9pXwZMV8WV8M-80_4Gykn6lr0fiIg/exec"
    try:
        print("Sending data:", form_data)
        response = requests.post(url, json=form_data)
        print("Response status code:", response.status_code)
        print("Response content:", response.text)

        if response.status_code == 200:
            messagebox.showinfo("Success", "Form submitted successfully!")
            studentnameEntry.delete(0, tk.END)
            lastschoolnameEntry.delete(0, tk.END)
            schoolidEntry.delete(0, tk.END)
            dateofbirthEntry.delete(0, tk.END)
            addressnameEntry.delete(0, tk.END)
            emailidEntry.delete(0, tk.END)
            markpercentEntry.delete(0, tk.END)
            admissionformnoEntry.delete(0, tk.END)
            phonenoEntry.delete(0, tk.END)

        else:
            messagebox.showerror("Error",
                                 f"Failed to submit form.\nStatus code: {response.status_code}\nResponse: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        print("Full error details:", e)


root = tk.Tk()
root.title("PROJECT OF DEPARTMENT")
root.geometry("700x800")
root.configure(bg="yellow")

tk.Label(root,text="STUDENT NAME.").pack(pady=10)
studentnameEntry=tk.Entry(root)
studentnameEntry.pack()

tk.Label(root,text=" LAST SCHOOL NAME").pack(pady=10)
lastschoolnameEntry=tk.Entry(root)
lastschoolnameEntry.pack()

tk.Label(root,text="SCHOOL ID").pack(pady=10 )
schoolidEntry=tk.Entry(root)
schoolidEntry.pack()

tk.Label(root,text="DATE OF BIRTH.").pack(pady=5)
dateofbirthEntry=tk.Entry(root)
dateofbirthEntry.pack()

tk.Label(root,text="ADDRESS NAME.").pack(pady=5)
addressnameEntry=tk.Entry(root)
addressnameEntry.pack()

tk.Label(root,text="E-MAIL ID .").pack(pady=5)
emailidEntry=tk.Entry(root)
emailidEntry.pack()

tk.Label(root,text="MARK PERCENT.").pack(pady=5)
markpercentEntry=tk.Entry(root)
markpercentEntry.pack()

tk.Label(root,text="ADMISSION FORM NO.").pack(pady=5)
admissionformnoEntry=tk.Entry(root)
admissionformnoEntry.pack()

tk.Label(root,text="PHONE NO.").pack(pady=5)
phonenoEntry=tk.Entry(root)
phonenoEntry.pack()

terms_var = tk.BooleanVar()
terms_check = tk.Checkbutton(root, text="I accept the Terms and Conditions",font=("Arial", 10, "bold"),variable=terms_var)
terms_check.pack(pady=10)

submit_btn = tk.Button(root, text="Submit", font=("Arial", 12, "bold"), bg="#00796b", fg="white", padx=10, pady=5,
                       command=submit_form)
submit_btn.pack(pady=10)


root.mainloop()
