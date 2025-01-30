import subprocess
import time

start = time.time()

file = "../Q2/MostCommonPWs"
file_gang = "../Q2/gang"
gang_list = []
pass_list = []

# construct a queue of the gang's usernames
with open(file_gang, "r") as file_gang:   
    for row in file_gang:
        gang_list.append(row.strip())

# construct a queue of common passwords
with open(file, "r") as file:
    for row in file:
       pass_list.append(row.strip())

# brute force check all passwords for all users
for user in gang_list:
    for passwd in pass_list:
        output = subprocess.run(["python3", "../Q1/Login.pyc", user, passwd], capture_output=True, text=True)
        if check.stdout[6] == "s": return # Login [s]ucessful is the only output with s at idx 6   

end = time.time()

print(f"Start: {start} End: {end} Elapsed: {end-start}")
