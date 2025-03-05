import subprocess
import os

def get_exe_files(path):
    exe_files = []
    directory = os.listdir(path)
    for file in directory:
        file_path = f"{path}/{file}"
        if os.path.isfile(file_path) and file_path.endswith(".exe"):
            exe_files.append(file_path.split("/")[-1])
    return exe_files

def hash_find_checksum_match(Q1_file_path):
    exe_file_queue = get_exe_files(Q1_file_path)
    hash_candidates = dict()

    with open("../Q2hash.txt", "r") as file:
        target_hash = file.read().strip()
    
    for file in exe_file_queue:    
        exe_path = "lab3/Q2files"
        with open(exe_path) as file:
            hash = hashlib.new("sha256")
            hash.update(file.read())
            hash_hex = hash.hexdigest()
            hash_candidates[hash_hex] = exe_path.split("/")[-1]
    
    if target_hash in hash_candidates:
        return hash_candidates[target_hash]

Q2_file_path = "lab3/Q2hash.txt"
hash_find_checksum_match(Q2_file_path)