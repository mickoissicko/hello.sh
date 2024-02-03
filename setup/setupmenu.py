# HOLY SHIT NO IMPORTS???

def edit_config(file_path, replacement_text):
    with open(file_path, 'r') as file:
        content = file.read()

    print(f"Before:\n{content}")

    with open(file_path, 'w') as file:
        file.write(replacement_text)

    print(f"After:\n{replacement_text}")


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


if __name__ == "__main__":
    main()