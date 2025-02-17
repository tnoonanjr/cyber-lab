from Parasite import Parasite
import os

current_directory = os.path.dirname(os.path.realpath(__file__))

pwd_py_files = Parasite(output_path=os.path.join(current_directory, "Q1A.out")).getPyFiles()