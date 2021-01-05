from tkinter import *
import mysql.connector
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os, io

root = Tk()
root.title = ("")
root.iconbitmap('')
root.geometry("600x600")

def convert_file(filename):
    with open(filename, 'rb') as file:
        converted_data = file.read()
    return converted_data


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Sally4th",
    database = "Payvant"
)

curs = mydb.cursor(buffered=True)

curs.execute("CREATE TABLE IF NOT EXISTS filemanagement (file_id INT AUTO_INCREMENT PRIMARY KEY, merchant_id INT, FOREIGN KEY(merchant_id) REFERENCES clients(merchant_id) ON DELETE CASCADE, my_file LONGBLOB NOT NULL)")
curs.execute("Select * from filemanagement")
cc = curs.fetchall()
#print(cc)

def callback():
    name = filedialog.askopenfilename(initialdir="c:\\Users\\kuris\\Pictures\\", title="Select A File", filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
#    name = filedialog.askopenfilename()
#    print(name)
    with open (name, 'rb') as file:
        binaryfile = file.read()

    cmd = "INSERT INTO filemanagement (merchant_id, my_file) VALUES (%s, %s)"
    values = (1, binaryfile)
    curs.execute(cmd, values)
    mydb.commit()

def write_files(filename, thebytes):
#    pathname = r"C:\Users\kuris\PycharmProjects\Payvant\temp_images"
#    os.makedirs(pathname, 493)
    os.chdir(r"C:\Users\kuris\PycharmProjects\Payvant\temp_images")
    with open(filename, 'wb') as file:
        file.write(thebytes)

def open_image(filename):
    print(filename)
    whoda = Tk()
    whoda.title(filename)
    whoda.geometry("600x600")
    load = Image.open(filename)
    render = ImageTk.PhotoImage(load, master=whoda)

    img = Label(whoda, image=render)
    img.image = render
    img.place(x=0, y=0)

def getblob():
    curs.execute("SELECT * FROM filemanagement WHERE merchant_id = 1")
    results = curs.fetchall()

    temprow = 2
    tempcolumn = 0
    for result in results:
        image = result[2]
        filename = 'temp' + str(result[0]) + '.png'
        write_files(filename, image)

        temp_image = Image.open(filename)
        temp_image = temp_image.resize((100, 100), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(temp_image)
        img = Button(image=render, text=filename, command=lambda: open_image(filename))
        img.size = 100, 100
        img.image=render
        img.grid(row=temprow, column= tempcolumn)
        tempcolumn += 1
        if tempcolumn == 4:
            tempcolumn = 0
            temprow += 1

def deletefiles():
    temp_dir = r"C:\Users\kuris\PycharmProjects\Payvant\temp_images"

    for f in os.listdir(temp_dir):
        os.remove(f)

errmsg = 'Error!'
mybutt = Button(text='Click to Open File', command=callback).grid(row=0, column=0)
deletebutt = Button(text="Delete all files", command=deletefiles)
deletebutt.grid(row=0, column=1)

getblob()

#curs.execute("Drop TABLE filemanagement")
root.mainloop()