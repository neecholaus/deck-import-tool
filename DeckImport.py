import requests
import re
import os.path
from Colors import Colors
from datetime import date
import time

class DeckImport:

    def writeImage(self, path, content):        
        img = open(path, "w")
        
        img.write(content)


    def __init__(self, input, output):

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
        
            # Send request
            response = requests.get(deckUrl)

            # Create unique filename based on date and time
            fileName = '/' + str(date.today()) + '-' + re.sub(r'[.]', '-', str(time.time())) + '.png'

            path = output + fileName

            self.writeImage(path, response.content)     

        srcFile.close()

