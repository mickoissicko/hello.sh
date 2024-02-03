#!/usr/bin/env python3

import os
import getpass
import subprocess

def howdy():
    os.system('clear')
    os.system('screenfetch')

    whoami = getpass.getuser()
    terminal_width = os.get_terminal_size().columns

    sup = f"Hello, {whoami}!"
    padding = (terminal_width - len(sup)) // 2

    border = "=" * terminal_width

    print(border)
    print(" " * padding + sup)
    print(border)

if __name__ == "__main__":
    howdy()
