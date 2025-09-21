import tkinter as tk
from tkinter import messagebox

# Conversion Functions
def celsius_to_fahrenheit():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result = f"{celsius}°C = {fahrenheit:.2f}°F"
        history.append(result)
        lbl_result.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric value.")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result = f"{fahrenheit}°F = {celsius:.2f}°C"
        history.append(result)
        lbl_result.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric value.")

def show_history():
    if history:
        history_str = "\n".join(history)
        messagebox.showinfo("Conversion History", history_str)
    else:
        messagebox.showinfo("Conversion History", "No conversions yet.")

# Main Window
root = tk.Tk()
root.title("🌡️ Temperature Converter")
root.geometry("400x300")
root.resizable(False, False)

history = []

# UI Elements
lbl_title = tk.Label(root, text="🌡️ Temperature Converter", font=("Arial", 16, "bold"))
lbl_title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

btn_c_to_f = tk.Button(frame_buttons, text="C → F", font=("Arial", 12), command=celsius_to_fahrenheit, width=10)
btn_c_to_f.grid(row=0, column=0, padx=5)

btn_f_to_c = tk.Button(frame_buttons, text="F → C", font=("Arial", 12), command=fahrenheit_to_celsius, width=10)
btn_f_to_c.grid(row=0, column=1, padx=5)

btn_history = tk.Button(root, text="📜 Show History", font=("Arial", 12), command=show_history)
btn_history.pack(pady=10)

lbl_result = tk.Label(root, text="Enter a value and choose a conversion", font=("Arial", 12), fg="blue")
lbl_result.pack(pady=20)

# Run the GUI
root.mainloop()

