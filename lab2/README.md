# Lab 2 - Malware

## Question 1 - Virus

### Q1A.py
Reads files in pwd, and writes them to file Q1A.out

### Q1B.py
- python3 Q1B.py [target_file]  

Takes in a parameter target_file that we inject code from Q2_payload.py into. Only runs if the file is a python file (checks for 'if \_\_name\_\_ == "\_\_main\_\_":' line) and the file has not already been infected. When injected, the target file will write to Q2B.out the command line when a user executes the file.

### Q1C.py
Infects every py file in current working directory (cwd), injecting them with the same functionality as Q1B. 

Video demo:


https://github.com/user-attachments/assets/0713936e-3e8b-4465-9d9c-54f3a3d803f8



## Question 2 - Worm

### Q2_worm.py

### find_vulnerable_machines():
Checks ips in the subnet for open telnet or ssh ports and outputs them to their respective file.

### find_vulnerable_users():
Checks users against vulnerable passwords in Q2pwd for telnet and ssh accounts in ips found using the previous method.

### extract_and_infect():
Enters exposed accounts and injects the virus.

Video demo:


https://github.com/user-attachments/assets/6a173ec8-991f-45ca-ae79-09ae724f6505



## Questions 3-5 - DuckyScript

### Question 3 - Echo using batch script
Scripts keystrokes using DuckyScript to write, save, and execute a batch file that simply echos our names in the terminal.

Video demo:


https://github.com/user-attachments/assets/4716e041-398a-4b57-970c-7703a37fc8da



### Question 4 - hello_world.py
Scripts keystrokes using DuckyScript to write, save, and execute a python hello world file.

Video demo:


https://github.com/user-attachments/assets/686119dc-831c-438f-b4c4-ac74735fdb52



### Question 5 - Q1C.py
Scripts keystrokes using DuckyScript to write, save, and execute the same functionality of Q1C.py.

Video demo:


https://github.com/user-attachments/assets/42043d79-c3cf-4ef7-8aa9-517fac1cb2d4



