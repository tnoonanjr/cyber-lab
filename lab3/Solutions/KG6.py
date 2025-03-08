# Write a key-generation program KG6.py, to generate a keypair of a public key e and a 
# private key d. Save them in files e.key and d.key in sub-directory Solutions. 
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
with open("e.key", "wb") as public_out_file:
    public_out_file.write(key.publickey().export_key())

with open("d.key", "wb") as private_out_file:
    private_out_file.write(key.export_key())
    
with open("e.key", "rb") as file:
    print(file.read())
with open("d.key", "rb") as file:
    print(file.read())
    