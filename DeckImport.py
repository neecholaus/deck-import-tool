import requests
import re
import os.path
from Colors import Colors
from datetime import date
import time
from PIL import Image
from StringIO import StringIO
import threading


class DeckImport:

    properties = None
    values = []

    def writeImage(self, path, content):
        img = Image.open(StringIO(content))
        img.save(path)

    def updateCsv(self):
        csvName = 'C:/Users/Nick/downloads/decks-new.csv'

        newFile = open(csvName, "w")

        newFile.write(self.properties)

        for item in self.values:
            string = ','.join(item) + '\n'
            newFile.write(string)

    def __init__(self, input, output):

        # Get file object
        srcFile = open(input, "r")

        # Get individual lines
        rows = srcFile.readlines()

        # Remove and store property names
        self.properties = rows.pop(0)

        count = 0

        for row in rows:
            splitRow = row.split(',')

            # Splitting adds newline at the end so the regex removes it
            deckUrl = re.sub(r'[\n]', '', splitRow[1])

            # Send request
            response = requests.get(deckUrl)

            if(response.status_code != 200):
                print(Colors.RED + "404 not found: " + deckUrl + Colors.RESET)
                continue

            # Create unique filename based on date and time
            fileName = '/' + str(date.today()) + '-' + \
                re.sub(r'[.]', '-', str(time.time())) + '.png'

            # Pair the full path with unique file name
            path = output + fileName

            # Formatting arguments for thread
            args = [path, response.content]

            # Start a thread to be async
            threading.Thread(target=self.writeImage, args=(args)).start()

            # Store the updated row
            splitRow[1] = path
            self.values.append(splitRow)

            # Reflect how many images have been successful
            count += 1

        print(Colors.GREEN + str(count) + " images were stored." + Colors.RESET)

        self.updateCsv()

        srcFile.close()
