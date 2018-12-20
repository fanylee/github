import psutil
import time
from tkinter import *


# while True:
#    'en0'
#    s1 = psutil.net_io_counters(pernic=True)
#    time.sleep(1)
#    s2 = psutil.net_io_counters(pernic=True)
#    result = s2.bytes_recv - s1.bytes_recv
#    print(result / 1024)

def make_app():
    app = Tk()
    app.geometry('400x400')
    app.config(bg='#303030')
    Label(text='Speed Monitor',
          font=('Arial', 25, 'bold'),
          bg='#303030',
          fg='white').pack()

    Label(name='lb2',
          text='_kb/s',
          font=('Arial', 25, 'bold'),
          bg='#303030',
          fg='white'
          ).pack()
    return app


def speed_test():
    # 'en0'
    s1 = psutil.net_io_counters(pernic=True)['Wi-Fi']
    time.sleep(1)
    s2 = psutil.net_io_counters(pernic=True)['Wi-Fi']
    result = s2.bytes_recv - s1.bytes_recv
    return str(result / 1024) + 'kb/s'


def ui_update(do):
    data = do()
    lbe = app.children['lb2']
    lbe.config(text=data)
    app.after(1000, lambda: ui_update(do))


app = make_app()
app.after(1000, lambda: ui_update(speed_test))
app.mainloop()
