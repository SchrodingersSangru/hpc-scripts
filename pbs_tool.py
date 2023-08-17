import tkinter as tk
from tkinter import messagebox
import subprocess

def submit_job():
    job_script = script_text.get("1.0", tk.END)
    try:
        process = subprocess.Popen(["bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out, err = process.communicate(input=job_script, timeout=10)
        if process.returncode == 0:
            messagebox.showinfo("Job Submission", "Job submitted successfully.")
        else:
            messagebox.showerror("Job Submission Error", f"Job submission failed:\n{err}")
    except subprocess.TimeoutExpired:
        messagebox.showerror("Job Submission Error", "Job submission timed out.")

# Create the GUI
root = tk.Tk()
root.title("Job Monitoring Tool")

script_label = tk.Label(root, text="Enter Job Script:")
script_label.pack()

script_text = tk.Text(root, height=10, width=40)
script_text.pack()

submit_button = tk.Button(root, text="Submit Job", command=submit_job)
submit_button.pack()

root.mainloop()
