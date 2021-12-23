import index
import time as t
import os

print("Welcome")

while 3 > 2:
    t.sleep(1)
    inputbar = input("SETTINGS: ")
    if inputbar == "_new":
        inp = input("NAME : ")
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
