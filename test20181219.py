# compress image
# click->dosomething
from PIL import Image
from tkinter import *


# ui
# ui update
# business
def make_app():
    app = Tk()
    Label()
    Listbox()
    Button()
    Button()
    return app

# path = r'D:\Temp\compress-wedding-picture\hello1.JPG'
# output = r'D:\Temp\c_hello1.JPG'
# image = Image.open(path)
# image.save(output, quality=60)

def do():
    print(1)


app = Tk()
Button(text='click', command=do).pack()
app.mainloop()
