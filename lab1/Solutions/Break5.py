from SkeletonKey import SkeletonKey
from time import time
from datetime import datetime

start_float = time()
start_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

test_param = [
        "/lab1/Q5/HashedPWs",   # passwd path
        "/lab1/Q5/gang",            # user path
        "/lab1/Q5/Login.pyc"        # exe path
    ]
    
key = SkeletonKey(passwd_hashed_path= test_param[0],
                  passwd_pwned_path= test_param[3],
                  user_file_path= test_param[1],
                  exe_path= test_param[2],
                  cracked_users={"SkyRedFalcon914", "MountainPurpleShark585"},
                  print_interval=1000000)

# Crack password
key.crack_pass_hash_brute_force()

end_float = time()
end_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
elapsed = end_float - start_float

print(f"Start time: [{start_str}] \nEnd time: [{end_str}] \nElapsed time: {round(elapsed, 2)} sec")
