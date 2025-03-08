from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import MD5

class Decryptor:
    def __init__(self, output_path: str, auxiliary_output_path) -> None:
        self.output_path = output_path
        self.auxiliary_output_path = auxiliary_output_path
    
    def aes_decrypt(self):
        ciphertext_binary_file = open(self.output_path, 'rb')
        init_vector = ciphertext_binary_file.read(AES.block_size)              # start after the initialization vector
        ciphertext_binary = ciphertext_binary_file.read()
        ciphertext_binary_file.close()

        key_file = open(self.auxiliary_output_path, 'rb') 
        key_binary = key_file.read()
        key_file.close()

        cipher = AES.new(key_binary, AES.MODE_CBC, init_vector)
        plaintext_padded = cipher.decrypt(ciphertext_binary)
        plaintext = unpad((plaintext_padded), AES.block_size).strip()
        return plaintext
    
    def md5_obfuscated_decrypt(self):
        ciphertext_binary_file = open(self.output_path, 'rb')
        init_vector = ciphertext_binary_file.read(AES.block_size)              # start after the initialization vector
        ciphertext_binary = ciphertext_binary_file.read()
        ciphertext_binary_file.close()

        hash = MD5.new()
        BLOCKSIZE = 2048

        with open(self.auxiliary_output_path, "rb") as file:
            buf = file.read(BLOCKSIZE)
            while len(buf) > 0:
                hash.update(buf)
                buf = file.read(BLOCKSIZE)
        
        hash_digest = hash.digest()

        cipher = AES.new(hash_digest, AES.MODE_CBC, init_vector)
        plaintext_padded = cipher.decrypt(ciphertext_binary)
        plaintext = unpad((plaintext_padded), AES.block_size).strip()

        return plaintext

if __name__ == '__main__':
    protocol = int(input(f"Enter test protocol:\n"))
    if protocol == 4 or protocol == 0:
        d = Decryptor(output_path='../../lab3/Q4files/Encrypted4',
                      auxiliary_output_path='../../lab3/Q4files/.key.txt')
        sol = d.aes_decrypt()
        print(sol)
    if protocol == 5 or protocol == 0:
        d = Decryptor(output_path='../../lab3/Q5files/Encrypted5',
                      auxiliary_output_path='../../lab3/Q5files/R5.py')
        sol = d.md5_obfuscated_decrypt()
        print(sol)