# Lab 3 - Cryptography, Malware & Ransomware


## Questions 1-3 - Checksum

# Question 1
Given a folder of executable files, check for a match for the target hash via brute force running each file.


### Question 2
Given a folder of executable files, check for a match for the target hash by hashing each executable (...?) and checking for equality.


### Question 3
Given a public key, check for authenticity via checking .sign files against the public key.

## Questions 4-5 - Decrypt

### Question 4
Given a python file that encrypts file, develop an algorithm to decrypt the files.

### Question 5
Given a obfucated file; i.e. a file that is written in a way to hide its true purposes, develop an algorithm to decrypt the file.


## Question 6 - Ransomware
Create a ransomware with two public keys; an ecryption key e, and decription key d. 

We use a 16-byte (128bits) key in order to encrypted the file data. This means that a brute force attack may have to try up to 2^128 permutations to brute-force our key in the worst case. There are no computers today that can run this many permutations in a reasonable amount of time. 

### KG6.py

### R6.py

### AD6.py

### D6.py

