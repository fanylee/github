from tkinter import *
import os

app = Tk()
label = Label(text='All hiden files', font=('Hack', 25, 'bold')).pack()
btn = Button(text='click me')
listbox = Listbox(bg='#f12f12f12', fg='purple')
listbox.pack(fill=BOTH, expand=True)
btn.pack()

path = r'D:\BigData\doc\Doc_HDP V2.6.0'
files = os.listdir(path)
for f in files:
    if f.startswith('bk_'):
        listbox.insert(END, f)

app.mainloop()
