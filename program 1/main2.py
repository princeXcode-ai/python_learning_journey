from pathlib import Path
import os

def readfileandfolder():
    path= Path( '.' )
    items=list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")
 
 
def createfile():
    try:
        readfileandfolder()
        name = input("tell your file and folder name :- ")
        p = Path(name)
        if not p.exists():
            with open (p,"w") as fs:
                data = input("what do you want to write in file = ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY") 
    
        
        else:
            print("this file is already exists")    
        
    except Exception as err:
        print(f"an error occured as {err}")
            
        
        
def readfile():
    try:
        readfileandfolder()
        name = input("which file and folder do you want to read :- ")
        p= Path(name)
        if p.exists() and p.is_file():
            with open (p,"r") as fs:
                data = fs.read()
                print(data)
            print("Readed successfully")

        else:
            print("file does not exists")
            
    except Exception as err:
        print(f"an error occured as {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("which file you want to delete:- ")
        p=Path(name)
        
        if p.exists() and p.is_file():
            os.remove(p)
            print ("FILE DELETE SUCESSFULLY")
            
        else:
            print("SUCH DATA NOT EXISTS")


    except Exception as err:
        print(f"an error occured as {err}")
    

def updatefile():
    try:
        readfileandfolder()
        name= input("which file do you want to update:- ")
        p= Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing name of file:- ")
            print("Press 2 for overwriting the data of file:- ")
            print("Press 3 for appending some data in a file:- ")
            
            res = int (input("tell your response :- "))
            
            if res == 1:
                name2= input("write your new file name:- ")
                p2 =Path(name2)
                p.rename(p2)
                
            if res == 2:
                with open(p,"w") as fs:
                    data = input("tell what you want to write this is will overwrite to data :- ")
                    fs.write(data)
                    
            if res == 3:
                with open(p,"a") as fs:
                    data = input("write what you want to append:- ")
                    fs.write(" "+data)

    except Exception as err:
        print(f"an error occured as {err}")
 


print("Press 1 for creating a file :- ")
print("Press 2 for reading a file :- ")
print("Press 3 for deleting a file :- ")
print("Press 4 for upadating a file :- ")

check = int(input("What are you want to do in file :- "))

if check == 1:
    createfile()

if check ==2:
    readfile()

if check ==3:
    deletefile()
    
if check == 4:
    updatefile()