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
    print("\n[1] Fetch command configured successfully.\n")

def configure_dotfile_path():
    rc_path = input("Enter the path to your RC/Prompt configuration file: ")
    term_emulator = input("Enter preferred terminal emulator: ")

    rc_content = f"# Default presets\n# You can add a custom path\n\n&STARSHIP == ~/.config/starship.toml\n&FISH == ~/.config/fish/config.fish\n&BASH == ~/.bashrc\n&ZSH == {rc_path}\n\n# The below line determines the path. Default is ~/.bashrc.\n$SHELL == {rc_path}\n"
    term_content = f"# The default terminal will be Konsole. You can change this.\n\n$TERM == {term_emulator}\n"

    write_file("../config/rc.toml", rc_content)
    write_file("../config/term.toml", term_content)

    print("\n[2] DOTFILE path and Terminal emulator configured successfully.\n")

def configure_automatic_start(rc_path):
    rc_content = read_file(rc_path)

    shell_line_start = rc_content.find("$SHELL == ") + len("$SHELL == ")
    shell_line_end = rc_content.find("\n", shell_line_start)

    current_shell_path = rc_content[shell_line_start:shell_line_end].strip()

    print(f"\nCurrent shell path: {current_shell_path}")

    new_script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'scripts', 'welcomeshell.py')

    new_content = f"\n# Added by the configuration script\npython {new_script_path}\n"

    with open(rc_path, 'a') as rc_file:
        rc_file.write(new_content)

    print("\n[3] Automatic start configured successfully.\n")

def main():
    while True:
        print("\nMenu:")
        print("[1] Configure *Fetch command")
        print("[2] DOTFILE path and Terminal emulator")
        print("[3] Configure Automatic start")
        print("[X] Quit")

        option = input("Enter your choice: ").upper()

        if option == 'X':
            print("\n[X] Quits the program.")
            break
        elif option == '1':
            configure_fetch_command()
        elif option == '2':
            configure_dotfile_path()
        elif option == '3':
            rc_path = input("Write the path once again (for verification) ")
            configure_automatic_start(rc_path)
        else:
            print("\nInvalid option. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
