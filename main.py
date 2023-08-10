import os

def main():
    while(True):
        print("1.Create file \n "
              "2.Delete file \n "
              "3.Create folder \n "
              "4.Delete folder \n "
              "5.Folder list \n "
              "6.Open folder \n "
              "7.Quit")
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
                print("bye")
                return False
            case _:
                print("INCORRECT OPTION")

def createFile():
    print("createFile")

def deleteFile():
    print("deleteFile()")

def createFolder():
    print("createFolder()")

def deleteFolder():
    print("deleteFolder()")

def listFolder():
    print("listFolder()")

def openFolder():
    print("openFolder()")

main()