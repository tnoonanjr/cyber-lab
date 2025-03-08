import os


def decrypt(encrypted_file, shared_key):
    with open(encrypted_file, "rb") as to_be_decrypted:
        to_be_decrypted_content = to_be_decrypted.read()

def decrypt_walk(shared_key)
    uncompromised_files = []
    current_folder = os.getcwd()
    dir = os.listdir(current_folder)
    for file in dir:
        path = os.path.join(current_folder, file)
        if os.path.isfile(path) and file.endswith(".encrypted"):
            try:
                uncompromised = decrypt(file, shared_key)
                uncompromised_files.append(compromised)
            except:
                print(f"An error occured decrypting file: {file}\n")

    return uncompromised_files



def main():
    if os.argv != 2:
        print("Usage: python AD6.py [DecryptedSharedKey path]")
        return 1
    
    pvt_k = b'\xe5}U\xb0H\xc2\x08f\xf92\x0b]\xdd\x01i32/K\xee\xda>s\xc9\xd0\x9f\x05\x84\x9d\x8c\xa9\xc9'

    decrypt(pvt_k)
    return 0
    

main()