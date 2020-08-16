from tkinter import *
from PIL import ImageTk,Image
import random as rand
import time
root = Tk()
Frame = Frame(root)
Frame.pack()
img = [ImageTk.PhotoImage(Image.open("1.png")),ImageTk.PhotoImage(Image.open("2.png")),ImageTk.PhotoImage(Image.open("3.png")), ImageTk.PhotoImage(Image.open("4.png")), ImageTk.PhotoImage(Image.open("5.png")), ImageTk.PhotoImage(Image.open("6.png"))]
On = True
Count = 0
Label(Frame, image=img[rand.randrange(0,len(img))]).pack()




root.mainloop()
"""import sqlite3
conn = sqlite3.connect('Database.db')
# Importing data from text
listclass = []
with open('ClassList.txt') as f:
    for x in f.readlines():
        listclass.append(x.strip())
Password = {}
with open('Data_Login.txt') as f:
    for x in f.readlines():
        a = x.split(',')
        Password[a[0]] = a[1].strip()
registration = {}
id = 0
for x in listclass:
    if x not in Password:
        registration[x] = 'N'
    else:
        registration[x] = 'Y'
print(registration)
c = conn.cursor()
id = 1

c.execute('Update Player Set registered = "N" WHERE name="Syed Noor"')

conn.commit()
for x in c:
    print(x)"""
