from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

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

if __name__ == '__main__':
    d = Decryptor(output_path='../../lab3/Q4files/Encrypted4',
                  auxiliary_output_path='../../lab3/Q4files/.key.txt')
    pt = d.aes_decrypt()
    print(pt)