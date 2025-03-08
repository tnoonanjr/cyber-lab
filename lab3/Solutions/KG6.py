# Write a key-generation program KG6.py, to generate a keypair of a public key e and a 
# private key d. Save them in files e.key and d.key in sub-directory Solutions. 
import secrets

def generate_keys(output_file):
    key = secrets.token_bytes(16)
    key_output_file = open(output_file, "wb")
    key_output_file.write(key)
    key_output_file.close
    return output_file

if __name__ == '__main__':
    public_key = generate_keys("e.key")
    private_key = generate_keys("d.key")

    with open(public_key, "rb") as file:
        print(file.read())
    with open(private_key, "rb") as file:
        print(file.read())
    