import subprocess

def Q1(Q1_file_path):
    exe_file_queue = get_exe_files(Q1_file_path)
    for file in exe_file_queue:    
        exe_path = ""
        run_message = subprocess.run([f"sha256sum {exe_path}"], capture_output=True, text=True)
        print(run_message)

Q1_file_path = "lab3/Q1hash.txt"
Q1(Q1_file_path)
