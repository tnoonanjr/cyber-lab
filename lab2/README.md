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
https://1drv.ms/v/c/9f5bc74f7c1ff50b/IQT7dmiCa9k3SJ9A9tVPd090AcE4rbXDf-w_tZQmr2zvNCA

## Question 2 - Worm

### Q2_worm.py

### find_vulnerable_machines():
Checks ips in the subnet for open telnet or ssh ports and outputs them to their respective file.

### find_vulnerable_users():
Checks users against vulnerable passwords in Q2pwd for telnet and ssh accounts in ips found using the previous method.

### extract_and_infect():
Enters exposed accounts and injects the virus.

Video demo:
https://1drv.ms/v/c/9f5bc74f7c1ff50b/IQR34IemyaD5RZ6R-Bp1GWiRAd7D7KnnbRDCs4uX10O2COI

## Questions 3-5 - DuckyScript

### Question 3 - Echo using batch script
Scripts keystrokes using DuckyScript to write, save, and execute a batch file that simply echos our names in the terminal.

Video demo:
https://1drv.ms/v/c/9f5bc74f7c1ff50b/IQTc1wDQA5ygTr4h7jjp4deMAdcR-OmTn-_UOiUx4CKZTjs

### Question 4 - hello_world.py
Scripts keystrokes using DuckyScript to write, save, and execute a python hello world file.

Video demo:
https://1drv.ms/v/c/9f5bc74f7c1ff50b/IQQl8usKO7ZsR5otjetHN-3hAVUK_q-sKqCRB0AO63I_kUs

### Question 5 - Q1C.py
Scripts keystrokes using DuckyScript to write, save, and execute the same functionality of Q1C.py.

Video demo:
https://1drv.ms/v/c/9f5bc74f7c1ff50b/IQQBU5ybKskrQbvVu4O33GhwAVJ3RU0fUGEAV5lU44CvBGM
