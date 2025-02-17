import os
pwd_directory_list = os.listdir()

for filename in pwd_directory_list:
  name, extension = filename.split(".")
  if extension == "py":
    with open("Q1A.out", "a") as file:
      file.write(f"{name}.py\n")
        
