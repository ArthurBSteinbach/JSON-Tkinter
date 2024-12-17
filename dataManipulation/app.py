import json
import os
import tkinter as tk
from tkinter import Tk

data_base = {
    "content": {
        "test1": {
            "property1": "Value1"
        }
    }
}

root = Tk()

    
def settingRoot():
    root.title("JSON with Tkinter")
    root.geometry("500x500")
    root.config(bg="gray")

def checkData():
    global data_get
    if not os.path.exists("dataManipulation/data.json"):
        with open("dataManipulation/data.json", "w") as f:
            json.dump(data_base, f, indent=4)
    else:
        with open("dataManipulation/data.json", "r") as f:
            data_get = json.load(f)

def sendData(): 
    checkData()
    data_get["content"]["test1"]["property2"] = "newValue2"

    #sends data
    with open("dataManipulation/data.json", "w") as f:
        json.dump(data_get, f, indent=4)

settingRoot()
sendData()

data_label = tk.Label(root, text=data_get , font=("Arial",15))
data_label.pack

os.system('cls')

root.mainloop()