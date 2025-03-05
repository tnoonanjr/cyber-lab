from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import subprocess


def Q3():
    
    with open("../Q3pk.pem", "r") as f:
        #pub_key = f.read()
        res = ""
        for row in f:
            row = row.strip()
            if row != "-----BEGIN PUBLIC KEY-----" and row != "-----END PUBLIC KEY-----":
                res += row
                
    print(res)
    
    output = subprocess.run(["ls", "../Q2files"], capture_output=True, text=True).stdout.strip("\n")
    
    files = output.split()
    
    key = RSA.import_key(open('public_key.der').read())
    
    h = SHA256.new(message)
    
    for file in files:
        
    
        try:
            pkcs1_15.new(key).verify(h, signature)
            print("The signature is valid.")
        except (ValueError, TypeError):
                print("The signature is not valid.")
    
    
if __name__ == "_main__":
    Q3()
