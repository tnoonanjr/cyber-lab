from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import MD5

def D5():

    with open("../Q5files/Encrypted5", "rb") as g:
        encrypted = g.read()
    
    
    
    BLOCKSIZE = 1024
    h = MD5.new()

    with open('../Q5files/R5.py' , 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            h.update(buf)
            buf = afile.read(BLOCKSIZE)
    
    hf = h.digest()
    
    cipher = AES.new(hf, AES.MODE_CBC)
    
    
    decrypted = cipher.decrypt(encrypted)
    
    unpadded = unpad((decrypted), AES.block_size)
    
    with open(".out5.txt", "wb") as o:
        o.write(unpadded)
    
    with open(".out5.txt" ,"rb") as r:
        r.seek(16)
        final = r.read()
    
    plaintext = final.decode('latin1', errors='ignore')  
   
    
    print(plaintext)


if __name__ == "__main__":
    D5()