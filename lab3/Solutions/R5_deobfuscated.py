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

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Hash import MD5


h = MD5.new()
hf = h.digest()


of2 = '.key.txt'
file_out = open(of2, "w") 
file_out.write("") # Write the varying length ciphertext to the file (this is the encrypted data)
file_out.close()

iF = 'p2.txt' # Input file
oUt = 'Encrypted5' #outputted cipher text (can rename)

fin = open(iF, 'rb')
chicago = fin.read()
fin.close() 

hf = h.digest()
detroit = AES.new(hf, AES.MODE_CBC)  #  cipher

ogD = detroit.encrypt(pad((chicago), AES.block_size))



fon = open(oUt, "wb")
fon.write(detroit.iv)
fon.write(ogD)
fon.close()
print('OK')
