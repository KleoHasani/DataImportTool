import sys
import os.path as path

# CLI Allowed commands.
CSV_COMMAND = ("-c", "--csv")
XLSX_COMMAND = ("-x", "--xlsx")

def cli():
    # Vars
    args = sys.argv[1:]
    arg_length = len(args)
    cmd = None
    cwp = ""

    try:
        # Check correct number of arguments is being passed.
        if arg_length == 0:
            raise Exception("No arguments supplied.")

        if arg_length == 1:
            raise Exception("No path argument supplied.")

        if arg_length > 3:
            raise Exception("Too many arguments supplied.")

        # Check command is valid.
        if args[0] == CSV_COMMAND[0] or args[0] == CSV_COMMAND[1]:
            cmd = "csv"
        elif args[0] == XLSX_COMMAND[0] or args[0] == XLSX_COMMAND[1]:
            cmd = "xlsx"
        else:
            raise Exception("Invalid command supplied.")

        # Set path.
        cwp = args[1]
        # Resolve path.
        cwp = path.abspath(cwp)
        print(cwp)


        # Check path is valid.
        if not path.exists(cwp):
            raise Exception("Invalid path.")

    except Exception as e:
        print(e)
        return sys.exit(0)

    # Return tuple with command and current working path.
    return (cmd, cwp)