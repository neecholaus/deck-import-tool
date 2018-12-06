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
    print(Colors.EX + " Invalid number of arguments.")
    exit()

input = args[1]

output = args[2]

# Verify csv exists
srcExists = os.path.isfile(input)

# Handle non existent csv
if(not srcExists):
    print(Colors.EX + " CSV could not be found.")
    print("Path: " + input + "")
    exit()

# Verify output dir exists
dirExists = os.path.isdir(output)

# Handle non existent output dir
if(not dirExists):
    print(Colors.WARNING + " Output directory could not be found so it will be created.")
    print(Colors.WARNING + " Output Path: " + output)

    # Make output dir
    try:
        os.makedirs(output)
    except:
        print(Colors.EX + "Output directory could not be created.")
        exit()

DeckImport(input, output)


