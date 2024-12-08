import json
import os
import tkinter as tk
from tkinter import Tk

dataBase = {}
root = Tk()

def settingRoot():
    root.geometry("1080x780")
    root.title("JSON with Tkinter")

def verifyDataFile():
    global dataGet
    if not os.path.exists("dataLibrary/data.json"):
        with open("dataLibrary/data.json", "w") as f:
            json.dump(dataBase, f, indent=4)
            labelData.config(text="no data get")
            labelKeys.config(text='no keys')
            labelValues.config(text='no values')
    else:
        with open("dataLibrary/data.json", "r") as f:
            dataGet = json.load(f)


            keys = list(dataGet.keys())
            values = list(dataGet.values())
    
            dataShow = '\n'.join(list(keys) + list(values))
            labelData.config(text=dataShow)

            labelKeys.config(text='\n'.join(keys))
            labelValues.config(text='\n'.join(values))

def sendData():
    value = entryValue.get().strip()
    key = entryKey.get().strip()
    verifyDataFile()
    
    if key and value:
        dataGet[key] = value
        with open("dataLibrary/data.json", "w") as f:
            json.dump(dataGet, f, indent=4) 
        verifyDataFile()
        buttonSend.config(bg=None)

    else:
        buttonSend.config(bg='red')

settingRoot()
# Row 0

labelTop = tk.Label(root, text="DATA LIBRARY", font=("Arial", 30, "bold"))
labelTop.grid(row=0, columnspan=2,pady=20)

#Row 1

labelInfoKeys = tk.Label(root, text="KEYS", font=("Arial",20, "bold")) # label saying keys
labelInfoKeys.grid(row=1,column=5)

labelInfoValues = tk.Label(root, text="VALUES", font=("Arial",20, "bold")) # label saying values
labelInfoValues.grid(row=1,column=4)

# Row 2

labelKeys = tk.Label(root, text='', font=("Arial",15)) # label with keys
labelKeys.grid(row=2,column=5,padx=200)

labelValues = tk.Label(root, text='', font=("Arial",15)) # label with values
labelValues.grid(row=2,column=4, padx=0)

entryKey = tk.Entry(root, width=30)
entryKey.grid(row=1,column=1)

entryValue = tk.Entry(root,width=30)
entryValue.grid(row=1,column=2)

buttonSend = tk.Button(root, text="SEND", command=sendData)
buttonSend.grid(row=5, columnspan=2, pady=20)

labelData = tk.Label(root, text='', font=("Arial", 20))
labelData.grid(row=6, columnspan=2, padx=20, pady=20)

verifyDataFile()

os.system('cls')
root.mainloop()