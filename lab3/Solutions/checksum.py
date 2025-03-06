import hashlib
import os
import subprocess

class Operations:
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
    hash_candidates[str(hash_hex)] = exe_file
  

# Naive approach:
###########################################
##############      Q1       ##############
###########################################
def bruteforce_find_checksum_match(Q1_file_path):
  exe_file_queue = self.get_exe_files(Q1_file_path)
  for file in exe_file_queue:    
      exe_path = "lab3/Q1files"
      run_message = subprocess.run([f"sha256sum {exe_path}"], capture_output=True, text=True)
      print(run_message)



class Checksum:
  ###########################################
  ##############      Q2       ##############
  ###########################################
  def hash_find_checksum_match(Q2_file_path, hash_path):
    exe_file_queue = get_exe_files(Q2_file_path)
    hash_candidates = dict()

    with open(hash_path, "r") as file:
        target_hash = file.read().strip()
    
    for exe_file in exe_file_queue:  
        Operations.hash_binary(f"{path}/{exe_file}")
    
    if target_hash in hash_candidates:
        return hash_candidates[target_hash]
      
