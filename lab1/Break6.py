from SkeletonKey import SkeletonKey
from time import time
from datetime import datetime

start_float = time()
start_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
key = SkeletonKey(passwd_file_path = "/home/cse/Lab1/Q6/PwnedPWs100k",
                  hash_file_path = "/home/cse/Lab1/Q6/SaltedPWs",
                  user_file_path = "/home/cse/Lab1/Q6/gang",
                  login_file_path = "/home/cse/Lab1/Q6/Login.pyc",
                  print_interval = 1000000)

# Crack password
key.crack_pass_hash_salt()

end_float = time()
end_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
elapsed = end_float - start_float

print(f"Start time: [{start_str}] \nEnd time: [{end_str}] \nElapsed time: {round(elapsed, 2)} sec")
