# Lab 2 - Malware

## Q1A.py
Reads files in pwd, and writes them to file Q1A.out

## Q1B.py
- python3 Q1B.py [target_file]
Takes in a parameter target_file that we inject code from Q2_payload.py into. Only runs if the file is a python file (checks for 'if __name__ == "__main__":' line) and the file has not already been infected.

## Q1C.py
