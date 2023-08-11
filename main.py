import os
from os import path
import shutil
def main():
    while(True):
        print("1.Create file \n "
              "2.Delete file \n "
              "3.Create folder \n "
              "4.Delete folder \n "
              "5.Folder list \n "
              "6.Open folder \n "
              "7.Quit")
        try:
            opp = int(input("Which operation do you choose?"))
            match opp:
                case 1:
                    createFile()
                case 2:
                    deleteFile()
                case 3:
                    createFolder()
                case 4:
                    deleteFolder()
                case 5:
                    listFolder()
                case 6:
                    openFolder()
                case 7:
                    print("Good bye!")
                    return False
                case _:
                    print("INCORRECT OPTION")
        except ValueError:
            print("You need to choose one of the given options")


def createFile():
    fileName = input("Give a name for file: ")
    wr = input("And give text that will be recorded to this file: ")
    file = open(f"{fileName}.txt", "w")
    file.write(wr)
    file.close()

    source_path = f"{fileName}.txt"
    destination_path = "test"
    shutil.move(source_path, destination_path)

    print("File had been created!")
def deleteFile():
    file =input("Which file do you want to delete? ")
    if path.exists(f"test/{file}.txt"):
        os.remove(f"test/{file}.txt")
        print("File was removed")
    else:
        print("This file does not exist.")

def createFolder():
    print("createFolder()")

def deleteFolder():
    print("deleteFolder()")

def listFolder():
    print("listFolder()")

def openFolder():
    print("openFolder()")

main()