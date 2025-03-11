import subprocess
import os

def stage():
    remove_queue = ['d.key', 'e.key', 'poe.txt.encrypted', 'EncryptedSharedKey', 'DecryptedSharedKey']
    for file in remove_queue:
        try:
            os.remove(file)   
        except:
            pass

stage()

input("Press enter to run the Encryption")
subprocess.run(["python3", "KG6.py"])
subprocess.run(["python3", "R6.py"])

input("Press enter to run the Decryption")
subprocess.run(["python3", "AD6.py", "EncryptedSharedKey"])
subprocess.run(["python3", "D6.py", "DecryptedSharedKey"])
stage()