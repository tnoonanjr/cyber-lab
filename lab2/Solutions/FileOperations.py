class FileOperations:
    def clear(file):
        with open(file, "w") as file:
            file.write("")
    
    def write_to(file, data):
        with open(file, "w") as file:
            file.write(data)

    def append_to(file, data):
        with open(file, "a") as file:
            file.write(data)
    
    def read(file):
        with open(file, "r") as file:
            return file.read()
    