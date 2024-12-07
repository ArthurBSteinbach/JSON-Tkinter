import json
import os
import tkinter as tk
from tkinter import Tk

dataBase = {}
root = Tk()

def setting_root():
    root.geometry("270x600")
    root.title("JSON with Tkinter")

def read_data():
    global dataGet
    if not os.path.exists("keyValueDatabase/data.json"):
        with open("data.json", "w") as f:
            json.dump(dataBase, f, indent=4)
        return dataBase  
    else:
        with open("keyValueDatabase/data.json", "r") as f:
            dataGet = json.load(f)
            dataLabel.config(text=dataGet)
        return dataGet

def send_data(dataGet):
    with open("keyValueDatabase/data.json", "w") as f:
        json.dump(dataGet, f, indent=4)
        dataLabel.config(text=dataGet)
        return dataGet
        
def clear_terminal():
    os.system("cls")

def root_destroy():
    root.destroy()

def show_entry():
    read_data()
    key = entry.get().strip()
    value = entry2.get().strip()
    
    if value.isdigit():
        value = int(value)
    else:
        value = str(value)

    existing_data = read_data()
    
    if key and value:
        if key not in existing_data:
            existing_data[key] = value
            entry_button.config(bg="green", fg="white")
            char = " ✔"
        else:
            entry_button.config(bg="red", fg="white")
            char = " ❌"
    else:
        entry_button.config(bg="red", fg="white")
        char = " ❌"

    entry_text.config(text="Key: " + key + char)
    entry2_text.config(text="Value: " + str(value) + char)
    send_data(existing_data) 

setting_root()

jsonLabel = tk.Label(root, text="JSON REGISTROR\nDATABASE", font=("Arial", 12, "bold"))
jsonLabel.grid(row=0, columnspan=2, padx=5, pady=10)

entry = tk.Entry(root, width=20)
entry.grid(row=1, column=0, padx=5, pady=10)

entry2 = tk.Entry(root, width=20)
entry2.grid(row=1, column=1, padx=5, pady=10)

entry_button = tk.Button(root, text="Send", command=show_entry, width=20)
entry_button.grid(row=2, column=0, columnspan=2, pady=20)

entry_text = tk.Label(root, text="Key: ")
entry_text.grid(row=3, column=0, pady=10)

entry2_text = tk.Label(root, text="Value: ")
entry2_text.grid(row=3, column=1, pady=10)

dataLabel = tk.Label(root, text="")
dataLabel.grid(row=4, column=0, columnspan=2)

buttonCls = tk.Button(root, text="Clean Terminal", command=clear_terminal)
buttonCls.grid(row=5, column=0, columnspan=2, pady=30)

buttonExit = tk.Button(root, text="Exit", command=root_destroy, width=10)
buttonExit.grid(row=6, column=0, columnspan=2)

root.mainloop()