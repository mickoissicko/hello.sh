#!/usr/bin/env python3

import os
import getpass
import subprocess

config_path = '../config/term.toml'
config2_path = '../config/neo.fetch'

try:
    with open(config_path, 'r') as config_file:
        terminal = config_file.read().strip()
except FileNotFoundError:
    terminal = 'konsole'

try:
    with open(config2_path, 'r') as config_file:
        nfetch_line = config_file.read().strip()
        nfetch_command = nfetch_line.split('==', 1)[1].strip()
except FileNotFoundError:
    nfetch_command = 'neofetch'

command = [terminal, '--hold', '-e', 'python3', 'scripts/btop.py'] if not nfetch_command else nfetch_command.split()

def howdy():
    os.system('clear')
    subprocess.run(command, shell=True)

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
