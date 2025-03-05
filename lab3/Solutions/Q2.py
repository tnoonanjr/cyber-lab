import subprocess
import os
import hashlib

def get_exe_files(path):
    exe_files = []
    directory = os.listdir(path)
    for file in directory:
        file_path = f"{path}/{file}"
        if os.path.isfile(file_path) and file_path.endswith(".exe"):
            exe_files.append(file_path.split("/")[-1])
    return exe_files

def hash_find_checksum_match(Q2_file_path):
    exe_file_queue = get_exe_files(Q2_file_path)
    hash_candidates = dict()

    with open("../../lab3/Q2hash.txt", "r") as file:
        target_hash = file.read().strip()
    
    for exe_file in exe_file_queue:  
        with open(f"{Q2_file_path}/{exe_file}", "rb") as file:
            binary_file = file.read()

        hash = hashlib.new("sha256")
        hash.update(binary_file)
        hash_hex = hash.hexdigest()
        hash_candidates[str(hash_hex)] = exe_file
    
    
    if target_hash in hash_candidates:
        return hash_candidates[target_hash]

Q2_file_path = "../../lab3/Q2files"
scan = hash_find_checksum_match(Q2_file_path)
print(scan)