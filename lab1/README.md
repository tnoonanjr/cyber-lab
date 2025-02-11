###  Lab 1

# Question 1
Our target user SkyRedFalcon914, uses a very common password. We can crack his account using a short list of common passwords that we iterate over. This is a form of brute force attack.

# Question 2
It's possible that rest of the gang use a password in our short list. In Question 2 we try the same method on the rest of the gang. 

# Question 3
Our short list won't be enough to crack most users. In Question 3, we test a more comprehensive list of pwned passwords against the gang. Note that trying each password against the Login file is very expensive. This attack takes a very long time (many hours), but eventually we may crack a user.

# Question 4
We gain access to a file of plaintext leaks of users name and password pairs. We check if our targets are in this leak and check if we are able to log in. 

# Question 5
Cyber attacks may gain access to a list of users and their hashed passwords. An example of this is the Linkedin hack in 2012. Sometimes users may use common passwords, but add a couple digits to make it a bit more secure. We compare the pwned passwords with two digits appended to the end to the hash of users in our target group. 

# Question 6
In this case we gain access to hashed passwords, but they are salted. Luckily, we also have the salt. We compare pwned passwords with one digit hashed with their salt against the hashed-and-salted password to see if we find a match.
