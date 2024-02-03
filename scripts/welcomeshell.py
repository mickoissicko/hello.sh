#!/usr/bin/env python3

import os
import getpass
import subprocess

config_path = '../config/term.toml'
config2_path = '../config/neo.fetch'

try:
    with open(config2_path, 'r') as config_file:
        nfetch_line = config_file.read().strip()
        nfetch_command = nfetch_line.split('==', 1)[1].strip()
except FileNotFoundError:
    nfetch_command = 'neofetch'

def read_term_config():
    try:
        with open(config_path, 'r') as config_file:
            for line in config_file:
                line = line.strip()
                if line.startswith('$TERM =='):
                    return line.split('==', 1)[1].strip()
            return None
    except FileNotFoundError:
        return None

def howdy():
    os.system('clear')

    term_command = read_term_config()

    if term_command:
        subprocess.run(term_command, shell=True)
    else:
        print("No $TERM command specified in term.toml")

    whoami = getpass.getuser()
    terminal_width = os.get_terminal_size().columns

    sup = f"Welcome back, {whoami}!"
    padding = (terminal_width - len(sup)) // 2

    border = "=" * terminal_width

    print(border)
    print(" " * padding + sup)
    print(border)

if __name__ == "__main__":
    howdy()