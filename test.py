from tkinter import *
import mysql.connector

root = Tk()
root.state('zoomed')

top_frame = Frame(root)
top_frame.pack(anchor=N)
bottom_frame = Frame(root, borderwidth=2, relief="groove")
bottom_frame.pack(anchor=N)


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Sally4th",
    database = "Payvant"
)

curs = mydb.cursor(buffered=True)

def edit_client():
    pass

def submit_client(business_name_entry, first_name_entry, last_name_entry, add_new_client):
    cmd = "INSERT INTO clients (business_name, first_name, last_name) VALUES (%s, %s, %s)"
    values = (business_name_entry.get(), first_name_entry.get(), last_name_entry.get())
    curs.execute(cmd, values)
    mydb.commit()
    display_all_clients(root)
    add_new_client.destroy()

def add_client():
    add_new_client = Tk()
    add_new_client.title("Add New Client")
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

    submit_button = Button(add_new_client, text="Submit", command=lambda: submit_client(business_name_entry, first_name_entry, last_name_entry, add_new_client))
    submit_button.grid(row=12, column=1)

def display_all_clients(add_new_client):
    for x in bottom_frame.winfo_children():
        x.destroy()

    ID_header_label = Label(bottom_frame, text="Merchant ID")
    ID_header_label.configure(font="Verdana 10 underline bold")
    ID_header_label.grid(row=1, column=1)
    business_header_label = Label(bottom_frame, text="Business Name")
    business_header_label.configure(font="Verdana 10 underline bold")
    business_header_label.grid(row=1, column=2)
    first_name_header_label = Label(bottom_frame, text="First Name")
    first_name_header_label.configure(font="Verdana 10 underline bold")
    first_name_header_label.grid(row=1, column=3)
    last_name_header_label = Label(bottom_frame, text="Last Name")
    last_name_header_label.configure(font="Verdana 10 underline bold")
    last_name_header_label.grid(row=1, column=4)

    curs.execute("SELECT * FROM clients")
    results = curs.fetchall()
    results.reverse()
    print(results)
    print(results[0][0])
    for index, result in enumerate(results):
        mycol = 0
        id_ref = str(result[0])
        edit_button = Button(bottom_frame, text="Edit", command=lambda id_ref=id_ref: edit_client(id_ref, index))
        edit_button.grid(row=index+2, column=mycol)
        for x in result:
            temp_label = Label(bottom_frame, text=x)
            temp_label.grid(row=index+2, column=mycol+1)
            mycol += 1


title_label = Label(top_frame, text="All Your Base Are Belong To Us", font=("courier", 16, "bold"))
title_label.grid(row=0, columnspan=2, pady=10)
# Buttons at top of frame
add_client_button = Button(top_frame, text="Add Client", command=add_client)
add_client_button.grid(row=0, column=3, pady=10, padx=10)
refresh_clients = Button(root, text="Refresh", command=lambda: display_all_clients(root))


display_all_clients(top_frame)

root.mainloop()