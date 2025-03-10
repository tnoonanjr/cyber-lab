# Lab 3 - Cryptography, Malware & Ransomware


## Questions 1-3 - Checksum

### Question 1
Given a folder of executable files, check for a match for the target hash via brute force running each file.


### Question 2
Given a folder of executable files, check for a match for the target hash by hashing each executable (...?) and checking for equality.


### Question 3
Given a public key, check for authenticity via checking .sign files against the public key.

## Questions 4-5 - Decryption

### Question 4
Given a python file that encrypts file, develop an algorithm to decrypt the files.

### Question 5
Given a obfucated file; i.e. a file that is written in a way to hide its true purposes, develop an algorithm to decrypt the file.


## Question 6 - Ransomware
Create a ransomware with two public keys; an ecryption key e, and decription key d. 
 

### KG6.py
Generates a public and private key to encrypt and decrypt target files. Keys are generated using the PyCryptdome object RSA. This method is best because to encrypt the files, the encryption script must be in the theoretical user's environment. If we do use something to the effect of RSA the encryption algorithm and keys would be visible to the user and they could decrypt the file themselves. Since RSA generates a public and private key, we can use the public key to encrypt, but it is useless in decryption. They would need access to the private key as well in order to return the files to normal.

### R6.py
Creates shared key & encrypts it for storgage, then uses the shared key to encrypt target files. The shared key is necessary to decrypt the files, but after encrypted it is useless to a hypothetical user. The shared key is encrypted using the PyCryptdome object PKCS1_OAEP, which is an asymmetric cipher generated using the RSA cipher with OAEP padding. This module allows us to encrypt using the public key and decrypt with a separate private key which is inaccessible to the supposed target. 


### AD6.py
File that would be only available to the theoretical attacker to decrypt the stored shared key that the user would likely send back to them as well as compensation the attacker likely demands. Decrypts the encrypted shared key that can be sent back to the user to decrpyt their files.

### D6.py
Takes the decrypted shared key and undoes the encryption algorithm to return the files to normal.

