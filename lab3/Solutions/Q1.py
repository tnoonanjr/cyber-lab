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

def bruteforce_find_checksum_match(Q1_file_path):
    exe_file_queue = get_exe_files(Q1_file_path)
    for file in exe_file_queue:    
        exe_path = "lab3/Q1files"
        run_message = subprocess.run([f"sha256sum {exe_path}"], capture_output=True, text=True)
        print(run_message)

Q1_file_path = "lab3/Q1hash.txt"
bruteforce_find_checksum_match(Q1_file_path)
