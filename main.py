import os
import shutil
from datetime import datetime
import pandas as pd
import zipfile
import datetime


def main():
    if not os.path.exists('test'): #fix
        os.mkdir('test')

    excel_file = 'D:\\Python\\test\\limit_info.xlsx'
    if not os.path.exists(excel_file):
        data = {'keys': [], 'values': []}
        df = pd.DataFrame(data)
        df.to_excel(excel_file, index=False)
    while True:
        print("1.Create file\n"
              "2.Delete file\n"
              "3.Create folder\n"
              "4.Delete folder\n"
              "5.Folder list\n"
              "6.Replace file\n"
              "7.Replace folder\n"
              "8.Set limit\n"
              "9.Delete all\n"
              "10.Archive all\n"
              "11.Quit")
        try:
            opp = int(input("Choose the operation: "))
            match opp:
                case 1:
                    file_name = input("Give a name for file: ").strip(" ")
                    wr = input("And give text that will be recorded to this file: ")
                    create_file(file_name, wr)
                    print("File had been created!")
                    print("-" * 30)
                case 2:
                    show_files()
                    file_name = input("Which file do you want to delete? ").strip(" ")
                    delete_file(file_name)
                    print("-" * 30)
                case 3:
                    folder_name = input("Give a name for folder: ").strip(" ")
                    create_folder(folder_name)
                    print("-" * 30)
                case 4:
                    show_folders()
                    folder_name = input("Which folder do you want to delete?").strip(" ")
                    delete_folder(folder_name)
                    print("-" * 30)
                case 5:
                    show_folders()
                    folder_name = input("Which folder's entries do you want to get? ").strip(" ")
                    list_folder(folder_name)
                    print("-" * 30)
                case 6:
                    file_name = input("Give a file name: ").strip(" ")
                    destination = input("Give folder name: ").strip(" ")
                    replace_file(file_name, destination)
                    print("-" * 30)
                case 7:
                    folder_name = input("Give the folder name: ").strip(" ")
                    destination = input("Give the destination name: ").strip(" ")
                    replace_folder(folder_name, destination)
                    print("-" * 30)
                case 8:
                    show_folders()
                    folder_name = input("Give the folder name: ").strip(" ")
                    limit = int(input("Give the limit size: ").strip(" "))
                    set_limit(folder_name, limit)
                case 9:
                    show_folders()
                    folder_name = input("Give the folder name: ").strip(" ")
                    criteria = int(input("Choose the criteria:\n1. by file type\n2. by created time\n3. by size "
                                         "\n4. to skip: ").strip(" "))
                    if criteria == 1:
                        file_type = input("Give the file type: ").strip(" ")
                        delete_all(folder_name, file_type=file_type)
                    elif criteria == 2:
                        date = input(
                            "Give the date(Year-month-day; all files before this date will be deleted): ").strip(" ")
                        creation_time = datetime.strptime(date, "%Y-%m-%d")
                        delete_all(folder_name, creation_time=creation_time)
                    elif criteria == 3:
                        size = int(input("Give a size(all files larger than this size will be deleted) ").strip(" "))
                        delete_all(folder_name, size=size)
                    else:
                        delete_all(folder_name)
                    print("-" * 30)
                case 10:
                    show_folders()
                    folder_name = input("Give the folder name: ").strip(" ")
                    criteria = int(input("Choose the criteria:\n1. by file type\n2. by created time\n3. by size "
                                         "\n4. to skip: ").strip(" "))
                    if criteria == 1:
                        file_type = input("Give the file type: ").strip(" ")
                        archive_all(folder_name, file_type=file_type)
                    elif criteria == 2:
                        date = input(
                            "Give the date(Year-month-day; all files before this date will be archived): ").strip(" ")
                        creation_time = datetime.strptime(date, "%Y-%m-%d")
                        archive_all(folder_name, creation_time=creation_time)
                    elif criteria == 3:
                        size = int(input("Give a size(all files larger than this size will be archived) ").strip(" "))
                        archive_all(folder_name, size=size)
                    else:
                        archive_all(folder_name)
                    print("-" * 30)

                case 11:
                    print("Good bye!")
                    print("-" * 30)
                    return False
                case _:
                    print("INCORRECT OPTION")
        except ValueError:
            print("You need to write integer number of operation.")
            print("-" * 30)


def create_file(file_name, wr):
    file = open(f"{file_name}.txt", "w")
    file.write(wr)
    file.close()
    shutil.move(f"D:\\Python\\{file_name}.txt", 'test')


def delete_file(file_name):
    file_path = find_file('test', file_name)
    if file_path:
        os.remove(file_path)
        print("File removed.")
    else:
        print("This file does not exist.")


def create_folder(folder_name):
    os.mkdir(f"D:\\Python\\test\\{folder_name}")
    print("Folder had been created!")
    return None


