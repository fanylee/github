# core --> core&ui --> core&ui&user --> Boundry.Edge.Corner
from tkinter import *
import time
import threading
from multiprocessing import Process

info = {
    'total_time': 0
}


def make_app():
    _font = ['Arial', 25, 'bold']
    app = Tk()
    Label(name='lb', text=0, font=_font).pack()
    Button(name='btn', text='start', command=time_counts).pack()
    Entry(name='ipt').pack()
    app.geometry('200x200')
    return app


def time_counts():
    def _counts():
        while info['total_time']:
            info['total_time'] -= 1
            print(info['total_time'])
            time.sleep(1)

    t = threading.Thread(target=_counts, name='timer')
    t.start()


def ui_watcher():
    def _update_button():
        pass

    def _get_time():

        ipt = app.children['ipt']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if not timer and ipt.get():
            info['total_time'] = int(ipt.get())

    def _update_time():
        lb = app.children['lb']
        lb['text'] = info['total_time']

    def _main():
        while True:
            print('tic toc')
            print(threading.enumerate())
            _get_time()
            _update_button()
            _update_time()

    t = threading.Thread(target=_main, name='watcher')
    t.start()


if __name__ == '__main__':
    app = make_app()
    app.after(0, time_counts)
    app.after(1, ui_watcher)
    app.mainloop()
