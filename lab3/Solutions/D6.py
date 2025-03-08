from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os
import sys

def decrypt(encrypted_file, shared_key):
    with open(encrypted_file, "rb") as to_be_decrypted:
        init_vector = to_be_decrypted.read(16)
        to_be_decrypted_content = to_be_decrypted.read()
    
    cipher = AES.new(shared_key, AES.MODE_CBC, init_vector)
    decrypted_content_padded =  cipher.decrypt(to_be_decrypted_content)
    decrypted_content = unpad(decrypted_content_padded, AES.block_size)

    decrypted = encrypted_file.removesuffix(".encrypted")
    with open(decrypted, "wb") as decrypted_file:
        decrypted_file.write(decrypted_content)
    return decrypted

def decrypt_walk(shared_key):
    decrypted_files = []
    current_folder = os.getcwd()
    dir_list = os.listdir(current_folder)
    for file in dir_list:
        path = os.path.join(current_folder, file)
        if os.path.isfile(path) and file.endswith(".encrypted"):
            try:
                uncompromised = decrypt(file, shared_key)
                decrypted_files.append(uncompromised)
            except:
                print(f"An error occured decrypting file: {file}\n")

    return decrypted_files



def main():
    if len(sys.argv) != 2:
        print("Usage: python AD6.py [DecryptedSharedKey path]")
        return 1
    
    with open(sys.argv[1], "rb") as file:
        decrypted_shared_key = file.read()
    try:
        sol = decrypt_walk(decrypted_shared_key)
        print(sol)
    except:
        print(f"An error occured decrypting {sys.argv[1]}")
    return 0
    
main()