# Lab 2 - Malware

## Question 1 - Virus

### Q1A.py
Reads files in pwd, and writes them to file Q1A.out

### Q1B.py
- python3 Q1B.py [target_file]  

Takes in a parameter target_file that we inject code from Q2_payload.py into. Only runs if the file is a python file (checks for 'if \_\_name\_\_ == "\_\_main\_\_":' line) and the file has not already been infected. When injected, the target file will write to Q2B.out the command line when a user executes the file.

### Q1C.py
Infects every py file in current working directory (cwd), injecting them with the same functionality as Q1B. 

## Question 2 - Worm

### Q2_worm.py
