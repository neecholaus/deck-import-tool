import sys
import os.path
from DeckImport import DeckImport
from Colors import Colors

args = sys.argv

# Where to find the current csv
input = None

# Where the new file will be (optional)
output = None

# Handle lack of input
if(len(args) < 3):
    print(Colors.RED + "Invalid number of arguments." + Colors.RESET)
    exit()

input = args[1]

output = args[2]

# Verify csv exists
srcExists = os.path.isfile(input)

# Handle non existent csv
if(not srcExists):
    print(Colors.RED + "CSV could not be found." + Colors.RESET)
    print("Path: " + input + "")
    exit()

# Verify output dir exists
dirExists = os.path.isdir(output)

# Handle non existent output dir
if(not dirExists):
    print(Colors.RED + "Output directory could not be found." + Colors.RESET)
    print("Path: " + output + "")
    exit()

DeckImport(input, output)