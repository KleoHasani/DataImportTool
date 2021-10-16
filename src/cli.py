import sys
import os.path as path

# Allowed commands.
ALLOWED_COMMANDS = [("-c", "--csv"), ("-x", "--xlsx")]

def cli():
    # Vars
    args = sys.argv
    cmd = None
    cwp = ""
    
    try:
        # Check for a valid number of arguments passed.
        if args.__len__() == 0 or args.__len__() > ALLOWED_COMMANDS.__len__() + 1:
            raise Exception("No arguments")
                
        # Check arg[1], command is valid.
        if args[1] == ALLOWED_COMMANDS[0][0] or args[1] == ALLOWED_COMMANDS[0][1]:
            cmd = "csv"
        elif args[1] == ALLOWED_COMMANDS[1][0] or args[1] == ALLOWED_COMMANDS[1][1]:
            cmd = "xlsx"
        else:
            raise Exception("Invalid command")
        
        # Check arg[2], path is valid.
        if args[2]:
            cwp = args[2]
        else:
            raise Exception("No path")

    except Exception as e:
        print(e)
        return sys.exit(0)


    # Resolve path.
    cwp = path.abspath(cwp)

    # Return tuple with command and current working path.
    return (cmd, cwp)