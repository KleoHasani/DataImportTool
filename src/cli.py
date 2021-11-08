import sys
import os.path as path

# CLI Allowed commands.

def cli():
    # Vars
    args = sys.argv[1:]
    arg_length = len(args)
    cmd = None
    cwp = ""
    mck = ""

    # Check correct number of arguments is being passed.
    # Raise error for 'main.py' to handle.
    if arg_length == 0:
        raise Exception("No arguments supplied.")

    if arg_length == 1:
        raise Exception("No data file path argument supplied.")

    if arg_length == 2:
        raise Exception("No mock file path argument supplied.")

    if arg_length > 3:
        raise Exception("Too many arguments supplied.")

    # Check command is valid.
    if args[0] == "-c":
        cmd = "csv"
    elif args[0] == "-x":
        cmd = "xlsx"
    else:
        raise Exception("Invalid command supplied.")

    # Set current working path.
    cwp = args[1]
    # Resolve path.
    cwp = path.abspath(cwp)

    # Check path is valid.
    if not path.exists(cwp):
        raise Exception("Invalid path.")
    
    # Set mock file path.
    mck = args[2]
    # Resolve path.
    mck = path.abspath(mck)

    # Return tuple with command and current working path.
    return (cmd, cwp, mck)