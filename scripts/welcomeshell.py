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
    script_dir = os.path.dirname(os.path.realpath(__file__))
    splashtext_file = os.path.join(script_dir, "..", "text", "splash.text")

    try:
        with open(splashtext_file, 'r') as file:
            phrases = file.readlines()

        random_phrase = random.choice(phrases)
    except FileNotFoundError:
        print(f"Error: File '{splashtext_file}' not found.")
        return

    except Exception:
        exit

    terminal_width = os.get_terminal_size().columns

    printmotd = f"{random_phrase.strip()}"
    padding = (terminal_width - len(printmotd)) // 2

    border = "=" * terminal_width

    print(border)
    print(" " * padding + printmotd)
    print(border)

def main():
    howdy()

    script_dir = os.path.dirname(os.path.realpath(__file__))
    nfetchpath = os.path.join(script_dir, "..", "config", "neo.fetch")

    try:
        with open(nfetchpath, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith("$NFETCH =="):
                startup_command = line.split("==")[1].strip()
                break
    except FileNotFoundError:
        startup_command = "echo Couldn't find neo.fetch."

    subprocess.run(startup_command, shell=True)

    splash()
if __name__ == "__main__":
    main()