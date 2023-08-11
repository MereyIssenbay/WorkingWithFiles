import os
from os import path
import shutil
def main():
    while(True):
        print(" 1.Create file\n "
              "2.Delete file\n "
              "3.Create folder\n "
              "4.Delete folder\n "
              "5.Folder list\n "
              "6.Open folder\n "
              "7.Quit")
        try:
            opp = int(input("Choose the operation: "))
            match opp:
                case 1:
                    file_name = input("Give a name for file: ").strip(" ")
                    wr = input("And give text that will be recorded to this file: ")
                    create_file(file_name, wr)
                    print("File had been created!")
                case 2:
                    file_name = input("Which file do you want to delete? ").strip(" ")
                    delete_file(file_name)
                case 3:
                    folder_name = input("Give a name for folder: ").strip(" ")
                    create_folder(folder_name)
                case 4:
                    folder_name = input("Which folder do you want to delete?").strip(" ")
                    delete_folder(folder_name)
                case 5:
                    folder_name = input("Which folder's entries do you want to get? ").strip(" ")
                    list_folder(folder_name)
                case 6:
                    replace_file()
                case 7:
                    print("Good bye!")
                    return False
                case _:
                    print("INCORRECT OPTION")
        except ValueError:
            print("You need to choose one of the given options")


def create_file(file_name, wr):
    file = open(f"{file_name}.txt", "w")
    file.write(wr)
    file.close()
    shutil.move(f"D:\\Python\\{file_name}.txt", "D:\\Python\\test")

def delete_file(file_name):
    if path.exists(f"D:\\Python\\test\\{file_name}.txt"):
        os.remove(f"D:\\Python\\test\\{file_name}.txt")
        print("File removed.")
    else:
        print("This file does not exist.")

def create_folder(folder_name):
    os.mkdir(f"D:\\Python\\test\\{folder_name}")
    print("Folder had been created!")

def delete_folder(folder_name):
    if is_empty(f"D:\\Python\\test\\{folder_name}"):
        os.rmdir(f"D:\\Python\\test\\{folder_name}")
        print("Folder removed.")
    else:
        ans = input("Are you sure? Folder is not empty. y/n ").strip(" ")
        if ans == "Y" or ans == "y":
            shutil.rmtree(f"D:\\Python\\test\\{folder_name}")
            print("Folder removed.")
        else:
            print("Folder is not removed.")

def list_folder(folder_name):
    if path.exists(f"D:\\Python\\test\\{folder_name}"):
        if is_empty(f"D:\\Python\\test\\{folder_name}"):
            print(f"Folder {folder_name} is empty.")
        else:
            print(f"Here is the list in the folder {folder_name}")
            for i in os.scandir(f"D:\\Python\\test\\{folder_name}"):
                print(i.name)
    else:
        print(f"Here is the list in the folder 'test'")
        for i in os.scandir(f"D:\\Python\\test"):
            print(i.name)
def replace_file():
    print("replace")


def is_empty(folder_path):
    items = os.listdir(folder_path)

    if len(items) == 0:
        return True
    else:
        return False

main()