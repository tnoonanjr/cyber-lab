import hashlib
import os
import subprocess

class Operations:
    '''
    '''
    def get_exe_files(path):
            exe_files = []
            directory = os.listdir(path)
            for file in directory:
                file_path = f"{path}/{file}"
                if os.path.isfile(file_path) and file_path.endswith(".exe"):
                    exe_files.append(file_path.split("/")[-1])
            return exe_files

    def hash_binary(path):
        with open(path, "rb") as file:
            binary_file = file.read()

        hash = hashlib.new("sha256")
        hash.update(binary_file)
        hash_hex = hash.hexdigest()
        return hash_hex
  

# Naive approach:
###########################################
##############      Q1       ##############
###########################################

def bruteforce_find_checksum_match(candidate_path):
    exe_file_queue = Operations.get_exe_files(candidate_path)
    with open("../../lab3/Q1hash.txt", "r") as file:
        target_hash = file.read().strip()
    for exe_file in exe_file_queue:
        run_message = subprocess.run([f"sha256sum {candidate_path}/{exe_file}"], shell=True, capture_output=True, text=True)
        sha256sum = str(run_message.stdout)[0:64]
    
        if sha256sum == target_hash:
            return f"Scan found match for hash: {sha256sum}.\n{exe_file}\n"
    return f"Scan did not find a match."



class Checksum:
    ''' 
    '''
    def __init__(self):
        pass
    ###########################################
    ##############      Q2       ##############
    ###########################################
    def hash_compare(candidate_path, target_path):
        exe_file_queue = Operations.get_exe_files(candidate_path)
        hash_candidates = dict()

        with open(target_path, "r") as file:
            target_hash = file.read().strip()
        
        for exe_file in exe_file_queue:  
            

            hash_hex = Operations.hash_binary(f"{candidate_path}/{exe_file}")
            hash_candidates[str(hash_hex)] = exe_file
        
        
        if target_hash in hash_candidates:
            return f"Scan found match for hash: {hash_candidates[target_hash]}"
        else:
            return f"Scan did not find a match."
    
    def Q3():
    
        files = []

        key = RSA.import_key(open('../../Q3pk.pem').read())
        print(key)
        
        output = subprocess.run(["ls", "../Q3files"], capture_output=True, text=True).stdout.strip("\n")
        get_files = output.split()
        for file in get_files:
            b = file.split(".")
            if "sign" not in b:
                files.append(file)
        
        
        
        for file in files:
            with open(f"../../Q3files/{file}.sign", "rb") as fb:
                signature = fb.read()
            
            with open(f"../Q3files/{file}", "rb") as gb:
                bin_text = gb.read()
            
            h = SHA256.new(bin_text)
            
            try:
                pkcs1_15.new(key).verify(h, signature)
                print("The signature is valid.")
                print(f"File: {file}")
                break
            except:
                print("The signature is not valid.")

if __name__ == '__main__':
    # 0: all
    # 1: Q1
    # 2: Q2
    # 3: Q3
    # 4: Q4
    protocol = int(input(f"Enter test protocol:\n"))
    scan = Checksum()
    if protocol == 1 or protocol == 0:
        candidate_path = "../../lab3/Q1files"
        scan = bruteforce_find_checksum_match(candidate_path)
        print(scan)
    
    if protocol == 2 or protocol == 0:
        candidate_path = "../../lab3/Q2files"
        target_path = "../../lab3/Q2hash.txt"
        scan = Checksum.hash_compare(candidate_path, target_path)
        print(scan)

    if protocol == 3 or protocol == 0:
        Checksum.Q3()



