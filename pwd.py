# not meant to be run

import os

def main():
    current_working_directory = os.getcwd()
    with open('../config/working.directory', 'w') as file:
        file.write(current_working_directory)

if __name__ == "__main__":
    main()
