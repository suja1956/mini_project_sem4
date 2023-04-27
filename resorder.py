from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from rdb import Rdatabase
import subprocess
import tkinter as tk

res = Rdatabase("order.db")
root = tk.Tk()
root.title("Restaurant Worker Management")
root.geometry("1270x690+0+0")
root.config(bg="pink")

date = StringVar()
total = StringVar()
billno = StringVar()
costofdrink = StringVar()
costoffood = StringVar()
menu = StringVar()

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    date.set(row[1])
    total.set(row[2])
    billno.set(row[3])
    costofdrink.set(row[4])
    costoffood.set(row[5])
    menu.set(row[6])

def displayAll():
    tv.delete(*tv.get_children())
    for row in res.displayall():
        tv.insert("", END, values=row)

def back():
    root.withdraw()
    subprocess.run(["python", "EMS.py"])

topFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Order History',font=('arial',30,'bold'),fg='black',bd=9,
                 bg='pink',width=51)
labelTitle.grid(row=0,column=0)

tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=30, y=100, width=1200, height=400)

style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5,6), style="mystyle.Treeview")
tv.heading("1", text="Date")
tv.column("1", width=4)
tv.heading("2", text="Total Cost")
tv.column("2", width=3)
tv.heading("3", text="Bill Ref.")
tv.column("3", width=4)
tv.heading("4", text="Cost of Drink")
tv.column("4", width=4)
tv.heading("5", text="Cost of Food")
tv.column("5", width=4)
tv.heading("6", text="Order")
tv.column("6", width=6)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

displayAll()

btnAdd = tk.Button(root, command=back, text="Back", width=12, font=("Calibri", 18, "bold"), fg="black",
                bg="#16a085", bd=0)
btnAdd.place(relx=0.5, rely=2, anchor=CENTER)

btnAdd.pack(side=BOTTOM, pady=35)

root.mainloop()
