import os

path = './'

files = os.listdir(path)
print(files)

for f in files:
    if f.endswith('.png'):
        print('Look! I found this' + f)
