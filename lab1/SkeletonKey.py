import subprocess
import hashlib
from datetime import datetime

class SkeletonKey:
    ''' 
    Skeleton Key is an object designed to adapt to each questions' parameters and search for users' password(s).
    
    params:
        user_file_path
            - Path of the file containing usernames (if applicable)
        
        passwd_file_path 
            - Path of the file containing passwords
        
        users 
            - List of usernames of users
            - Compiled from `user_file_path` if provided
        
        login_file_path
            - Path of the python file to attempt to crack
        
        hash_file_path
            - Path of the file containing hashes

        cracked_users
            - Sets a maxmimum amount of users to crack for execessively long bruteforces

        print_interval
            - Sets the interval of login attempts to print updates
    
    '''
    def __init__(self, user_file_path=None, passwd_file_path=None, users=None, login_file_path=None, hash_file_path=None, cracked_users=None, print_interval=None):
        self.user_file_path = user_file_path
        self.passwd_file_path = passwd_file_path
        self.login_file_path = login_file_path
        self.hash_file_path = hash_file_path
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

        run = subprocess.run(["python3", self.login_file_path, user, passwd], capture_output=True, text=True)

        if run.stdout == "Login successful.\n":
            curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{curr_time}] Attempt {self.number_runs} \n==!!!== Successful crack attempt ==!!!== \nUser: {user} \nPassword: {passwd}\n")
            
            return True
        
        return False
    

    def log_crack_attempts(self, user, passwd):
        '''
        Incremements `self.number_runs`.
        Logs an attempt every `self.print_interval` runs to the terminal, 
        showing the attempt number, timestamp, and tested credentials.
        Returns void.
        '''
        self.number_runs += 1

        if self.print_interval:
            if self.number_runs % self.print_interval == 0: 
                curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{curr_time}] Attempt {self.number_runs} \nCurrent test: {user} --> {passwd}\n")


    def parse_row(self, row):
        '''
        Splits a comma-separated string into a list of values after stripping whitespace.
        Returns the list of values.
        '''
        split_string = row.strip().split(",")
        return split_string

    ###########################################
    ##########      Q1, Q2, Q3      ###########
    ###########################################

    def crack_pass_bruteforce(self):
        '''
        Attempts to crack all users in `self.users` using passwords from `self.passwd_file_path`.
        Prints report upon successful login and returns.
        '''
        self.number_runs = 0

        try:
            for user in self.users:
                with open(self.passwd_file_path, "r") as file:
                    for row in file:
                            
                        passwd = row.strip()

                        self.log_crack_attempts(user, passwd)  
                        
                        if self.attempt_crack(user, passwd): return
        
        except KeyboardInterrupt:
            print("Quit successfully\n")
        
    ###########################################
    ##########          Q4          ###########
    ###########################################

    def crack_pass_leaked_database(self): # Used for Q4
        '''
        Attempts to crack users from `self.users` using a leaked database of logins.
        `self.passwd_file_path` should contain entries in format "<username>,<passwd>" 
        with each entry on a separate line.
        Prints report upon successful login and returns.
        '''
        self.number_runs = 0
        user_set = set(self.users)

        with open(self.passwd_file_path, "r") as file:
            for row in file:
                user, passwd = self.parse_row(row)

                self.log_crack_attempts(user, passwd)  

                if user in user_set:
                    if self.attempt_crack(user, passwd): return

    ###########################################
    ##########          Q5          ###########
    ###########################################

    def crack_pass_hash_brute_force(self):
        '''
        Attempts to crack users from `self.users` using a file containing their hashed password.
        `self.hash_file_path` should contain entries in format "<username>,<hashed_passwd>" 
        with each entry on a separate line.
        Prints report upon successful login and returns.
        '''
        self.number_runs = 0
        user_set = set(self.users)  
        hash_dict = {}              # Stores hash:user key-value pairs for lookup of hashes

        # Populate hash_dict with hashes associated with users in user_set
        with open(self.hash_file_path, "r") as file:
            for row in file:
                user, hashkey = self.parse_row(row)

                if user in user_set:
                    hash_dict[hashkey] = user

        # Attempts to find matching hashes for passwords and attempts to login with the associated user 
        with open(self.passwd_file_path) as file:
            for row in file:
                passwd = row.strip()
        
                for i in range(100): 
                    # Concatenate 00-99 to end of each password to test

                    if i < 10: concat_number = f"0{i}"
                    else: concat_number = str(i)

                    concat_passwd = passwd + concat_number

                    # Hash current password
                    h = hashlib.sha256()
                    h.update(bytes(concat_passwd, "utf-8"))
                    hash_candidate = h.hexdigest()

                    self.log_crack_attempts(user, passwd) 

                    if hash_candidate in hash_dict:
                        user = hash_dict[hash_candidate]

                        if self.attempt_crack(user, concat_passwd): return
                        

    ###########################################
    ##########          Q6          ###########
    ###########################################

    def crack_pass_hash_salt(self): 
        '''
        Attempts to crack users from `self.users` using a file containing their salt and salted hash.
        `self.hash_file_path` should contain entries in format "<username>,<salt>,<salted_hashed_passwd>" 
        with each entry on a separate line.
        Creates file "Q6_Cracked_Gang_Members" containing all cracked logins and their passwords.
        '''
        self.number_runs = 0
        user_set = set(self.users)
        salted_hash_set = set()     # Stores hashes of users in user_set
        user_salt_dict = {}         # Stores user:list(salt) key-value pairs
        cracked_dict = {}           # Stores user:passwd key-value pairs of cracked accounts

        # Populate salted_hash_set and user_salt_dict
        with open(self.hash_file_path, "r") as file:
            for row in file:
                user, salt, salted_hashkey = self.parse_row(row)

                if user in user_set:
                    salted_hash_set.add(salted_hashkey)

                    if user in user_salt_dict: user_salt_dict[user].append(salt)
                    else: user_salt_dict[user] = [salt]

        # Attempt to crack passwords for users in user_salt_dict
        for user, salts in user_salt_dict.items():
            for salt in salts:
                # Iterate through salts associated with user

                with open(self.passwd_file_path) as file:
                    # Iterate through passwords from PwnedPWs100k

                    for row in file:
                        passwd = row.strip()

                        candidate_passwds = [passwd + str(i) for i in range(10)]

                        for candidate_passwd in candidate_passwds:
                            salted_passwd = salt + candidate_passwd

                            # Hash current password
                            h = hashlib.sha256()
                            h.update(bytes(salted_passwd, "utf-8"))
                            hash_candidate = h.hexdigest()

                            self.log_crack_attempts(user, passwd)  
                            
                            if hash_candidate in salted_hash_set:
                                if self.attempt_crack(user, candidate_passwd):
                                    cracked_dict[user] = candidate_passwd
                                
        # Write cracked gang member's credentials to file
        with open("/home/cse/Lab1/Solutions/Q6_Cracked_Gang_Members", "w") as file:
            for user, passwd in cracked_dict.items():
                file.write(f"{user}, {passwd}\n")   
