from decrypt import Decryptor

d = Decryptor(output_path='../../lab3/Q5files/Encrypted5',
              auxiliary_output_path='../../lab3/Q5files/R5.py')
sol = d.md5_obfuscated_decrypt()
print(sol)