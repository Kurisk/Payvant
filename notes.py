from tkinter import *
import mysql.connector
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os, io

root = Tk()
root.title = ("")
root.iconbitmap('')
#root.geometry("600x600")


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Sally4th",
    database = "Payvant"
)

curs = mydb.cursor(buffered=True)

curs.execute("CREATE TABLE IF NOT EXISTS notes (file_id INT AUTO_INCREMENT PRIMARY KEY, merchant_id INT, FOREIGN KEY(merchant_id) REFERENCES clients(merchant_id) ON DELETE CASCADE, note MEDIUMTEXT)")
curs.execute("Select * from notes")
cc = curs.fetchall()
print(cc)

def add_note(bigbox):
    bigbox = bigbox.get('1.0', END)
    print(bigbox)

    cmd = "INSERT INTO notes (merchant_id, note) VALUES (%s, %s)"
    values = (8, bigbox)
    curs.execute(cmd, values)
    mydb.commit()

def show_notes():
    curs.execute("SELECT * FROM notes")
    results = curs.fetchall()

    myrow = 3
    for result in results:
        print(result)
        tempbox = Text(root, height=10)
        tempbox.grid(row=myrow, column=0)
        tempbox.insert(END, result[2])
        myrow += 1

bigbox = Text(root, height=10)
bigbox.grid(row=0, column=0)
submit = Button(root, text='Submit', command=lambda: add_note(bigbox))
submit.grid(row=1, columnspan=2)

show = Button(root, text='Show Notes', command=show_notes)
show.grid(row=2, columnspan=2)


#curs.execute("Drop TABLE notes")
root.mainloop()