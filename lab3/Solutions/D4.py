from decrypt import Decryptor

d = Decryptor(output_path='../../lab3/Q4files/Encrypted4',
              auxiliary_output_path='../../lab3/Q4files/.key.txt')
sol = d.aes_decrypt()
print(sol)