import subprocess
import hashlib
from datetime import datetime

class SkeletonKey:
    ''' 
    Skeleton Key is an object designed to adapt to each questions' parameters and search for users' password(s).
    
    params:
        user_file_path
            - Input the path to the file that contains usernames if applicable
        
        passwd_pwned_path 
            - Input the path to the file that contains common or pwned passwords
        
        passwd_hashed_path
            - Input secondary path to file that contains hashed passwords
        
        users 
            - Input the usernames of users if there is no file as a list
        
        exe_path
            - Input the path of the python file to execute the command 'python3 [path] [username] [password]'

        cracked_users
            - Sets a maxmimum amount of users to crack for execessively long bruteforces
        
        print_interval
            - Input how often you wish to print progress statements
    
    '''
    def __init__(self, user_file_path=None, passwd_pwned_path=None, passwd_hashed_path=None, to_file_path=None, users=None, exe_path=None, cracked_users=None, print_interval=None):
        self.user_file_path = user_file_path
        self.passwd_pwned_path = passwd_pwned_path
        self.exe_path = exe_path
        self.passwd_hashed_path = passwd_hashed_path
        self.to_file_path = to_file_path
        self.cracked_users = cracked_users if cracked_users else set()
        self.users = self.compile_file_to_list() if user_file_path else list([users])
        self.print_interval = print_interval
        self.number_runs = 0
    
    def compile_file_to_list(self):
        ''' 
        Compiles the file of usernames to a list to iterate over in the bruteforce function
            - This method assumes the length of an arbitrary list of usernames << the length of an arbitrary list of common passwords
        
        '''
        compiled_list = []
        with open(self.user_file_path, "r") as file:
            for row in file:
                item = row.strip()
                if item not in self.cracked_users:
                    compiled_list.append(item)
        
        return compiled_list

    def attempt_crack(self, user, passwd, ignore_else=False):
        '''
        Attempts to crack user `user` with passwd `passwd`
        Returns True and prints to terminal if crack attempt was successful
        Returns False otherwise

        '''
        run = subprocess.run(["python3", self.exe_path, user, passwd], capture_output=True, text=True)
        curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if run.stdout == "Login successful.\n":
            print(f"[{curr_time}] Attempt {self.number_runs} \n==!!!== Successful crack attempt ==!!!== \nUser: {user} \nPassword: {passwd}\n")
            
            return True
        
        else: 
            if not ignore_else:
                print(f"[{curr_time}] Attempt {self.number_runs} \n==---== Failed crack attempt ==---== \nUser: {user} \nPassword: {passwd}\n")
                return False
    
    def log_crack_attempts(self, user, passwd):
        '''
        Logs an attempt every `self.print_interval` runs to the terminal
        showing the attempt number, timestamp, and tested credentials
        Returns void

        '''

        if self.print_interval:
            if self.number_runs % self.print_interval == 0: 
                curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{curr_time}] Attempt {self.number_runs} \nCurrent test: {user} --> {passwd}\n")

    def parse_row(self, row):
        return row.strip().split(",")
    
    

    ###########################################
    ##########     Q1, Q2, Q3       ###########
    ###########################################

    def crack_pass_bruteforce(self, max_cracked=float('inf')): 
        '''
        Attempts to crack the password by checking against the file for every password in passwd_pwned_path
        
        '''
        number_cracked = 0
        cracked_map = dict()

        try:
            for user in self.users:
                with open(self.passwd_pwned_path, "r") as file:
                    for row in file:
                        self.number_runs += 1
                            
                        passwd = row.strip()
                        
                        if self.attempt_crack(user, passwd, ignore_else=True):    
                            number_cracked += 1
                            cracked_map[user] = passwd
                            if number_cracked >= max_cracked: return cracked_map

                        self.log_crack_attempts(user, passwd)  
            
            return cracked_map
        
        except KeyboardInterrupt:
            print("Quit successfully\n")



    ###########################################
    ##########          Q4          ###########
    ###########################################
        
    def crack_pass_leaked_database(self): 
        '''
        Attempts to crack given users passwords using a file denoting a leaked database of users and their passwords
        
        '''
        cracked_map = {}
        user_set = set(self.users)

        with open(self.passwd_pwned_path, "r") as file:
            for row in file:
                self.number_runs += 1
                user, passwd = self.parse_row(row)

                if user in user_set:
                    if self.attempt_crack(user, passwd):
                        cracked_map[user] = passwd
                        return cracked_map
                
                self.log_crack_attempts(user, passwd)  



    ###########################################
    ##########          Q5          ###########
    ###########################################

    def crack_pass_hash_brute_force(self): 
        '''
        Attempts to crack the password of users by comparing the hash of a common password 
        plus two appended digits on the end against the hashed file
        
        '''
        user_set = set(self.users)
        hash_dict = {}

        with open(self.passwd_hashed_path, "r") as file:
            for row in file:
                user, hashkey = self.parse_row(row)

                if user in user_set:
                    hash_dict[hashkey] = user
        
        with open(self.passwd_pwned_path) as file:
            for row in file:
                # Concatenate 00-99
                passwd = row.strip()
                for i in range(100): 
                    self.number_runs += 1

                    if i < 10: concat_number = f"0{i}"
                    else: concat_number = str(i)

                    concat_passwd = passwd + concat_number

                    # Hash current password
                    h = hashlib.sha256()
                    h.update(bytes(concat_passwd, "utf-8"))
                    hash_candidate = h.hexdigest()

                    if hash_candidate in hash_dict:
                        user = hash_dict[hash_candidate]

                        if self.attempt_crack(user, concat_passwd):
                            return
                        
                    self.log_crack_attempts(user, concat_passwd)
    


    ###########################################
    ##########          Q6          ###########
    ###########################################

    def crack_pass_hash_salted_brute_force(self):
        '''
        Attempts to crack the password of users by comparing the salted password hashed with a common password 
        plus an appended digit on the end against the hashed and salted file
        
        '''
        self.file_reset(self.to_file_path)
        user_hash_salt_map = dict()

        with open(self.passwd_hashed_path, "r") as file:
            for row in file:
                username, salt, hash_salted = self.parse_row(row)

                if username in self.users:
                    user_hash_salt_map[hash_salted] = (salt, username)
                
        for hash_salted in user_hash_salt_map:
                salt, username = user_hash_salt_map[hash_salted][0], user_hash_salt_map[hash_salted][1]
                with open(self.passwd_pwned_path, "r") as file:
                    for row in file:
                        row = row.strip()

                        for i in range(10):
                            self.number_runs += 1
                            passwd_candidate = salt + row + str(i)

                            h = hashlib.sha256()
                            h.update(bytes(passwd_candidate, "utf-8"))
                            hash_candidate = h.hexdigest()

                            if hash_candidate in user_hash_salt_map:
                                unsalted_passwd = row + str(i)
                                is_passwd = self.attempt_crack(username, unsalted_passwd)
                                if is_passwd:
                                    self.to_file(username, unsalted_passwd, self.to_file_path)
                            
                        self.log_crack_attempts(username, passwd_candidate)

    def to_file(self, username, unsalted_passwd, path):
        """
        Takes in username, password, and file path and writes the username and password to the file

        """
        with open(path, "a") as file:
            print(f"in path {path}")
            file.write(f"{username}, {unsalted_passwd}")
    
    def file_reset(self, path):
        ''' Wipes file in path '''
        with open(path, "w") as _:
            pass

        
