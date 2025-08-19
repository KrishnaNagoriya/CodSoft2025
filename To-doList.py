import tkinter as tk
from tkinter import messagebox
import os

# Load tasks from a file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for line in f:
                task, status = line.strip().rsplit("::", 1)
                task_list.insert(tk.END, task)
                if status == "done":
                    task_list.itemconfig(tk.END, {'fg': 'gray'})

# Save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as f:
        for i in range(task_list.size()):
            task = task_list.get(i)
            status = "done" if task_list.itemcget(i, 'fg') == 'gray' else "pending"
            f.write(f"{task}::{status}\n")

# Add task
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# Delete selected task
def delete_task():
    try:
        selected = task_list.curselection()[0]
        task_list.delete(selected)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Mark task as complete
def complete_task():
    try:
        selected = task_list.curselection()[0]
        task = task_list.get(selected)
        task_list.delete(selected)
        task_list.insert(selected, task)
        task_list.itemconfig(selected, {'fg': 'gray'})
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark complete.")

# Main GUI
root = tk.Tk()
root.title("To-Do List App")

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add Task", width=10, command=add_task)
add_button.pack(side=tk.LEFT)

# Task List
task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

delete_button = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)
delete_button.grid(row=0, column=0, padx=5)

complete_button = tk.Button(btn_frame, text="Mark Complete", width=12, command=complete_task)
complete_button.grid(row=0, column=1, padx=5)

# Load tasks when app starts
load_tasks()

root.mainloop()
