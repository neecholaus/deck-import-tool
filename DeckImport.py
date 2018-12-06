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

    def updateCsv(self, path):
        newFile = open(path, "w")

        newFile.write(self.properties)

        for item in self.values:
            string = ','.join(item) + '\n'
            newFile.write(string)

        newFile.close()

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
            try:
                response = requests.get(deckUrl)
            except:
                print(Colors.EX + " 400 Bad Request: " + deckUrl)
                continue

            if(response.status_code != 200):
                print(Colors.EX + " 404 Not Found: " + deckUrl)
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

        responseColor = Colors.CHECK if count > 0 else Colors.EX

        print(responseColor + " Storing " + str(count) + " images.")

        # Update input CSV with local file paths
        self.updateCsv(input)
        srcFile.close()

        print(Colors.GREEN + u'\u2713' + Colors.RESET + " CSV file paths have been updated.")

        print(Colors.WARNING + " Finishing up...")