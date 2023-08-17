import tkinter as tk
from tkinter import messagebox
import psutil

def get_process_status(pid):
    try:
        process = psutil.Process(pid)
        return process.status()
    except psutil.NoSuchProcess:
        return "Process not found"
    except psutil.AccessDenied:
        return "Access denied"

def check_process_status():
    pid = int(pid_entry.get())
    status = get_process_status(pid)
    status_label.config(text=f"Process Status: {status}")

# Create the GUI
root = tk.Tk()
root.title("Process Status Checker")

pid_label = tk.Label(root, text="Enter Process PID:")
pid_label.pack()

pid_entry = tk.Entry(root)
pid_entry.pack()

check_button = tk.Button(root, text="Check Status", command=check_process_status)
check_button.pack()

status_label = tk.Label(root, text="Process Status: Not checked yet")
status_label.pack()

root.mainloop()

