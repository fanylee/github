from tkinter import *
import os

app = Tk()
label = Label(text='List All hiden files', font=('Hack', 25, 'bold'))
label.pack()
listbox = Listbox(bg='#f2f2f2', fg='aquamarine')
listbox.pack(fill=BOTH, expand=True)
path = r'D:\BigData\doc\Doc_HDP V2.6.0'
files = os.listdir(path)
for f in files:
    if f.startswith('bk_'):
        listbox.insert(END, f)

app.mainloop()
