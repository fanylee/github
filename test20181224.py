from runpy import run_path
from tkinter import *
import multiprocessing
import os


# from multiprocessing import Process


def make_app():
    app = Tk()
    app.geometry('300x300')
    Label(app, text='auto run script', font=('Arial', 25, 'bold')).pack()
    Listbox(app, name='listb', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(text='run', command=run_script).pack()
    return app


def ui_make_list():
    listb = app.children['listb']
    for d in os.listdir():
        listb.insert(END, d)


def run_script():
    listb = app.children['listb']
    s_path = listb.get(ACTIVE)
    p = multiprocessing.Process(name='print', target=run_path, args=(s_path,))
    p.start()


def stop_script():
    for p in multiprocessing.active_children():
        if p.name == 'print':
            p.terminate()


def watcher():
    print(multiprocessing.active_children())
    listb = app.children['listb']
    s_path = listb.get(ACTIVE)
    print(s_path)
    app.after(1000, watcher)


if __name__ == '__main__':
    app = make_app()
    app.after(100, ui_make_list)
    app.after(0, watcher)
    app.mainloop()
