from os.path import join
from pathlib import Path as gPath

# App logo.
ascii_logo = '''
 ____________________________________________________________________
|                                                                    |
|    ___________              ___________            ___________     |
|   |  _______  \            |_____ _____|          |_____ _____|    |
|   | |        \ |                | |                    | |         |
|   | |        | |                | |                    | |         |
|   | |        | |                | |                    | |         |
|   | |        | |                | |                    | |         |
|   | |        | |                | |                    | |         |
|   | |        | |                | |                    | |         |
|   | |________/ |   _        ____| |____     _          | |         |
|   |___________/   |_|      |___________|   |_|         |_|         |
|                                                                    |
| Data Import Tool                                                   |
|____________________________________________________________________|
        https://github.com/csdcti/DataImportTool    By: CSDCTI Team.
'''

# Done logo.
ascii_done = '''
_____________________
|                   |
|   * * Done * *    |
|___________________|
'''

# Default config path for the app.
DEFAULT_CONFIG_PATH = join(gPath.home(), "dit.json")