import tkinter as tk

# Function to update the input field
def on_button_click(value):
    entry_field.insert(tk.END, value)

# Function to clear the input field
def clear_field():
    entry_field.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry_field.get())  # Evaluate the expression
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, result)
    except Exception:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="lightgray")

# Entry Field
entry_field = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify="right")
entry_field.pack(pady=10, fill="both")

# Buttons Layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Create Buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for char in row:
        if char == "=":
            btn = tk.Button(frame, text=char, font=("Arial", 18), bg="green", fg="white",
                            command=calculate)
        elif char == "C":
            btn = tk.Button(frame, text=char, font=("Arial", 18), bg="red", fg="white",
                            command=clear_field)
        else:
            btn = tk.Button(frame, text=char, font=("Arial", 18),
                            command=lambda c=char: on_button_click(c))

        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

# Run the application
root.mainloop()
