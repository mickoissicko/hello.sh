import os
import getpass

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def print_file_content(file_path):
    content = read_file(file_path)
    print(f"Content of {file_path}:\n{content}")

def configure_fetch_command():
    fetch_path = input("Enter the *Fetch command: ")
    fetch_content = f"# Startup command. Default is ScreenFetch -- you may change this.\n\n$NFETCH == {fetch_path}\n"
    write_file("../config/neo.fetch", fetch_content)

def activate():

    dot_files = input("Enter the path to your shell-DOTFILES: ")

    current_working_directory = os.getcwd()
    with open('../config/working.directory', 'w') as file:
        file.write(f'WD={current_working_directory}\n')
        file.write(f'DF={dot_files}\n')

    with open(dot_files, 'a') as file:
        file.write(f'# HelloShell Startup Configuration\n')
        file.write(f'python {current_working_directory}/scripts/welcomeshell.py\n')

def deactivate():
    pass

def main():
    while True:
        print("\nMenu:")
        print("[1] Configure *Fetch command")
        print("[2] Activate")
        print("[3] Deactivate")
        print("[X] Quit")

        option = input("Enter your choice: ").upper()

        if option == 'X':
            print("\n[X] Quits the program.")
            break
        elif option == '1':
            configure_fetch_command()
        elif option == '2':
            activate()
        elif option == '3':
            deactivate()
        else:
            print("\nInvalid option. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
