import json
import os  
import tkinter as tk
from tkinter import Tk

dataBase = {}
root = Tk()

def settingroot():
    root.geometry("1000x600")
    root.title("JSON with Tkinter")

def readData():
    global dataGet
    if not os.path.exists("data.json"):
        with open("data.json", "w") as f:
            json.dump(dataBase, f, indent=4)
        return dataBase  
    else:
        with open("data.json", "r") as f:
            dataGet = json.load(f)
            dataLabel.config(text=dataGet)
        return dataGet

def sendData(dataGet):
    with open("data.json", "w") as f:
        json.dump(dataGet, f, indent=4)

def cls():
    os.system("cls")

def showEntry():
    readData()
    key = entry.get()
    value = entry2.get()
    
    if value.isdigit():
        value = int(value)
    else:
        value = str(value)

    existingData = readData()
    
    if key not in existingData:
        if key.replace(' ','') or value.replace(' ',''):
            char = " ✔"
            existingData[key] = value
        else:
            char = " ❌"
            
    else:
        char = " ❌"

    entry_text.config(text="Key " + key + char)
    entry2_text.config(text="Value " + str(value) + char)
    sendData(existingData) 

settingroot()

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, padx=5, pady=10)

entry2 = tk.Entry(root, width=20)
entry2.grid(row=0, column=1, padx=5, pady=10)

entry_button = tk.Button(root, text="Send", command=showEntry, width=20)
entry_button.grid(row=1, column=0, columnspan=2, pady=20)

entry_text = tk.Label(root, text="Key: ")
entry_text.grid(row=2, column=0, pady=10)

entry2_text = tk.Label(root, text="Value: ")
entry2_text.grid(row=2, column=1, pady=10)

dataLabel = tk.Label(root, text="")
dataLabel.grid(row=3, column=0, columnspan=2)

buttonCls = tk.Button(root, text="Clean Terminal", command=cls)
buttonCls.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()

if os.path.exists("data.json"):
    os.remove("data.json")