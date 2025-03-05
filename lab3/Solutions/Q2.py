from Crypto.Hash import SHA256
import subprocess

def find_hash():
    
    output = subprocess.run(["ls", "../Q2files"], capture_output=True, text=True).stdout.strip("\n")
    
    files = output.split()
    
    with open("../Q2hash.txt", "rb") as f:
        bin_text = f.read()
        
    with open("../Q2hash.txt", "r") as g:
        base_text = g.read()
        
    Q2_h = SHA256.new(bin_text)
    Q2_hash = Q2_h.hexdigest()
    print(base_text)
    print(Q2_hash)
    
    for file in files:
        bin_file = file.encode()
        h = SHA256.new(bin_file)
        hashed_file = h.hexdigest()
        print(hashed_file)
        
        if Q2_hash == hashed_file:
            print("Done!")
    print("Completed")
    
if __name__ == "__main__":
    find_hash()
