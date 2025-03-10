from SkeletonKey import SkeletonKey
from time import time
from datetime import datetime

start_float = time()
start_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

params = ["/lab1/Q1/MostCommonPWs",   # passwd path
          "SkyRedFalcon914",                   # users
          "/lab1/Q1/Login.pyc"        # exe path
        ]
key = SkeletonKey(passwd_pwned_path = params[0],
                  users = params[1],
                  exe_path = params[2])

# Crack password
key.crack_pass_bruteforce(max_cracked=1)

end_float = time()
end_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
elapsed = end_float - start_float

print(f"Start time: [{start_str}] \nEnd time: [{end_str}] \nElapsed time: {round(elapsed, 2)} sec")
