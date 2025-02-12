import os

output_path = "Q1A.out"
pwd_directory_list = os.listdir()

for filename in pwd_directory_list:
  name, extension = filename.split(".")
  if extension == "py":
    with open(output_path, "a") as file:
      file.write(f"{name}.py\n")
        
