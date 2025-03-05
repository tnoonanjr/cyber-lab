from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import subprocess

def get_exe_files(path):
    exe_files = []
    directory = os.listdir(path)
    for file in directory:
        file_path = f"{path}/{file}"
        if os.path.isfile(file_path) and file_path.endswith(".exe"):
            exe_files.append(file_path.split("/")[-1])
    return exe_files

def verify_sign(Q3_sign_path):
    with open(Q3_sign_path, "r") as file:
        file.read().split("-----")[-2]
    exe_file_queue = get_exe_files(Q3_exe_dir_path)
    for exe_file in exe_file_queue:
        


Q3_exe_dir_path = "../../lab3/Q3files"

scan = verify_sign()