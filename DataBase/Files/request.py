import index
import time as t
import os
import time

print("Welcome")
print("to create a file do _new and NAME : will show up")
print("type in your file name afterwards.")
print("do _edit to edit a file, bare in mind that you have to type in the .filetype")
print("the file type the database uses .dtb therefore if you wish to edit .json files for example")
print("it wont edit the text it would just be (again for example pourpeses): EXAMPLE TEXT")
print("_read will read files")
print("_del deletes files")

time.sleep(1.5)

while 3 > 2:
    t.sleep(1)
    inputbar = input("SETTINGS: ")
    if inputbar == "_new":
        inp = input("NAME : ")
        if " " in inp:
            print("invalid)
        else: 
            index.files.new(inp.lower() + ".dtb")
    if inputbar == "_edit":
        inp = input("FILE NAME : ")
        index.files.edit(inp.lower())
    if inputbar == "_read":
        inp = input("FILE NAME : ")
        print("")
        index.files.read(inp.lower())
        t.sleep(2.5)
    if inputbar == "_del":
        inp = input("FILE : ")
        os.remove(inp.lower())
    if inputbar == "_exit":
        break

