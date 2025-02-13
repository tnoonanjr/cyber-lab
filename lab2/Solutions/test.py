import os
import sys

if __name__ == "__main__":
    do_stuff = 1234
    more_stuff = False
    for element in sys.argv:
        print(element)
        
# 56858c6a52df13e2ae9f3a7cd02bc623c4b42d3670960249a6d50ebe4c5b9d7d
import sys

command = str(sys.argv)[1:-2]
command = command.replace(',','').replace("'","")

with open("Q1B.out", 'a') as file:
    file.write(str(command)+"\n")
    