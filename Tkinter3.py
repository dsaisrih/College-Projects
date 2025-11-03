import tkinter as tk
from tkinter import messagebox

def validate():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    # Validation 1: Name should not be empty
    if name == "":
        messagebox.showerror("Error", "Name cannot be empty!")
        return

    # Validation 2: Email should contain '@'
    if "@" not in email:
        messagebox.showerror("Error", "Email must contain '@' symbol!")
        return

    # Validation 3: Age should be numeric
    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a number!")
        return

    # If all validations pass
    messagebox.showinfo("Success", "Registration Successful!")

# Main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("300x250")

# Labels and Entries
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack()

# Submit Button
tk.Button(root, text="Submit", command=validate).pack(pady=20)

root.mainloop()