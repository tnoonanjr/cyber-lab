from SkeletonKey import SkeletonKey
from time import time                                                                                                                                                                                                                                                                                                            

test_param = ["/home/cse/Lab1/Q3/PwnedPWs100k",   # passwd path
              "/home/cse/Lab1/Q3/gang",            # user path
              "/home/cse/Lab1/Q3/Login.pyc"        # exe path
            ]
key = SkeletonKey(passwd_file_path = test_param[0],
                  user_file_path = test_param[1],
                  exe_path = test_param[2],
                    cracked_users=set(["SkyRedFalcon914", "MontainBlueFalcon157"]))

start = time()
key.crack_pass_bruteforce(max_cracked=1)
end = time()

print(f"""Start: {start}
End: {end}
Elapsed: {end-start}""")
