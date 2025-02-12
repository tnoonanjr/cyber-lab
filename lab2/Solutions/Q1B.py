def get_input_and_verify():
    is_python_script = False
    required_statement = "if __name__ == '__main__':"
    code = None

    input_script = input("Enter a python file in pwd:")

    with open(input_script, "r") as file:
        for row in file:
            if row.strip == required_statement:
                is_python_script = True
                break
            # add statement to find if script exists
    
    if not is_python_script:
        print("Could not verify file is python script; no {required_statement} statement")
        return
    

    