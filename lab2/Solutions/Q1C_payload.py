# 56858c6a52df13e2ae9f3a7cd02bc623c4b42d3670960249a6d50ebe4c5b9d7e
import sys

command = str(sys.argv)[1:-2]
command = command.replace(',','').replace("'","")

with open("Q1C.out", 'a') as file:
    file.write(str(command)+"\n")
    