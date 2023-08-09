import os

path = 'D:\\Python\\test'
dirList = os.listdir(path)
print(dirList)
for i in dirList:
    print(i,type(i),path+'\\'+i,os.path.isdir(path+'\\'+i))