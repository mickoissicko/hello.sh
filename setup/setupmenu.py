import os

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

def configure_dotfile_path():
    dotpath = input("Enter the path to your shell-DOTFILE: ")

    with open('../config/rc.toml', 'r') as file:
        contents = file.read()

    contents = contents.replace('$SHELL == ~/.bashrc', f'$SHELL == {dotpath}')

    with open('../config/rc.toml', 'w') as file:
        file.write(contents)

    current_path = os.getcwd()
    final_path = os.path.join(current_path, 'scripts', 'welcomeshell.py')

    dotpath_without_setup = os.path.join(os.path.dirname(dotpath), os.path.basename(dotpath).replace('setup', ''))
    
    with open(dotpath_without_setup, 'a') as file:
        file.write(f'# ADDED BY HELLOSHELL DO NOT ADD ANYTHING UNDER IT\npython {final_path}\n')

def main():
    while True:
        print("\nMenu:")
        print("[1] Configure *Fetch command")
        print("[2] Configure DOTFILE path")
        print("[X] Quit")

        option = input("Enter your choice: ").upper()

        if option == 'X':
            print("\n[X] Quits the program.")
            break
        elif option == '1':
            configure_fetch_command()
        elif option == '2':
            configure_dotfile_path()
        else:
            print("\nInvalid option. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
