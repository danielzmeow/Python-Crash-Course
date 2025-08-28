#!/usr/bin/env python3
"""
Simple tool: read user input in a loop, append '.__doc__', and print the docstring.
"""

# No unused imports

while True:
    try:
        name = input('Enter object (e.g., len or module.func, or "exit" to quit): ')
    except EOFError:
        print()  # newline on Ctrl-D
        break
    if name.strip().lower() in ('exit', 'quit', 'q'):
        break
    try:
        # Form the doc access expression and evaluate it
        doc = eval(f"{name}.__doc__")
        print(doc)
    except Exception as e:
        print(f"Error accessing doc for {name}: {e}")
    # continue looping
    print()
