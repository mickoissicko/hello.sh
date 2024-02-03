#!/usr/bin/env python3

import os
import getpass
import subprocess
import random

def howdy():
    os.system('clear')

    whoami = getpass.getuser()
    terminal_width = os.get_terminal_size().columns

    sup = f"Welcome back, {whoami}!"
    padding = (terminal_width - len(sup)) // 2

    border = "=" * terminal_width

    print(border)
    print(" " * padding + sup)
    print(border)

def splash():
    splashtext_file = "../text/splash.text"
    
    try:
        with open(splashtext_file, 'r') as file:
            phrases = file.readlines()
        
        random_phrase = random.choice(phrases)
    except FileNotFoundError:
        print(f"Error: File '{splashtext_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    terminal_width = os.get_terminal_size().columns

    printmotd = f"{random_phrase.strip()}"
    padding = (terminal_width - len(printmotd)) // 2

    border = "=" * terminal_width

    print(border)
    print(" " * padding + printmotd)
    print(border)

def main():
    howdy()

    try:
        with open('neo.fetch', 'r') as file:
            startup_command = file.read().strip()
    except FileNotFoundError:
        startup_command = "neofetch"
    subprocess.run(startup_command, shell=True)

    splash()

if __name__ == "__main__":
    main()
