def write_file(file_name, file_content):
    # Ensuring file_name is a string and adding the .txt extension to the file name
    file_name = str(file_name) + ".txt"
    
    # Opening the file in write mode
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    
    file_name = str(file_name) + ".txt"

    # opening file in append mode
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    
    file_name = str(file_name) + ".txt"

    # opening file n read mode
    with open(file_name, 'r') as file:
        content = file.read()

    return content


# Example usage:
write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

log_content = read_file(file_name="logfile")
print(log_content)
