import os
import getpass

os.chdir('..')

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
    write_file("config/neo.fetch", fetch_content)

def activate():

    dot_files = input("Enter the path to your shell-DOTFILES: ")

    current_working_directory = os.getcwd()
    with open('config/working.directory', 'w') as file:
        file.write(f'WD={current_working_directory}\n')
        file.write(f'DF={dot_files}\n')

    with open(dot_files, 'a') as file:
        file.write(f'\n# HelloShell Startup Configuration\n')
        file.write(f'clear\n')
        file.write(f'python {current_working_directory}/scripts/welcomeshell.py\n')

def deactivate():
    config_file_path = "config/working.directory"
    with open(config_file_path, 'r') as config_file:
        config_contents = config_file.readlines()
    df_path = None
    for line in config_contents:
        if line.startswith("DF="):
            df_path = line.split('=')[1].strip()
            break
    try:
        with open(df_path, 'r') as target_file:
            file_contents = target_file.read()
        modified_contents = file_contents.split("# HelloShell Startup Configuration")[0].split("python")[0].strip()
        with open(df_path, 'w') as target_file:
            target_file.write(modified_contents)
        print(f"File '{df_path}' edited successfully.")
    except FileNotFoundError:
        print(f"File '{df_path}' not found.")


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
