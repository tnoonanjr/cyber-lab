from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import subprocess


def Q3():
    
    files = []
    """
    with open("../Q3pk.pem", "r") as f:
        
        
        #pub_key = f.read()
        pub_key = ""
        for row in f:
            row = row.strip()
            if row != "-----BEGIN PUBLIC KEY-----" and row != "-----END PUBLIC KEY-----":
                pub_key += row
                
    print(pub_key)
    """
    key = RSA.import_key(open('../Q3pk.pem').read())
    print(key)
    
    output = subprocess.run(["ls", "../Q3files"], capture_output=True, text=True).stdout.strip("\n")
    get_files = output.split()
    for file in get_files:
        b = file.split(".")
        if "sign" not in b:
            files.append(file)
    
    
    
    for file in files:
        with open(f"../Q3files/{file}.sign", "rb") as fb:
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
