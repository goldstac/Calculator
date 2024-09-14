import customtkinter as ctk
import tkinter as tk

# Function to handle button click
def button_click(value):
    current = entry.get()
    if value == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Initialize the main window
app = ctk.CTk()
app.title("Calculator")
app.geometry("300x400")

# Entry widget for displaying expressions and results
entry = ctk.CTkEntry(app, font=("Arial", 18))
entry.pack(pady=10, padx=10, fill="x")

# Frame to hold the buttons
button_frame = ctk.CTkFrame(app)
button_frame.pack()

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create and place buttons
row_val = 0
col_val = 0
for button in buttons:
    b = ctk.CTkButton(button_frame, text=button, command=lambda b=button: button_click(b), width=60, height=60)
    b.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
app.mainloop()
