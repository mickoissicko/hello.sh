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
    os.system('python ../pwd.py')

    with open('../config/working.directory', 'r') as wd_file:
        working_directory = wd_file.read().strip()

    dotfile_path = input("Enter the path to your shell-DOTFILE: ")

    username = getpass.getuser()
    dotfile_path = dotfile_path.replace('~', f'/home/{username}')

    rc_toml_path = '../config/rc.toml'

    with open(rc_toml_path, 'r') as file:
        contents = file.read()

    contents = contents.replace('$SHELL ==', f'$SHELL == "{dotfile_path}"')

    with open(rc_toml_path, 'w') as file:
        file.write(contents)

    with open(dotfile_path, 'a') as dotfile:
        dotfile.write(f'\n# HELLOSHELL CONFIGURATION\npython {working_directory}/scripts/welcomeshell.py')

def deactivate():
    rc_toml_path = '../config/rc.toml'

    with open(rc_toml_path, 'r') as file:
        contents = file.read()

    contents = contents.replace('$SHELL ==', '$SHELL == ~/.bashrc')

    with open(rc_toml_path, 'w') as file:
        file.write(contents)

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
