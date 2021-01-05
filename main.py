from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import mysql.connector
import os
import csv
from tkinter import filedialog

root = Tk()
root.title("Vickys Fucking Database")
root.iconbitmap('Vicky.ico')
#root.geometry("1600x600")
root.state('zoomed')

def getfoc(self):
    print("It worked!")

def about_menu():
    about = Tk()
    about.geometry("400x400")
    about.title("About Vickys Fucking Database")
    about_label = Label(about, text="This is a fucking database program for Vicky!").pack(pady=30)
    who_did_it = Label(about, text="Created by Dana Kennedy ~ GoFuckYourself@FuckYou.Biz").pack(pady=100)
    version_label = Label(about, text="Version 1.0").pack(pady=40)

def submit_client(business_name_entry, first_name_entry, last_name_entry, phone_number_entry, address1, address2, city, state, country, merchant_number, checking_account, notes, add_new_client):
    cmd = "INSERT INTO clients (business_name, first_name, last_name, phone_number, address1, address2, city, state, country, merchant_number, checking_account, notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (business_name_entry.get(), first_name_entry.get(), last_name_entry.get(), phone_number_entry.get(), address1.get(), address2.get(), city.get(), state.get(), country.get(), merchant_number.get(), checking_account.get(), notes.get("1.0", 'end-1c'))
    curs.execute(cmd, values)
    mydb.commit()
    display_all_clients(root)
    add_new_client.destroy()

def add_client():
    add_new_client = Tk()
    add_new_client.title("Add New Client To Vickys Fucking Database")
    add_new_client.geometry("400x600")

    business_name_label = Label(add_new_client, text="Business Name:")
    business_name_label.grid(row=0, column=0, padx=5, pady=3)
    business_name_entry = Entry(add_new_client)
    business_name_entry.grid(row=0, column=1)
    first_name_label = Label(add_new_client, text="First Name:")
    first_name_label.grid(row=1, column=0, padx=5, pady=3)
    first_name_entry = Entry(add_new_client)
    first_name_entry.grid(row=1, column=1)
    last_name_label = Label(add_new_client, text="Last Name:")
    last_name_label.grid(row=2, column=0, padx=5, pady=3)
    last_name_entry = Entry(add_new_client)
    last_name_entry.grid(row=2, column=1, padx=10, pady=3)
    phone_number_label = Label(add_new_client, text="Phone Number:")
    phone_number_label.grid(row=3, column=0, padx=10, pady=3)
    phone_number_entry = Entry(add_new_client)
    phone_number_entry.grid(row=3, column=1, padx=10, pady=3)
    address1 = Label(add_new_client, text="Address 1:")
    address1.grid(row=4, column=0, padx=10, pady=3)
    address1 = Entry(add_new_client)
    address1.grid(row=4, column=1, padx=10, pady=3)
    address2 = Label(add_new_client, text="Address 2:")
    address2.grid(row=5, column=0, padx=10, pady=3)
    address2 = Entry(add_new_client)
    address2.grid(row=5, column=1, padx=10, pady=3)
    city = Label(add_new_client, text="City:")
    city.grid(row=6, column=0, padx=10, pady=3)
    city = Entry(add_new_client)
    city.grid(row=6, column=1, padx=10, pady=3)
    state = Label(add_new_client, text="State:")
    state.grid(row=7, column=0, padx=10, pady=3)
    state = Entry(add_new_client)
    state.grid(row=7, column=1, padx=10, pady=3)
    country = Label(add_new_client, text="Country:")
    country.grid(row=8, column=0, padx=10, pady=3)
    country = Entry(add_new_client)
    country.grid(row=8, column=1, padx=10, pady=3)
    merchant_number = Label(add_new_client, text="Merchant Number:")
    merchant_number.grid(row=9, column=0, padx=10, pady=3)
    merchant_number = Entry(add_new_client)
    merchant_number.grid(row=9, column=1, padx=10, pady=3)
    checking_account = Label(add_new_client, text="Checking Account:")
    checking_account.grid(row=10, column=0, padx=10, pady=3)
    checking_account = Entry(add_new_client)
    checking_account.grid(row=10, column=1, padx=10, pady=3)
    notes = Label(add_new_client, text="Notes:")
    notes.grid(row=11, column=0, padx=10, pady=3)
    notes = ScrolledText(add_new_client, width=20, height=5)
    notes.grid(row=11, column=1, padx=10, pady=3)


    submit_button = Button(add_new_client, text="Submit", command=lambda: submit_client(business_name_entry, first_name_entry, last_name_entry, phone_number_entry, address1, address2, city, state, country, merchant_number, checking_account, notes, add_new_client))
    submit_button.grid(row=12, column=1)

