import sys
import os.path
import requests
import re
from datetime import date
import time
from Arguments import Arguments
from DeckImport import DeckImport
from Colors import Colors
from Tkinter import *
from tkFileDialog import *
from PIL import Image
from StringIO import StringIO
import threading


class Tool:

    """
    Prompt user to select csv input file
    """
    def promptInput(self, event=None):        
        input = askopenfilename(initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        if(Arguments.validateInput(input)):
            self.inputElement.delete(0, END)
            self.inputElement.insert(0, input)
            self.appendToLog("CSV path is valid.")
            self.input = input
        else:
            self.appendToLog("Selected input path is not valid.")


    """
    Prompt user to select a directory for downloaded images
    """
    def promptOutput(self, event=None):
        output = askdirectory()
        if(Arguments.validateOutput(output)):
            self.outputElement.delete(0, END)      
            self.outputElement.insert(0, output)
            self.appendToLog("Output path has been found.")
            self.output = output
        else:
            self.appendToLog("Output path is unavailable.")


    """
    Parse csv, return String[]
    """
    def parseInput(self, path):
        if(not path):
            return []

        # Get file object
        srcFile = open(path, "r")

        # Get individual lines
        rows = srcFile.readlines()

        srcFile.close()

        # Remove and store property names
        self.properties = rows.pop(0)
        
        return rows


    """
    Convert string to image and store in given path
    """
    def writeImage(self, path, content, index):
        img = Image.open(StringIO(content))
        img.save(path)

        self.finishedImages += 1

        if(self.finishedImages >= self.imageCount):
            self.appendToLog("Done.")


    """
    Replace csv with updated local paths
    """
    def updateCsv(self, path):
        newFile = open(path, "w")

        newFile.write(self.properties)

        for item in self.values:
            string = ','.join(item) + '\n'
            newFile.write(string)

        newFile.close()
        self.appendToLog("CSV file paths have been updated.")


    """
    Make request and handle response
    """
    def _request(self, url):
        try:
            response = requests.get(url)
        except:
            self.appendToLog("400 Bad Request: " + url)
            self.imageCount -= 1
            return False
        if(response.status_code != 200):
            self.appendToLog("404 Not Found: " + url)
            self.imageCount -= 1
            return False

        return response.content


    """
    Parse csv, download files, update csv
    """
    def fetch(self):
        rows = self.parseInput(self.input)

        self.imageCount = len(rows)
        Count = 0

        for row in rows:
            Count += 1

            splitRow = row.split(',')

            # Splitting adds newline at the end so the regex removes it
            deckUrl = re.sub(r'[\n]', '', splitRow[1])

            # Send request
            response = self._request(deckUrl)
            if(not response):
                continue

            # Tell user if successful and show order number
            self.appendToLog("File found: " + splitRow[0])

            # Create unique filename based on date and time
            fileName = '/' + str(date.today()) + '-' + re.sub(r'[.]', '-', str(time.time())) + '.png'

            # Pair the full path with unique file name
            path = self.output + fileName

            # Formatting arguments for thread
            args = [path, response, Count]

            # Start a thread to be async
            threading.Thread(target=self.writeImage, args=(args)).start()

            # Store the updated row
            splitRow[1] = path
            self.values.append(splitRow)

        self.appendToLog("Storing " + str(Count) + " images.")

        # Update input CSV with local file paths
        self.updateCsv(self.input)

        self.appendToLog("Parsing images...")


    """
    Enter text to be displayed in the log
    """
    def appendToLog(self, string):
        self.logText.insert(END, string + "\n\n")
        self.window.update()
        self.logText.see("end")


    """
    Constructor
    """
    def __init__(self):
        # Incoming data
        self.input = None
        self.output = None

        # Updated CSV
        self.properties = None
        self.values = []

        # Needed in order to determine when last photo was finished
        self.imageCount = 0
        self.finishedImages = 0

        # Create canvas
        self.window = Tk()

        # Set window icon
        self.window.iconbitmap(r'favicon.ico')
 
        # Main window configuration
        self.window.title("Custom Deck Importer")
        self.window.resizable(False, False)

        # Header
        self.header = Label(self.window, text="Custom Deck Importer", font=("Helvetica 15 bold"))
        self.header.pack(pady=(20, 30))

        # Input
        self.inputFrame = Frame(self.window)
        self.inputLabel = Label(self.inputFrame, text="CSV Path:", width=12, anchor="e", font=("Helvetica 12"))
        self.inputBtn = Button(self.inputFrame, text="Find", command=self.promptInput)
        self.inputElement = Entry(self.inputFrame, width=50)

        # Input Pack
        self.inputFrame.pack(fill=X)
        self.inputLabel.pack(side=LEFT, padx=(50, 0), pady=5)
        self.inputBtn.pack(side=RIGHT, padx=(5, 30))
        self.inputElement.pack(side=RIGHT, padx=(20, 0), pady=5)
        self.inputElement.bind("<Button-1>", self.promptInput)

        # Output
        self.outputFrame = Frame(self.window)
        self.outputLabel = Label(self.outputFrame, text="Image Destination:", width=15, anchor="e", font=("Helvetica 12"))
        self.outputBtn = Button(self.outputFrame, text="Find", command=self.promptOutput)
        self.outputElement = Entry(self.outputFrame, width=50)

        # Output Pack
        self.outputFrame.pack(fill=X)
        self.outputLabel.pack(side=LEFT, padx=(40, 0), pady=5)
        self.outputBtn.pack(side=RIGHT, padx=(5, 30))
        self.outputElement.pack(side=RIGHT, padx=(20, 0), pady=5)
        self.outputElement.bind("<Button-1>", self.promptOutput)

        # Log
        self.logText = Text(self.window, relief=SUNKEN, bg="#e3e3e3", height=10, width=50)
        self.logText.pack(fill=X, padx=10, pady=(30, 10))

        # Commands
        self.commandFrame = Frame(self.window)
        self.quitBtn = Button(self.commandFrame, text="Quit", command=self.window.destroy)
        self.fetchBtn = Button(self.commandFrame, text="Fetch", command=self.fetch)

        # Commands Pack
        self.commandFrame.pack(fill=X, expand=False, padx=1, pady=(40, 1), anchor=S)
        self.quitBtn.pack(side=RIGHT, padx=5, pady=3)
        self.fetchBtn.pack(side=RIGHT, padx=5, pady=3)

        self.window.mainloop()


Tool()
