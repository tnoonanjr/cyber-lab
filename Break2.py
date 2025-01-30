from SkeletonKey import SkeletonKey
from time import time

test_param = ["/home/cse/Lab1/Q2/MostCommonPWs",   # passwd path
              "/home/cse/Lab1/Q2/gang",            # user path
              "/home/cse/Lab1/Q2/Login.pyc"        # exe path
            ]
key = SkeletonKey(passwd_file_path = test_param[0],
                  user_file_path = test_param[1],
                  exe_path = test_param[2])

start = time()
key.crack_pass_bruteforce()
end = time()

print(f"""Start: {start}
End: {end}
Elapsed: {end-start}""")