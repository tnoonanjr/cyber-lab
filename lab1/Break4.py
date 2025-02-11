from SkeletonKey import SkeletonKey
from time import time
from datetime import datetime

start_float = time()
start_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    

key = SkeletonKey(passwd_file_path = "/home/cse/Lab1/Q4/PwnedPWfile",
                  user_file_path = "/home/cse/Lab1/Q4/gang",
                  login_file_path = "/home/cse/Lab1/Q4/Login.pyc",
                  cracked_users = {"SkyRedFalcon914", "MountainPurpleShark585", "StarGreenBear981"},
                  print_interval = 500)

# Crack password
key.crack_pass_leaked_database()

end_float = time()
end_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
elapsed = end_float - start_float

print(f"Start time: [{start_str}] \nEnd time: [{end_str}] \nElapsed time: {round(elapsed, 2)} sec")
