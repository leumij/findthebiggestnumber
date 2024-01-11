# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.

import tkinter as tk
from tkinter import messagebox

# ask user 3 number for input
def find_greatest():
    try:
        number_one = int(entry_one.get())
        number_two = int(entry_two.get())
        number_three = int(entry_three.get())

# find the greatest number
        
        if number_one > number_two and number_one > number_three:
            greatest = number_one
        elif number_two > number_one and number_two > number_three:
            greatest = number_two
        else:
            greatest = number_three

        result_label.config(text=f"The greatest among the numbers you have entered {number_one}, {number_two}, and {number_three} is {greatest}.")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Find the Greatest Number")
root.geometry("400x300")
root.configure(bg="#F2F2F2")

# Create and place widgets with a custom design
label_one = tk.Label(root, text="Enter your First Number:", bg="#F2F2F2", font=("Arial", 12))
label_one.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

entry_one = tk.Entry(root, font=("Arial", 12), relief=tk.FLAT, bd=2)
entry_one.grid(row=0, column=1, padx=10, pady=10)

label_two = tk.Label(root, text="Enter your Second Number:", bg="#F2F2F2", font=("Arial", 12))
label_two.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

entry_two = tk.Entry(root, font=("Arial", 12), relief=tk.FLAT, bd=2)
entry_two.grid(row=1, column=1, padx=10, pady=10)