if __name__ == '__main__':
    ###########################################
    ##########          Q1          ###########
    ###########################################
    test_param = [
        "/home/cse/Lab1/Q1/MostCommonPWs",   # passwd path
        "SkyRedFalcon914",                   # users
        "/home/cse/Lab1/Q1/Login.pyc"        # exe path
        ]
    key = SkeletonKey(passwd_pwned_path = test_param[0],
                      users = test_param[1],
                      exe_path = test_param[2])
    
    key.crack_pass_bruteforce()



    ###########################################
    ##########          Q2          ###########
    ###########################################
    test_param = [
        "/home/cse/Lab1/Q2/MostCommonPWs",   # passwd path
        "/home/cse/Lab1/Q2/gang",            # user path
        "/home/cse/Lab1/Q2/Login.pyc"        # exe path
    ]
    key = SkeletonKey(passwd_pwned_path = test_param[0],
                      user_file_path = test_param[1],
                      exe_path = test_param[2],
                      cracked_users=['SkyRedFalcon914'])

    key.crack_pass_bruteforce()

    ###########################################
    ##########          Q3          ###########
    ###########################################
    ### ! Runs for many hours, Ctrl-C out ! ###
    ###########################################
    test_param = [
        "/home/cse/Lab1/Q3/PwnedPWs100k",   # passwd path
        "/home/cse/Lab1/Q3/gang",            # user path
        "/home/cse/Lab1/Q3/Login.pyc"        # exe path
    ]
    key = SkeletonKey(passwd_pwned_path = test_param[0],
                      user_file_path = test_param[1],
                      exe_path = test_param[2],
                      cracked_users=set(["SkyRedFalcon914", "MountainPurpleShark585"]),
                      print_interval=100)
    
    key.crack_pass_bruteforce(max_cracked=1)



    ###########################################
    ##########          Q4          ###########
    ###########################################
    test_param = [
        "/home/cse/Lab1/Q4/PwnedPWfile", # passwd path
        "/home/cse/Lab1/Q4/gang", # user path
        "/home/cse/Lab1/Q4/Login.pyc" # exe path
    ]
    key = SkeletonKey(passwd_pwned_path = test_param[0],
                      user_file_path = test_param[1],
                      exe_path = test_param[2],
                      cracked_users=set(["SkyRedFalcon914", "MountainPurpleShark585"]),
                      print_interval=100)
    
    key.crack_pass_leaked_database()



    ###########################################
    ##########          Q5          ###########
    ###########################################         
    test_param = [
        "/home/cse/Lab1/Q5/HashedPWs",       # passwd path
        "/home/cse/Lab1/Q5/gang",            # user path
        "/home/cse/Lab1/Q5/Login.pyc",        # exe path
        "/home/cse/Lab1/Q5/PwnedPWs100k"     # pwned path
    ]
    
    key = SkeletonKey(passwd_hashed_path= test_param[0],
                      passwd_pwned_path= test_param[3],
                      user_file_path= test_param[1],
                      exe_path= test_param[2],
                      cracked_users={"SkyRedFalcon914", "MountainPurpleShark585"},
                      print_interval=1000000)

    key.crack_pass_hash_brute_force()

    ###########################################
    ##########          Q6          ###########
    ###########################################
    params = [
        "/home/cse/Lab1/Q6/SaltedPWs",                  # passwd path
        "/home/cse/Lab1/Q6/PwnedPWs100k",               # aux file path
        "/home/cse/Lab1/Q6/gang",                       # user path
        "/home/cse/Lab1/Q6/Login.pyc",                  # exe path
        "/home/cse/Lab1/Solutions/Q6_crackedPasswords"  # to file path
    ]

    key = SkeletonKey(passwd_hashed_path= params[0],
                  passwd_pwned_path= params[1],
                  user_file_path= params[2],
                  exe_path= params[3],
                  to_file_path= params[4],
                  print_interval= 500000)

    key.crack_pass_hash_salted_brute_force()
