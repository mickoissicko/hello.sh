
import os

def edit_config(file_path, replacement_text):
    with open(file_path, 'r') as file:
        content = file.read()

    print(f"Before:\n{content}")

    with open(file_path, 'w') as file:
        file.write(replacement_text)

    print(f"After:\n{replacement_text}")

def configure_automatic_start(rc_path):
    with open(rc_path, 'r') as rc_file:
        rc_content = rc_file.read()

    shell_line_start = rc_content.find("$SHELL == ") + len("$SHELL == ")
    shell_line_end = rc_content.find("\n", shell_line_start)

    current_shell_path = rc_content[shell_line_start:shell_line_end].strip()

    print(f"\nCurrent shell path: {current_shell_path}")

    new_script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'scripts', 'welcomeshell.py')

    new_content = f"\n# Added by the configuration script\npython {new_script_path}\n"

    with open(rc_path, 'a') as rc_file:
        rc_file.write(new_content)

    print("\n[4]\nApplied settings!\n")

def main():
    print("[1] Configure *Fetch command")
    fetch_path = input("Enter the path for Fetch command: ")
    fetch_content = f"# Startup command. Default is ScreenFetch -- you may change this.\n\n$NFETCH == {fetch_path}\n"
    edit_config("../config/neo.fetch", fetch_content)

    print("\n[2] Configure DOTFILE path")
    rc_path = input("Enter the path to your RC/Prompt configuration file: ")
    rc_content = f"# Default presets\n# You can add a custom path\n\n&STARSHIP == ~/.config/starship.toml\n&FISH == ~/.config/fish/config.fish\n&BASH == ~/.bashrc\n&ZSH == {rc_path}\n\n# The below line determines the path. Default is ~/.bashrc.\n$SHELL == {rc_path}\n"
    edit_config("../config/rc.toml", rc_content)

    print("\n[3] Configure Terminal emulator")
    term_emulator = input("Enter preferred terminal emulator: ")
    term_content = f"# The default terminal will be Konsole. You can change this.\n\n$TERM == {term_emulator}\n"
    edit_config("../config/term.toml", term_content)

    while True:
        print("\n[4] Configure automatic start")
        print("[X] Quit")
        option = input("Enter your choice (4 to configure automatic start, X to quit): ").upper()

        if option == 'X':
            print("\n[X] Quits the program.")
            break
        elif option == '4':
            configure_automatic_start(rc_path)
        else:
            print("\nInvalid option. Please enter 4 to configure automatic start or X to quit.")

if __name__ == "__main__":
    main()
