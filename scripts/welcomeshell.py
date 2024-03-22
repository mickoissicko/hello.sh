#!/usr/bin/env python3

import os
import getpass
import subprocess
import random

def print_with_border(text):
    terminal_width = os.get_terminal_size().columns
    border = "=" * terminal_width
    padding = (terminal_width - len(text)) // 2
    print(border)
    print(" " * padding + text)
    print(border)

def howdy():
    os.system('clear')
    whoami = getpass.getuser()
    sup = f"Welcome back, {whoami}!"
    print_with_border(sup)

def splash():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    splashtext_file = os.path.join(script_dir, "..", "text", "splash.text")

    try:
        with open(splashtext_file, 'r') as file:
            phrases = file.readlines()

        random_phrase = random.choice(phrases).strip()
        print_with_border(random_phrase)
    except FileNotFoundError:
        print(f"Error: File '{splashtext_file}' not found.")
    except Exception as e:
        print("An error occurred:", e)

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
