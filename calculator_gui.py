import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = a / b
        else:
            messagebox.showerror("Error", "Invalid operator")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x300")

tk.Label(root, text="Python Calculator",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="First number").pack()
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Select operator").pack()
operator_var = tk.StringVar(value="+")
tk.OptionMenu(root, operator_var, "+", "-", "*", "/").pack()

tk.Label(root, text="Second number").pack()
entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Button(root, text="Calculate",
          command=calculate).pack(pady=10)

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()