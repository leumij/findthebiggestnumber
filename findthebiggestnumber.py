# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.

import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk

# pseudocode

# ask user 3 number for input
def find_greatest():
    try:
        number_one = int(entry_one.get())
        number_two = int(entry_two.get())
        number_three = int(entry_three.get())

# find the greatest value
        if number_one > number_two and number_one > number_three:
            greatest = number_one
        elif number_two > number_one and number_two > number_three:
            greatest = number_two
        else:
            greatest = number_three

# print the biggest number
         print("The greatest among the numbers you have entered {},{} and {} is number{}" .format(number_one,number_two,number_three, greatest))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Find the Greatest Number")
root.geometry("400x300")
root.configure(bg="#F2F2F2")