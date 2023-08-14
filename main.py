import os
import shutil
import datetime
def main():
    while(True):
        print("1.Create file\n"
              "2.Delete file\n"
              "3.Create folder\n"
              "4.Delete folder\n"
              "5.Folder list\n"
              "6.Replace file\n"
              "7.Replace folder\n"
              "8.Set limit\n"
              "9.Quit")
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
                    file_name = input("Give a file name: ").strip(" ")
                    destination = input("Give folder name: ").strip(" ")
                    replace_file(file_name, destination)
                case 7:
                    folder_name = input("Give the folder name: ").strip(" ")
                    destination = input("Give the destination name: ").strip(" ")
                    replace_folder(folder_name, destination)
                case 8:
                    folder_name = input("Give the folder name: ").strip(" ")
                    limit = int(input("Give the limit size: ").strip(" "))
                    set_limit(folder_name,limit)
                case 9:
                    print("Good bye!")
                    print("-" * 30)
                    return False
                case _:
                    print("INCORRECT OPTION")
        except ValueError:
            print("You need to write integer number of operation.")
            print("-" * 30)

folder_limits = {}
def create_file(file_name, wr):
    file = open(f"{file_name}.txt", "w")
    file.write(wr)
    file.close()
    shutil.move(f"D:\\Python\\{file_name}.txt", "D:\\Python\\test")

def delete_file(file_name):
    file_path = find_file("D:\\Python\\test", file_name)
    if file_path:
        os.remove(file_path)
        print("File removed.")
        print("-" * 30)
    else:
        print("This file does not exist.")
        print("-" * 30)

def create_folder(folder_name):
    os.mkdir(f"D:\\Python\\test\\{folder_name}")
    print("Folder had been created!")
    print("-" * 30)
    return None

def delete_folder(folder_name):
    folder_path = find_folder("D:\\Python\\test", folder_name)
    if folder_path:
        if is_empty(folder_path):
            os.rmdir(folder_path)
            print("Folder removed.")
            print("-" * 30)
        else:
            ans = input("Are you sure? Folder is not empty. y/n ").strip(" ")
            if ans == "Y" or ans == "y":
                shutil.rmtree(folder_path)
                print("Folder removed.")
                print("-" * 30)
            else:
                print("Folder is not removed.")
                print("-" * 30)
    return None

def list_folder(folder_name):
    folder_path = find_folder("D:\\Python\\test", folder_name)

    if folder_path:
        list_info(folder_path)
    elif folder_name == "test":
        list_info("D:\\Python\\test")
    else:
        print(f"Folder '{folder_name}' not found.")
        print("-" * 30)
    return None

def replace_file(file_name, destination):
    destination_path = find_folder("D:\\Python\\test", destination)
    file_path = find_file("D:\\Python\\test", file_name)
    if destination_path and file_path:
        if has_limit(destination):
            destination_size = get_folder_size(destination_path)
            limit = get_limit(destination)
            if destination_size > limit:
                print("Warning: Folder size exceeds the limit. You can not add the file. ")
                print("-" * 30)
            else:
                shutil.move(file_path, destination_path)
                print("File replaced successfully!")
        else:
            shutil.move(file_path, destination_path)
            print("File replaced successfully!")
    else:
        print(destination_path)
        print(file_path)
        print("The destination or file is not existing.")
        print("-" * 30)
    return None

def replace_folder(folder_name, destination):
    folder_path = find_folder("D:\\Python\\test", folder_name)
    destination_path = find_folder("D:\\Python\\test", destination)
    if folder_path and destination_path:
        if has_limit(destination):
            destination_size = get_folder_size(destination_path)
            limit = get_limit(destination)
            if destination_size > limit:
                print("Warning: Folder size exceeds the limit. You can not add the folder. ")
                print("-" * 30)
            else:
                shutil.move(folder_path, destination_path)
                print("Folder replaced successfully!")
                print("-" * 30)
        else:
            shutil.move(folder_path, destination_path)
            print("Folder replaced successfully!")
            print("-" * 30)
    else:
        print(folder_path)
        print(destination_path)
        print("The destination or folder is not existing.")
        print("-" * 30)
    return None

def set_limit(folder_name, limit):
    folder_path = find_folder("D:\\Python\\test", folder_name)
    folder_size = get_folder_size(folder_path)
    if folder_path:
        if folder_size > limit:
            print("Warning: Current folder size exceeds the limit. Limit cannot be set.")
            print("-" * 30)
        else:
            folder_limits[folder_name] = limit
            print(f"Limit of {limit} bytes set successfully for folder {folder_name}.")
            print("-" * 30)
    else:
        print(f"Folder '{folder_name}' not found.")
        print("-" * 30)


def has_limit(folder_name):
    return folder_name in folder_limits

def get_limit(folder_name):
    return folder_limits.get(folder_name)

def find_folder(start_dir, folder_name):
    for entry in os.scandir(start_dir):
        if entry.is_dir() and entry.name == folder_name:
            return entry.path
        elif entry.is_dir():
            result = find_folder(entry.path, folder_name)
            if result:
                return result
    return None

def find_file(start_dir, file_name):
    for entry in os.scandir(start_dir):
        if entry.is_file() and entry.name == f"{file_name}.txt":
            return entry.path
        elif entry.is_dir():
            result = find_file(entry.path, file_name)
            if result:
                return result
    return None

def list_info(folder_path):
    folder_name = os.path.basename(folder_path)
    print(f"Folder: {folder_path}")
    print(f"Total folder size: {get_folder_size(folder_path)} bytes")
    if has_limit(folder_name):
        folder_size = get_folder_size(folder_path)
        limit = get_limit(folder_name)
        print(f"Size limit: {limit} bytes")
        print("-" * 30)
        if folder_size > limit:
            print("Warning: Folder size exceeds the limit.")
            print("-" * 30)
    else:
        print("Folder size is within the limit.")
        print("-" * 30)
    print("Files:")

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            file_type = os.path.splitext(filename)[1]
            file_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

            print(f"File name: {filename}")
            print(f"File size: {file_size} bytes")
            print(f"File type: {file_type}")
            print(f"File creation time: {file_creation_time}")
            print("-" * 30)
        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)
            dir_size = f"{get_folder_size(dir_path)} bytes"
            dir_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(dir_path))
            print(f"File name: {dirname}")
            print(f"File size: {dir_size}")
            print(f"File creation time: {dir_creation_time}")
            print("-" * 30)
    return None

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

def is_empty(folder_path):
    items = os.listdir(folder_path)

    if len(items) == 0:
        return True
    else:
        return False


main()