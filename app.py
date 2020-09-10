import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = ( ("executables","*.exe"), ("all files","*.*") ))

    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg='grey')
        label.pack()

def runApps():
    for app in apps:
        os.system(app)

canvas = tk.Canvas(root, height=900, width=1200, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile= tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps= tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

root.mainloop()

with open('save.txt', 'w') as savefile:
    for app in apps:
        savefile.write(app + ',')