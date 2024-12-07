import json
import os
import tkinter as tk
from tkinter import Tk

dataBase = {}
root = Tk()

def settingRoot():
    root.geometry("1000x1000")
    root.title("JSON with Tkinter")

def verifyDataFile():
    global dataGet
    if not os.path.exists("dataLibrary/data.json"):
        with open("dataLibrary/data.json", "w") as f:
            json.dump(dataBase, f, indent=4)
            labelData.config(text="no data get")
    else:
        with open("dataLibrary/data.json", "r") as f:
            dataGet = json.load(f)
            dataGet = str(dataGet).replace("{", "").replace("}", "")
            labelData.config(text=dataGet)
            return dataGet

settingRoot()

labelTop = tk.Label(root, text="DATA LIBRARY", font=("Arial", 20, "bold"))
labelTop.grid(row=0, columnspan=2, padx=20, pady=20)

labelData = tk.Label(root, text='', font=("Arial", 20))
labelData.grid(row=1, columnspan=2, padx=20, pady=20)

verifyDataFile()

keys = dataBase.keys()

label = tk.Label(root, text=keys)
label.grid(row=2, columnspan=2, padx=20, pady=20)

os.system('cls')
root.mainloop()