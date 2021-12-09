from os.path import join
from pathlib import Path as gPath

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

ascii_done = '''
_____________________
|                   |
|   * * Done * *    |
|___________________|
'''

DEFAULT_CONFIG_PATH = join(gPath.home(), "dit.conf")
DEFAULT_KEY_PATH = join(gPath.home(), "dit.key")
