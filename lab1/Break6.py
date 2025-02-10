from SkeletonKey import SkeletonKey
from time import time
from datetime import datetime

start_float = time()
start_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

test_param = [
        "/home/cse/Lab1/Q6/SaltedPWs",   # passwd path
        "/home/cse/Lab1/Q6/gang",            # user path
        "/home/cse/Lab1/Q6/Login.pyc"        # exe path
    ]
    
key = SkeletonKey(passwd_hashed_path= params[0],
                  passwd_pwned_path= params[1],
                  user_file_path= params[2],
                  exe_path= params[3],
                  to_file_path= params[4],
                  print_interval= 500000)

# Crack password
key.crack_pass_hash_salt()

end_float = time()
end_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
elapsed = end_float - start_float

print(f"Start time: [{start_str}] \nEnd time: [{end_str}] \nElapsed time: {round(elapsed, 2)} sec")
