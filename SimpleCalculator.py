import tkinter as tk
import threading

# Function to update the expression in the entry box
def update_expression(symbol):
    global reset_display
    if reset_display:
        if symbol in ('+', '-', '×', '÷'):
            current_text = expression_var.get()
            expression_var.set(current_text + symbol)
        else:
            expression_var.set(symbol)
        reset_display = False
    else:
        current_text = expression_var.get()
        expression_var.set(current_text + symbol)

# Function to clear the entry box
def clear_expression():
    expression_var.set("")
    global reset_display
    reset_display = False

# Function to evaluate the expression
def calculate_expression():
    global reset_display
    try:
        expression = expression_var.get()
        expression = expression.replace('×', '*').replace('÷', '/')  # Replace symbols with actual operators
        result = eval(expression)  # Using eval to evaluate the mathematical expression
        expression_var.set(str(result))
        reset_display = True  # Set flag to clear on next input unless an operator is pressed
    except Exception as e:
        expression_var.set("Error")
        reset_display = True

# Function to run the calculation in a separate thread
def run_calculation():
    threading.Thread(target=calculate_expression).start()

# Set up the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Variable to hold the expression and reset flag
expression_var = tk.StringVar()
reset_display = False

# Display entry box
entry = tk.Entry(root, textvariable=expression_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Creating buttons
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=run_calculation)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
                           command=lambda t=text: update_expression(t))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 18), command=clear_expression)
clear_button.grid(row=5, column=0, columnspan=2)

# Run the main loop
root.mainloop()
