import time
from tkinter import *
from multiprocessing import Process
import threading

info = {
    'total_time': 60
}

flag = [False]


def make_app():
    _font = ['Arial', 25, 'bold']
    app = Tk()
    Label(name='lb', text=0, font=_font).pack()
    Button(name='btn', text='start', command=time_counts).pack()
    Entry(name='ips').pack()
    Button(name='bts', text='reset', command=time_reset).pack()
    Entry(name='ipt').pack()
    Button(name='btp', text='pause', command=time_pause).pack()
    Entry(name='ipp').pack()
    app.geometry('300x300')
    return app


def time_counts():
    flag[0] = False

    def _counts():
        while info['total_time']:
            if flag[0]:
                break
            info['total_time'] -= 1
            print(info['total_time'])
            time.sleep(1)

    t = threading.Thread(target=_counts, name='timer')
    t.start()


def time_reset():
    flag[0] = True
    info['total_time'] = 60


def time_pause():
    flag[0] = True


def ui_watcher():
    def _update_button():
        btn = app.children['btn']
        btp = app.children['btp']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if timer:
            btn['state'] = 'disabled'
            btp['state'] = 'normal'
        else:
            btn['state'] = 'normal'
            btp['state'] = 'disable'

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
            print("tik toc")
            print(threading.enumerate())
            _update_button()
            _get_time()
            _update_time()

            time.sleep(0.5)

    t = threading.Thread(target=_main, name='watcher')
    t.start()


if __name__ == '__main__':
    app = make_app()
    app.after(0, ui_watcher)
    app.mainloop()
