import tkinter as tk

# Function to do calculation
def do_calculation():
    num1 = entry1.get()
    num2 = entry2.get()
    operation = op.get()

    try:
        n1 = float(num1)
        n2 = float(num2)

        if operation == '+':
            result = n1 + n2
        elif operation == '-':
            result = n1 - n2
        elif operation == '*':
            result = n1 * n2
        elif operation == '/':
            if n2 == 0:
                result_label.config(text="Cannot divide by 0")
                return
            result = n1 / n2
        else:
            result_label.config(text="Choose operation")
            return

        result_label.config(text="Result: " + str(result))

    except:
        result_label.config(text="Enter valid numbers")

# Main Window
win = tk.Tk()
win.title("Simple Calculator")

# First number
tk.Label(win, text="First Number").pack()
entry1 = tk.Entry(win)
entry1.pack()

# Second number
tk.Label(win, text="Second Number").pack()
entry2 = tk.Entry(win)
entry2.pack()

# Operation dropdown
tk.Label(win, text="Select Operation").pack()
op = tk.StringVar()
op.set("+")  # default
tk.OptionMenu(win, op, "+", "-", "*", "/").pack()

# Calculate button
tk.Button(win, text="Calculate", command=do_calculation).pack(pady=10)

# Result label
result_label = tk.Label(win, text="Result: ")
result_label.pack()

# Run the window
win.mainloop()