def callback(merch_id_entry):
    name = filedialog.askopenfilename(initialdir="c:\\Users\\kuris\\Pictures\\", title="Select A File", filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
    with open (name, 'rb') as file:
        binaryfile = file.read()

    cmd = "INSERT INTO filemanagement (merchant_id, my_file) VALUES (%s, %s)"
    values = (merch_id_entry, binaryfile)
    curs.execute(cmd, values)
    mydb.commit()

def write_files(filename, thebytes):
    os.chdir(r"C:\Users\kuris\PycharmProjects\Payvant\temp_images")
    with open(filename, 'wb') as file:
        file.write(thebytes)
    print("Files have been written.")

def open_image(filename):
    whoda = Tk()
    whoda.title(filename)
    whoda.geometry("600x600")
    load = Image.open(filename)
    render = ImageTk.PhotoImage(load, master=whoda)
    img = Label(whoda, image=render)
    img.image = render
    img.place(x=0, y=0)

def edit_client_update(edit_client_window):
    cmd = "UPDATE clients SET business_name = %s, first_name = %s, last_name = %s, phone_number = %s, address1 = %s, address2 = %s, city = %s, state = %s, country = %s, merchant_number = %s, checking_account = %s WHERE merchant_id = %s"

    business_name = business_name_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    phone_number = phone_number_entry.get()
    address1 = address1_entry.get()
    address2 = address2_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    country = country_entry.get()
    merchant_number = merchant_number_entry.get()
    checking_account = checking_account_entry.get()

    merch_id = merch_id_entry

    values = (business_name, first_name, last_name, phone_number, address1, address2, city, state, country, merchant_number, checking_account, merch_id)
    curs.execute(cmd, values)


    note_cmd = "INSERT INTO notes (merchant_id, note) VALUES (%s, %s)"
    note = new_note_entry.get('1.0', END)
    values = (merch_id, note)
    curs.execute(note_cmd, values)
    mydb.commit()
    display_all_clients(root)
    edit_client_window.destroy()

def edit_client(id_ref, index):
    edit_client_window = Tk()
    edit_client_window.title("Edit Client In Vickys Fucking Database")

    cmd = "SELECT * FROM clients WHERE merchant_id = %s"
    values = (id_ref,)
    curs.execute(cmd, values)
    results = curs.fetchall()
    for result in results:
#        print(result)
        continue
##### ENTRY WIDGETS
    business_name_label = Label(edit_client_window, text="Business Name:")
    business_name_label.grid(row=0, column=0, padx=5, pady=3)
    global business_name_entry
    business_name_entry = Entry(edit_client_window)
    business_name_entry.grid(row=0, column=1)
    business_name_entry.insert(0, result[1])
    first_name_label = Label(edit_client_window, text="First Name:")
    first_name_label.grid(row=1, column=0, padx=5, pady=3)
    global first_name_entry
    first_name_entry = Entry(edit_client_window)
    first_name_entry.grid(row=1, column=1)
    first_name_entry.insert(0, result[2])
    last_name_label = Label(edit_client_window, text="Last Name:")
    last_name_label.grid(row=2, column=0, padx=5, pady=3)
    global last_name_entry
    last_name_entry = Entry(edit_client_window)
    last_name_entry.grid(row=2, column=1, padx=10, pady=3)
    last_name_entry.insert(0, result[3])
    phone_number_label = Label(edit_client_window, text="Phone Number:")
    phone_number_label.grid(row=3, column=0, padx=10, pady=3)
    global phone_number_entry
    phone_number_entry = Entry(edit_client_window)
    phone_number_entry.grid(row=3, column=1, padx=10, pady=3)
    phone_number_entry.insert(0, result[4])
    address1_entry_label = Label(edit_client_window, text="Address 1:")
    address1_entry_label.grid(row=4, column=0, padx=10, pady=3)
    global address1_entry
    address1_entry = Entry(edit_client_window)
    address1_entry.grid(row=4, column=1, padx=10, pady=3)
    address1_entry.insert(0, result[5])
    address2_entry_label = Label(edit_client_window, text="Address 2:")
    address2_entry_label.grid(row=5, column=0, padx=10, pady=3)
    global address2_entry
    address2_entry = Entry(edit_client_window)
    address2_entry.grid(row=5, column=1, padx=10, pady=3)
    address2_entry.insert(0, result[6])
    city_entry_label = Label(edit_client_window, text="City:")
    city_entry_label.grid(row=6, column=0, padx=10, pady=3)
    global city_entry
    city_entry = Entry(edit_client_window)
    city_entry.grid(row=6, column=1, padx=10, pady=3)
    city_entry.insert(0, result[7])
    state_entry_label = Label(edit_client_window, text="State:")
    state_entry_label.grid(row=7, column=0, padx=10, pady=3)
    global state_entry
    state_entry = Entry(edit_client_window)
    state_entry.grid(row=7, column=1, padx=10, pady=3)
    state_entry.insert(0, result[8])
    country_entry_label = Label(edit_client_window, text="Country:")
    country_entry_label.grid(row=8, column=0, padx=10, pady=3)
    global country_entry
    country_entry = Entry(edit_client_window)
    country_entry.grid(row=8, column=1, padx=10, pady=3)
    country_entry.insert(0, result[9])
    merchant_number_label = Label(edit_client_window, text="Merchant Number:")
    merchant_number_label.grid(row=9, column=0, padx=10, pady=3)
    global merchant_number_entry
    merchant_number_entry = Entry(edit_client_window)
    merchant_number_entry.grid(row=9, column=1, padx=10, pady=3)
    merchant_number_entry.insert(0, result[10])
    checking_account_label = Label(edit_client_window, text="Checking Account:")
    checking_account_label.grid(row=10, column=0, padx=10, pady=3)
    global checking_account_entry
    checking_account_entry = Entry(edit_client_window)
    checking_account_entry.grid(row=10, column=1, padx=10, pady=3)
    checking_account_entry.insert(0, result[11])
    global new_note_entry
    new_note_entry = Text(edit_client_window, height=7, width=45)
    new_note_entry.grid(row=11, column=0, columnspan=2, pady=(10, 10), padx=(10, 0))
    global merch_id_entry
    merch_id_entry = result[0]

### GET NOTES FROM DATABASE
    curs.execute(f"SELECT * FROM notes WHERE merchant_id = {id_ref}")
    results = curs.fetchall()
    notes_frame = Frame(edit_client_window)
    notes_frame.grid(row=0, rowspan=100, column=3, sticky=N, padx=(10, 20), pady=(10, 10))
    myrow = 3
    results.reverse()
    for result in results:
        tempbox = Text(notes_frame, height=7)
        tempbox.grid(row=myrow, column=0, pady=(0, 10))
        tempbox.insert(END, result[2])
        myrow += 1

    update_button = Button(edit_client_window, text="Submit", command=lambda: edit_client_update(edit_client_window))
    update_button.grid(row=15, column=1, pady=(0, 10))
    upload = Button(edit_client_window, text='Click to Open File', command=lambda: callback(merch_id_entry))
    upload.grid(row=31, column=1, pady=(10,10))

### GET IMAGES FROM DATABASE
    curs.execute(f"SELECT * FROM filemanagement WHERE merchant_id = {id_ref}")
    results = curs.fetchall()
    temprow = 20
    tempcolumn = 0
    for index, result in enumerate(results):
        image = result[2]
        filename = 'temp' + str(result[0]) + '.png'
        write_files(filename, image)
        temp_image = Image.open(filename)
        temp_image = temp_image.resize((100, 100), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(temp_image, master=edit_client_window)
        img = Button(image=render, text=filename, command=lambda filename=filename: open_image(filename), master=edit_client_window)
        print(f"This is the image text " + img['text'])
        img.size = 100, 100
        img.image=render
        img.grid(row=temprow, column= tempcolumn)
        tempcolumn += 1
        if tempcolumn == 4:
            tempcolumn = 0
            temprow += 1

def display_all_clients(add_new_client):
    curs.execute("SELECT * FROM clients")
#    print(curs.description)
    results = curs.fetchall()
    results.reverse()
#    scrollbar = Scrollbar(root)
#    scrollbar.grid(sticky=E)
    for index, result in enumerate(results):
        mycol = 0
        id_ref = str(result[0])
        edit_button = Button(root, text="Edit", command=lambda id_ref=id_ref: edit_client(id_ref, index))
        edit_button.grid(row=index+2, column=mycol)
        for x in result:
            temp_label = Label(add_new_client, text=x)
            temp_label.grid(row=index+2, column=mycol+1)
            mycol += 1

def delete_client(doomed_client_entry, delete_client_sub):
    cmd = "DELETE FROM clients WHERE merchant_id = %s"
    doomed_client_entry = (doomed_client_entry.get(),)
    curs.execute(cmd, doomed_client_entry)

    mydb.commit()
    delete_client_sub.destroy()

def delete_client_window():
    delete_client_sub = Tk()
    delete_client_sub.title("Delete Client From Vickys Fucking Database")

    del_main_frame = LabelFrame(delete_client_sub, text="Clients", bd=5, bg="LightGray", padx=10, pady=10)
    del_main_frame.pack(padx=5, pady=5)
    display_all_clients(del_main_frame)

    doomed_client_label = Label(delete_client_sub, text="Enter Merchant ID In Box To Delete")
    doomed_client_label.pack()
    doomed_client_entry = Entry(delete_client_sub, width=3)
    doomed_client_entry.pack(pady=5)
    doomed_client_button = Button(delete_client_sub, text="Delete", command=lambda: delete_client(doomed_client_entry, delete_client_sub))
    doomed_client_button.pack(pady=5)


#TODO fix export file name so it has a time stamp
def export_DB():
    curs.execute("SELECT * FROM clients")
    results = curs.fetchall()
    with open('clients_DB.csv', 'w') as f:
        w = csv.writer(f, dialect='excel')
        w.writerow(results)
#TODO blah
# BUILD THE MAIN MENU
main_menu = Menu(root)
edit_menu = Menu(root)
view_menu = Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu)
edit_menu = Menu(edit_menu)
view_menu = Menu(view_menu)
main_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Settings')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)
main_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Add Client', command=add_client)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', command=add_client)
edit_menu.add_command(label='Copy', command=add_client)
edit_menu.add_command(label='Paste', command=add_client)
main_menu.add_cascade(label='View', menu=view_menu)
view_menu.add_command(label='About', command=about_menu)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Sally4th",
    database = "Payvant"
)

