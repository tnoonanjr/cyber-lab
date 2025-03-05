from Crypto.Hash import SHA256
import subprocess

def find_hash():
    
    output = subprocess.run(["ls", "../Q2files"], capture_output=True, text=True).stdout.strip("\n")
    
    files = output.split()
        
    with open("../Q2hash.txt", "r") as g:
        base_text = g.read()
        
    print(base_text)
    
    for file in files:
        with open("../Q2files/" + file, "rb") as bt:
            
            bin_file = bt.read()
        
        h = SHA256.new(bin_file)
        hashed_file = h.hexdigest()
        print(hashed_file)
        
        if base_text == hashed_file:
            print("Found!")
            break
    
if __name__ == "__main__":
    find_hash()
