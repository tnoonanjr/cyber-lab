from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def D4():
    
    with open("../Q4files/Encrypted4", "rb") as f:
        encrypted_text = f.read()
    
    with open("../Q4files/.key.txt", "rb") as g:
        variable = g.read()
    
    cipher = AES.new(variable, AES.MODE_CBC)
    
    
    plaintext = cipher.decrypt(encrypted_text)
    
    
    unpadded = unpad((plaintext), AES.block_size)
    
    print(unpadded)

    # Try decoding with a common encoding, like 'utf-8', 'latin1', or 'iso-8859-1'
    decoded_string = unpadded.decode('latin1', errors='ignore')  # Using 'latin1' for this example
    print(decoded_string)
    
    

if __name__ == "__main__":
    D4()