curs = mydb.cursor(buffered=True)
#curs.execute("CREATE DATABASE Payvant")
#curs.execute("DROP TABLE clients")

# Build the client table if it doesn't exist.
curs.execute("CREATE TABLE IF NOT EXISTS clients (merchant_id INT AUTO_INCREMENT PRIMARY KEY, \
    business_name VARCHAR(255), \
    first_name VARCHAR(255), \
    last_name VARCHAR(255), \
    phone_number VARCHAR(255), \
    address1 VARCHAR(255), \
    address2 VARCHAR(255), \
    city VARCHAR(255), \
    state VARCHAR(50), \
    country VARCHAR(50), \
    merchant_number VARCHAR(255), \
    checking_account VARCHAR(255), \
    notes VARCHAR(255))")
#    notes VARCHAR(255), \
#    merchant_id INT AUTO_INCREMENT PRIMARY KEY)")

title_label = Label(root, text="Fucking program for Vicky", font=("courier", 16, "bold"))
title_label.grid(row=0, columnspan=2, pady=10)
ID_header_label = Label(root, text="Merchant ID")
ID_header_label.configure(font="Verdana 10 underline bold")
ID_header_label.grid(row=1, column=1)
business_header_label = Label(root, text="Business Name")
business_header_label.configure(font="Verdana 10 underline bold")
business_header_label.grid(row=1, column=2)
first_name_header_label = Label(root, text="First Name")
first_name_header_label.configure(font="Verdana 10 underline bold")
first_name_header_label.grid(row=1, column=3)
last_name_header_label = Label(root, text="Last Name")
last_name_header_label.configure(font="Verdana 10 underline bold")
last_name_header_label.grid(row=1, column=4)
phone_header_label = Label(root, text="Phone Number")
phone_header_label.configure(font="Verdana 10 underline bold")
phone_header_label.grid(row=1, column=5)
address1_header_label = Label(root, text="Address")
address1_header_label.configure(font="Verdana 10 underline bold")
address1_header_label.grid(row=1, column=6)
address2_header_label = Label(root, text="Apt / Suite")
address2_header_label.configure(font="Verdana 10 underline bold")
address2_header_label.grid(row=1, column=7)
city_header_label = Label(root, text="City")
city_header_label.configure(font="Verdana 10 underline bold")
city_header_label.grid(row=1, column=8)
state_header_label = Label(root, text="State")
state_header_label.configure(font="Verdana 10 underline bold")
state_header_label.grid(row=1, column=9)
country_header_label = Label(root, text="Country")
country_header_label.configure(font="Verdana 10 underline bold")
country_header_label.grid(row=1, column=10)
merchant_number_header_label = Label(root, text="Merchant Number")
merchant_number_header_label.configure(font="Verdana 10 underline bold")
merchant_number_header_label.grid(row=1, column=11)
checking_header_label = Label(root, text="Checking Account")
checking_header_label.configure(font="Verdana 10 underline bold")
checking_header_label.grid(row=1, column=12)
notes_header_label = Label(root, text="Notes")
notes_header_label.configure(font="Verdana 10 underline bold")
notes_header_label.grid(row=1, column=13)

# Buttons at top of frame
add_client_button = Button(root, text="Add Client", command=add_client)
add_client_button.grid(row=0, column=3, pady=10, padx=10)
delete_client_button = Button(root, text="Delete Client", command=delete_client_window)
delete_client_button.grid(row=0, column=4, pady=10, padx=10)
refresh_clients = Button(root, text="Refresh", command=lambda: display_all_clients(root))
refresh_clients.grid(row=0, column=5, pady=10, padx=10)
export_DB_button = Button(root, text="Export DB", command=export_DB)
export_DB_button.grid(row=0, column=6, pady=10, padx=10)
export_DB_button.bind('<Enter>', getfoc)


display_all_clients(root)

root.mainloop()
#curs.execute("DELETE FROM filemanagement WHERE merchant_id = 4")
#curs.execute("DELETE FROM clients WHERE merchant_id = 4")
temp_dir = r"C:\Users\kuris\PycharmProjects\Payvant\temp_images"

try:
    for f in os.listdir(temp_dir):
        os.remove(f)
except:
    print("all is good")