import sys
from DeckImport import DeckImport

# ANSI color codes
RED = "\033[1;31;40m"
GREEN = "\033[1;31;32m"
RESET = "\033[0m"

args = sys.argv

# Where to find the current csv
input = None

# Where the new file will be (optional)
output = None

# Handle lack of input
if(len(args) < 3):
    print(RED + "Invalid number of arguments." + RESET)
    exit()

input = args[1]

output = args[2]

DeckImport(input, output)