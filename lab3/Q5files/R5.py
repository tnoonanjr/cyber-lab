# This is an obfuscated ransomware file.  
# To learn more about obfuscation, see the following links:
        # https://searchsecurity.techtarget.com/definition/obfuscation
        # https://www.geeksforgeeks.org/what-is-obfuscation/
# Your goal is to go through this funky code and understanmd what it is that it is doing, 
# and how it is doing it.
# Once you understand how itis encrypting a user's file, werite a program (decrypt2.py) 
# that decrpyts encrypted2.txt.  

# This is the ransomware program that encrypts a specified file.  
# Make sure you spend time to understand how it works.  
# Feel free to change the input file to get a snesne of the programs capabilities.  
# The given input program is an example .txt file, with several made up passwords.  

#Use the following link to read documentation on this imported library:
        #https://pycryptodome.readthedocs.io/en/latest/

import math
from Crypto.Cipher import AES
import binascii
from Crypto.Util.Padding import pad
import time 
from Crypto.Random import get_random_bytes 
import socket
import sys
from Crypto.Hash import MD5

def MyChecksum(hexlist):
    summ=0
    carry=0
    for i in range(0,len(hexlist),2):
        summ+=(hexlist[i]<< 8)  + hexlist[i+1]
        carry=summ>>16
        summ=(summ & 0xffff)  + carry
    while( summ != (summ & 0xffff)):
        carry=summ>>16
        summ=summ & 0xffffffff  + carry
    summ^=0xffff 
    return summ
myHost = 'localhost'
myPort = 50007
BLOCKSIZE = 2048
h = MD5.new()
count = 0

with open( 'R5.py' , 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        count = count + 1
        h.update(buf)
        buf = afile.read(BLOCKSIZE)
hf = h.digest()
bird = hf
hawk = str(bird)
of2 = '.key.txt'
file_out = open(of2, "w") 
file_out.write("") # Write the varying length ciphertext to the file (this is the encrypted data)
file_out.close()
iF = 'p2.txt' # Input file
oUt = 'Encrypted5' #outputted cipher text (can rename)
fin = open(iF, 'rb')
chicago = fin.read()
n = 23
f2 = 1
for i in range(1,n+1):
    f2 = f2 * i
fin.close() 
detroit = AES.new(bird, AES.MODE_CBC)  #  cipher
ogD = detroit.encrypt(pad((chicago), AES.block_size))
fon = open(oUt, "wb")
fon.write(detroit.iv)
fon.write(ogD)
fon.close()
print('OK')

try:
    server_sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
    server_sock.connect((myHost, myPort))
except OSError as e:
    if server_sock:
        server_sock.close()
#    sys.exit(1)