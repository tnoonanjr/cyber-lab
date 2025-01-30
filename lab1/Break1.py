from SkeletonKey import SkeletonKey
from time import time

params = ["/home/cse/Lab1/Q1/MostCommonPWs",   # passwd path
          "SkyRedFalcon914",                   # users
          "/home/cse/Lab1/Q1/Login.pyc"        # exe path
        ]
key = SkeletonKey(passwd_file_path = params[0],
                  users = params[1],
                  exe_path = params[2])

start = time()
key.crack_pass_bruteforce()
end = time()

print(f"""Start: {start}
End: {end}
Elapsed: {end-start}""")

# expected correct: 1234567890
