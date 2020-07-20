import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.title("DealMachine Script")

root.geometry('300x350')

frame = tk.Frame(master=root)
frame.pack()

filePath = ""

pathLabel = tk.Label(frame, text=filePath, bg = "white", width = 30)
pathLabel.pack(pady = 15)

def chooseFile():
    filePath = filedialog.askopenfilename()
    pathLabel.configure(text = filePath)


propertyTag = tk.StringVar(root)
propertyTag.set("Choose a tag") # default value

tagMenu = tk.OptionMenu(root, propertyTag, "Choose a tag", "Absentee", "Distressed").pack()

chooseFileButton = tk.Button(master=frame, text = "Choose File", command = chooseFile)
chooseFileButton.pack()

loginUsernameGet = tk.StringVar(root)
loginPasswordGet = tk.StringVar(root)

label1 = tk.Label(frame, text = "Username").pack(pady = 10)
loginUsernameEntry = tk.Entry(master=frame, textvariable = loginUsernameGet).pack()

label2 = tk.Label(frame, text = "Password").pack(pady = 10)
loginPasswordEntry = tk.Entry(master=frame, textvariable = loginPasswordGet, show = "*").pack()

def startButton():
    loginUsername = loginUsernameGet.get()
    loginPassword = loginPasswordGet.get()
    runEntry(loginUsername, loginPassword, propertyTag, filePath)



startEntryButton = tk.Button(master=frame, text = "Start Entry", command = startButton).pack(pady = 10)
root.mainloop()
