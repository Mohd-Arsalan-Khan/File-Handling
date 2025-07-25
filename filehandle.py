from pathlib import Path

def readfileandfolder():
    path = Path("")
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Please enter your file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in this file :- ")
                fs.write(data)
            print("FILE CREATED SUCESSFULLY")
        else:
            print("This file is already exsist")
    
    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Please enter the name of the file you want to read :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
            print("FILE READ SUCESSFULLY")
        else:
            print("No such file exist")    

    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Please enter the file name you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of the file")
            print("Press 2 for overwriting the data of the file")
            print("Press 3 for appending some content in the file")

            res = int(input("Enter you response :- "))

            if res == 1:
                namesecond = input("Please enter the new file name :- ")
                pathsecond = Path(namesecond)
                p.rename(pathsecond)

            if res == 2:
                with open(p, "w") as fs:
                    data = input("Please enter you want to update this will overwrite the data :-")
                    fs.write(data)

            if res == 3:
                with open(p, "a") as fs:
                    data = input("Please enter you want to append in the file :-")
                    fs.write(" " + data)
        else:
            print("No such file exist")    
    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the file name you want to delete :-")
        p = Path(name)

        if p.exists() and p.is_file():
            p.unlink()
            print("FILE REMOVE SUCESSFULLY")
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An error occured as {err}")

print("Enter 1 for creating a file")
print("Enter 2 for reading a file")
print("Enter 3 for updating a file")
print("Enter 4 for deletion a file")

check = int(input("Please tell me your number between:-"))

if check == 1: 
    createfile()
if check == 2:
    readfile()
if check == 3:
    updatefile()
if check == 4:
    deletefile()