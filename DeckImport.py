import requests
import re
import os.path
from Colors import Colors
from datetime import date
import time


class DeckImport:

    properties = None
    values = []

    def writeImage(self, path, content):
        img = open(path, "w")

        img.write(content)

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

            orderNum = splitRow[0]

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

            path = output + fileName

            self.writeImage(path, response.content)

            splitRow[1] = path

            self.values.append(splitRow)

            count += 1

        print(Colors.GREEN + str(count) + " images were stored." + Colors.RESET)

        self.updateCsv()

        srcFile.close()
