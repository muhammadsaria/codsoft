import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(length_entry.get())
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    generated_password.set("Your Password: " + "".join(s[0:plen]))


root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Enter the desired length for password:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()


generated_password = tk.StringVar()
password_label = tk.Label(root, textvariable=generated_password)
password_label.pack()


root.mainloop()

