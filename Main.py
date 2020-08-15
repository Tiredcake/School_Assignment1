import tkinter as tk
from tkinter import ttk
ClassList = []

ClassPassword = {}

with open('sauce.txt') as f:
    for x in f.readlines():
        ClassList.append(x.strip())



with open('Data_Loginner.txt') as f:
    for x in f.readlines():
        a = x.split(',')
        ClassPassword[a[0]] = a[1].strip()


"""for x in ClassList:
    if x not in ClassPassword:
        print(x, "has not sign up yet\n")"""




class DiceThrower:
    def __init__(self):
        Screen = tk.Tk()
        Screen.geometry('1920x1080')
        Title = tk.Label(Screen, text='Welcome to SHUT THE DOOR', font=('Courier', 50,'bold'))
        Title.place(relx=0.25, rely=0.1)

        Start = tk.Button(Screen, text='Start', font=('Courier', 30, 'italic')).place(relx=0.45,rely=0.3)

        Rules = tk.Button(Screen, text='Rules', font=('Courier', 30, 'italic')).place(relx=0.45,rely=0.35)

        self.Player = tk.Label(Screen, text='Players', font=('Courier', 30, 'italic'))
        self.Player.place(relx=0.45,rely=0.40)

        self.Player.bind('<<Button-1>>', self.hi)
        Screen.mainloop()

    def hi(self):
        print('Hello')

Application = DiceThrower()

