from tkinter import *
import threading
import multiprocessing
from runpy import run_path
import time

data = []


def make_app():
    app = Tk()
    app.geometry('400x500')
    Button(name='add', text='add task', command=make_task).pack(side=BOTTOM)
    return app


def make_task():
    _font = ['Arial', 15, 'bold']
    f = Frame(bg='#f2f2f2')
    Label(f, name='lb_name', text='script name', bg='green', font=_font).pack(anchor='nw')
    Label(f, name='lb_time', text='configure task detail', bg='green').pack(side=TOP)
    Button(f, text='modify', command=lambda: make_win(f)).pack(anchor='se')
    f.pack(fill=X)


def make_win(f):
    t = Toplevel(f)
    Label(t, text='File Path', bg='black', fg='red').pack()
    Entry(t, name='file_ipt').pack()
    Label(t, text='Start Time', bg='black', fg='red').pack()
    Entry(t, name='time_ipt').pack()
    Button(t, text='save', command=lambda: (save(t), t.destroy())).pack()


def save(t):
    d = {}
    file_path = t.children['file_ipt'].get()
    start_time = t.children['time_ipt'].get()
    d['file_path'] = file_path
    d['start_time'] = start_time
    d['execute'] = False
    data.append(d)


def watcher():
    def _test():
        print(data)

    def _refresh_tasks():

        tasks = [t[1] for t in app.children.items() if t[0] != 'add']
        for d, t in zip(data, tasks):
            t.children['lb_name']['text'] = d['file_path']
            t.children['lb_time']['text'] = d['start_time']

    def _task_check():
        now = time.ctime().split()[-2]
        for d in data:
            if d['start_time'] <= now and not d['execute']:
                p = multiprocessing.Process(target=run_path,args=(d['file_path']))
                p.start()
                d['execute'] = True

    def _main():
        while True:
            time.sleep(0.5)
            _test()
            _refresh_tasks()
            _task_check()

    t = threading.Thread(target=_main, name='watcher')
    t.start()


if __name__ == '__main__':
    app = make_app()
    app.after(0, watcher)
    app.mainloop()
