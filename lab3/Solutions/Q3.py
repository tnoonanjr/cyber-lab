from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import subprocess


def Q3():
    
    files = []

    key = RSA.import_key(open('../../lab3/Q3pk.pem').read())
    print(key)
    
    output = subprocess.run(["ls", "../../lab3/Q3files"], capture_output=True, text=True).stdout.strip("\n")
    get_files = output.split()
    for file in get_files:
        b = file.split(".")
        if "sign" not in b:
            files.append(file)
    
    
    
    for file in files:
        with open(f"../../Q3files/{file}.sign", "rb") as fb:
            signature = fb.read()
        
        with open(f"../Q3files/{file}", "rb") as gb:
            bin_text = gb.read()
        
        h = SHA256.new(bin_text)
        
        try:
            pkcs1_15.new(key).verify(h, signature)
            print("The signature is valid.")
            print(f"File: {file}")
            break
        except:
            print("The signature is not valid.")
    
    
if __name__ == "__main__":
    Q3()
