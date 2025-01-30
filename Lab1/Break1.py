import subprocess
import time


start = time.time()
file = "../Q1/MostCommonPWs"

with open(file, "r") as file:
   for row in file:
        print(row)
        subprocess.run(["python3", "../Q1/Login.pyc", "SkyRedFalcon914", row.strip()])
        
end = time.time()

print(f"Start: {start} End: {end} Elapsed: {end-start}")
