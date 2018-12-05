import sys
from DeckImport import DeckImport

# ANSI color codes
RED = '\033[1;31;40m'
GREEN = "\033[1;31;32m"
RESET = '\033[0m'

args = sys.argv

# Where to find the current csv
input = None

# Where the new file will be (optional)
output = None

# Handle lack of input
if(len(args) < 2):
    print(GREEN + "Invalid number of arguments." + RESET)
    exit()

input = args[1]

# Choose whether current file will be updated
# or new file will be generated with updated paths
if(len(args) > 2):
    print(GREEN + "Creating new file for updated paths." + RESET)
    output = args[2]
else:
    print(GREEN + "Updating current file with new values" + RESET)

DeckImport(input, output)