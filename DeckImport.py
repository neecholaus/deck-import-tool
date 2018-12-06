import requests
import re
import os.path

class DeckImport:
    def __init__(self, input, output):

        # Verify csv exists
        srcExists = os.path.isfile(input)

        # Handle non existent csv
        if(not srcExists):
            print("CSV could not be found.")
            print("Path: " + input + "")
            exit()

        # Verify output dir exists
        dirExists = os.path.isdir(output)

        # Handle non existent output dir
        if(not dirExists):
            print("Output directory could not be found.")
            print("Path: " + output + "")
            exit()


        # Get file object
        srcFile = open(input, "r")

        # Get individual lines
        rows = srcFile.readlines()


        # Remove and store property names
        properties = rows.pop(0)

        for row in rows:
            splitRow = row.split(',')

            orderNum = splitRow[0]

            # Splitting adds newline at the end so the regex removes it
            deckUrl = re.sub(r'[\n]', '', splitRow[1])
        
            response = requests.get(deckUrl)

            print(response)

            # Save image to output path
            newPath = output + '/' + orderNum + '.png'

            newImg = open(newPath, "w")

            newImg.write(response.content)

        srcFile.close()

