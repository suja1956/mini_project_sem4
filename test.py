from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk

class CustomTable(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)

        # create table headings
        headings = ['Date', 'Total', 'Bill Ref', 'Cost of Drink', 'Cost of Food', 'Menu']
        for col, heading in enumerate(headings):
            label = ttk.Label(self, text=heading, style='primary.TLabel')
            label.grid(row=0, column=col, sticky='we')

        # create table content
        for row in range(rows):
            for col in range(columns):
                label = ttk.Label(self, text=f'Row {row} Col {col}', style='secondary.TLabel')
                label.grid(row=row+1, column=col, sticky='we')

        # add scrollbars
        vsb = ttk.Scrollbar(self, orient="vertical")
        vsb.grid(row=1, column=columns+1, sticky='ns')
        canvas = tk.Canvas(self, yscrollcommand=vsb.set)
        canvas.grid(row=1, column=0, columnspan=columns+1, sticky='we')
        vsb.config(command=canvas.yview)
        canvas.config(scrollregion=canvas.bbox("all"))

        self.grid(sticky='we')

# create a style instance from ttkbootstrap
style = Style(theme='flatly')

# create the main window
root = style.master
root.title("Custom Table")

# create the table
table = CustomTable(root, rows=10, columns=6)
table.pack(expand=True, fill='both')

# start the main loop
root.mainloop()