def delete_folder(folder_name):
    folder_path = find_folder('test', folder_name)
    if folder_path:
        if is_empty(folder_path):
            os.rmdir(folder_path)
            print("Folder removed.")
        else:
            ans = input("Are you sure? Folder is not empty. y/n ").strip(" ")
            if ans == "Y" or ans == "y":
                shutil.rmtree(folder_path)
                print("Folder removed.")
            else:
                print("Folder is not removed.")
    return None


def list_folder(folder_name):
    folder_path = find_folder('test', folder_name)

    if folder_path:
        list_info(folder_path)
    elif folder_name == "test":
        list_info('test')
    else:
        print(f"Folder '{folder_name}' not found.")
    return None


def replace_file(file_name, destination):
    destination_path = find_folder('test', destination)
    file_path = find_file('test', file_name)
    if destination_path and file_path:
        if has_limit(destination):
            destination_size = get_folder_size(destination_path)
            limit = get_limit(destination)
            if destination_size > limit:
                print("Warning: Folder size exceeds the limit. You can not add the file. ")
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
    return None


def replace_folder(folder_name, destination):
    folder_path = find_folder('test', folder_name)
    destination_path = find_folder('test', destination)
    if folder_path and destination_path:
        if has_limit(destination):
            destination_size = get_folder_size(destination_path)
            limit = get_limit(destination)
            if destination_size > limit:
                print("Warning: Folder size exceeds the limit. You can not add the folder. ")
            else:
                shutil.move(folder_path, destination_path)
                print("Folder replaced successfully!")
        else:
            shutil.move(folder_path, destination_path)
            print("Folder replaced successfully!")
    else:
        print(folder_path)
        print(destination_path)
        print("The destination or folder is not existing.")
    return None


limit_info = {}


def set_limit(folder_name, limit):
    folder_path = find_folder('test', folder_name)
    if folder_path:
        folder_size = get_folder_size(folder_path)
        if folder_size > limit:
            print("Warning: Current folder size exceeds the limit. Limit cannot be set.")
            print("-" * 30)
        else:
            excel_file = 'D:\\Python\\test\\limit_info.xlsx'
            df = pd.read_excel(excel_file)
            add_to_excel(excel_file, folder_name, limit)
            for index, row in df.iterrows():
                xl_folder_name = row['keys']
                xl_limit = row['values']
                limit_info[xl_folder_name] = xl_limit
            print(limit_info)
            print(f"Limit of {limit} bytes set successfully for folder {folder_name}.")
            print("-" * 30)
    else:
        print(f"Folder '{folder_name}' not found.")
        print("-" * 30)


def has_limit(folder_name):
    excel_file = 'D:\\Python\\test\\limit_info.xlsx'
    df = pd.read_excel(excel_file)
    for index, row in df.iterrows():
        xl_folder_name = row['keys']
        xl_limit = row['values']
        limit_info[xl_folder_name] = xl_limit
    return folder_name in limit_info


def get_limit(folder_name):
    return limit_info.get(folder_name)


def add_to_excel(excel_file, folder_name, limit):
    data = {'keys': [folder_name], 'values': [limit]}
    data_frame = pd.DataFrame(data)
    existing_data_frame = pd.read_excel(excel_file)
    updated_data_frame = pd.concat([existing_data_frame, data_frame], ignore_index=True)
    updated_data_frame.to_excel(excel_file, index=False)


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
            print(f"Folder name: {dirname}")
            print(f"Folder size: {dir_size}")
            print(f"Folder creation time: {dir_creation_time}")
            print("-" * 30)
    return None


def show_files():
    for dirpath, dirnames, filenames in os.walk('test'):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            print(f"File: {filename}, size: {file_size} bytes")
            print("-" * 30)


def show_folders():
    for dirpath, dirnames, filenames in os.walk('test'):
        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)
            dir_size = f"{get_folder_size(dir_path)} bytes"
            print(f"Folder: {dirname} size: {dir_size}")
            print("-" * 30)


def delete_all(folder_name, file_type=None, size=None, creation_time=None):
    folder_path = find_folder('test', folder_name)
    if folder_path:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if file_type and not filename.endswith(file_type):
                    continue
                if size and os.path.getsize(file_path) < size:
                    continue
                if creation_time and os.path.getctime(file_path) > creation_time.timestamp():
                    continue

                os.remove(file_path)
        print("Files removed.")
    else:
        print("Folder not found.")


def archive_all(folder_name, file_type=None, size=None, creation_time=None):
    folder_path = find_folder('test', folder_name)
    if folder_path:
        zip_file_name = f"{folder_name}.zip"
        with zipfile.ZipFile(zip_file_name, "w") as file_zip:
            for dirpath, _, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    if file_type and not filename.endswith(file_type):
                        continue
                    if size and os.path.getsize(file_path) < size:
                        continue
                    if creation_time and os.path.getctime(file_path) > creation_time.timestamp():
                        continue
                    file_zip.write(file_path, os.path.relpath(file_path, folder_path),
                                   compress_type=zipfile.ZIP_DEFLATED)
            print("Files archived.")
    else:
        print("Folder not found.")


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
