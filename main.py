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
                    create_file()
                case 2:
                    delete_file()
                case 3:
                    create_folder()
                case 4:
                    delete_folder()
                case 5:
                    list_folder()
                case 6:
                    open_folder()
                case 7:
                    print("Good bye!")
                    return False
                case _:
                    print("INCORRECT OPTION")
        except ValueError:
            print("You need to choose one of the given options")


def create_file():
    fileName = input("Give a name for file: ").strip(" ")
    wr = input("And give text that will be recorded to this file: ")
    destination = input("Give folder name in which fila will be stored: ")
    file = open(f"{fileName}.txt", "w")
    file.write(wr)
    file.close()
    if destination != "test":
        source_path = f"{fileName}.txt"
        destination_path = f"D:\\Python\\test\\{destination}"
        shutil.move(source_path, destination_path)
    else:
        source_path = f"{fileName}.txt"
        destination_path = "test"
        shutil.move(source_path, destination_path)
    print("File had been created!")
def delete_file():
    file = input("Which file do you want to delete? ").strip(" ")
    if path.exists(f"test/{file}.txt"):
        os.remove(f"test/{file}.txt")
        print("File removed.")
    else:
        print("This file does not exist.")

def create_folder():
    name = input("Give a name for folder: ").strip(" ")
    os.mkdir(f"D:\\Python\\test\\{name}")
    print("Folder had been created!")


def delete_folder():
    name = input("Which folder do you want to delete?").strip(" ")
    is_empty = os.stat(f"D:\\Python\\test\\{name}").st_size == 1
    if is_empty:
        os.rmdir(f"D:\\Python\\test\\{name}")
        print("Folder removed.")
    else:
        ans = input("Are you sure? Folder is not empty. y/n ").strip(" ")
        if ans == "Y" or ans == "y":
            shutil.rmtree(f"D:\\Python\\test\\{name}")
            print("Folder removed.")
        else:
            print("Folder is not removed.")

def list_folder():
    print("listFolder()")

def open_folder():
    print("openFolder()")

main()