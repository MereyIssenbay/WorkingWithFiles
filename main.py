import os

path = 'D:\\Python\\test'
for i in os.scandir(path):
    if i.is_file() and i.name.endswith('.txt'):
        print(i.name)

