import tkinter as tk
from tkinter import ttk
import operator


def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    selected_operator = operator_dict[operator_var.get()]
    result.set(selected_operator(num1, num2))


root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='#f0f0f0')


label_num1 = tk.Label(root, text="Enter the first number:", bg='#f0f0f0')
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter the second number:", bg='#f0f0f0')
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()


operator_var = tk.StringVar()
operator_var.set('+')
operator_label = tk.Label(root, text="Select operator:", bg='#f0f0f0')
operator_label.pack()
operator_dropdown = ttk.Combobox(root, textvariable=operator_var, values=['+', '-', '*', '/'])
operator_dropdown.pack()


calculate_button = tk.Button(root, text="Calculate", command=calculate, bg='#4caf50', fg='white')
calculate_button.pack()


result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, bg='#f0f0f0', font=('Arial', 14, 'bold'))
result_label.pack()


operator_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


root.mainloop()
