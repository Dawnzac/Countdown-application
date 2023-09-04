import tkinter as tk
from tkinter import ttk
from datetime import datetime
import os
import shutil
import sys
import subprocess
import getpass
import ctypes


event_date = datetime(2023, 9, 5)

def update_countdown_label():
    current_date = datetime.now()
    remaining_days = (event_date - current_date).days + 1
    countdown_label.config(text=f"Days remaining till NABH Inspection : {remaining_days} days")
    if remaining_days <= 0:
        self_destruct()

# def self_destruct():
#     try:
#         # Get the path to the current script
#         script_path = os.path.abspath(sys.argv[0])

#         # Check if running with admin rights
#         if ctypes.windll.shell32.IsUserAnAdmin():
#             # Running with admin rights, so delete the script file
#             os.remove(script_path)
#         else:
#             # Request admin rights and then attempt deletion
#             ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script_path, None, 1)
#             os.remove(script_path)
#         app.quit()
#     except Exception as e:
#         print(f"Self-destruction failed: {e}")

def self_destruct():
    try:
        script_path = os.path.join(startup_folder, "countdown.exe")
        os.remove(script_path)
        app.quit()
    except Exception as e:
        
        print(f"Self-destruction failed: {e}")

def open_startup_folder():
    subprocess.Popen(["explorer", startup_folder])

startup_folder = os.path.join("C:\\Users", getpass.getuser(), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
if os.path.abspath(sys.argv[0]).lower() != os.path.join(startup_folder, "countdown.py").lower():
    # Copy the script to the Windows Startup folder
    shutil.copy2(sys.argv[0], os.path.join(startup_folder, "countdown.exe"))
    
app = tk.Tk()
app.title("NABH Inspection Countdown")

style = ttk.Style()
style.configure("Countdown.TLabel", font=("Helvetica", 24), padding=10)

countdown_label = ttk.Label(app, text="", style="Countdown.TLabel")
countdown_label.pack()

open_folder_button = ttk.Button(app, text="Open Startup Folder", command=open_startup_folder)
open_folder_button.pack()

update_countdown_label()

app.mainloop()
