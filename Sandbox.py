from tkinter import *
import mysql.connector

root = Tk()
root.geometry("600x600")
#root.state('zoomed')
main_frame = Frame(root)
main_frame.pack()

add_frame = Frame(root, borderwidth=5)
add_frame.pack()

topFrame = Frame(root, width=1350, height=50)  # Added "container" Frame.
topFrame.pack(side=TOP, fill=X, expand=1, anchor=N)

titleLabel = Label(topFrame, font=('arial', 12, 'bold'),
                   text="Vehicle Window Fitting - Management System",
                   bd=5, anchor=W)
titleLabel.pack(side=LEFT)

clockFrame = Frame(topFrame, width=100, height=50, bd=4, relief="ridge")
clockFrame.pack(side=RIGHT)
clockLabel = Label(clockFrame, font=('arial', 12, 'bold'), bd=5, anchor=E)
clockLabel.pack()

bottomFrame = Frame(root, width=1350, height=50, bd=4, relief="ridge")
bottomFrame.pack(side=BOTTOM, fill=X, expand=1, anchor=S)


def makelife():
    main_area = Listbox(topFrame)
    main_area.pack()


#    makebutt = Button(main_frame, text="Create", command=makelife)
#    makebutt.pack()

    mylist = ["one", "two", "three", "four", "five", "six", "one", "two", "three", "four", "five", "six", "one", "two", "three", "four", "five", "six"]

    for x in mylist:
        main_area.insert(END, x)
    for y in topFrame.winfo_children():
        print(y)


def killall():
    for x in main_frame.winfo_children():
        x.destroy()
        print(f"{x} was destroyed!")
    makelife()

makelife()
mybutt = Button(bottomFrame, text="Kill", command=killall)
mybutt.pack()
makebutt = Button(bottomFrame, text="Create", command=makelife)
makebutt.pack()


root.mainloop()