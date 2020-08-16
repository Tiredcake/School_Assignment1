from tkinter import *
from PIL import ImageTk,Image
import random as rand
import time
dictionary = {'player1':0, 'player2':0}
a = dictionary.keys['player1']
b = dictionary.keys['player2']
print(type(a))
print(type(b))

if a == 1 and b == 1:
    print("True")


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
