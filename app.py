import sys
import os.path
from Arguments import Arguments
from DeckImport import DeckImport
from Colors import Colors
from Tkinter import *
from tkFileDialog import *

class Tool:

    def promptInput(self, ui):
        input =  askopenfilename(initialdir="/",title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        Arguments.validateInput(input)

    def __init__(self):
        # Create canvas
        window = Tk()

        # Main window configuration
        window.title("Custom Deck Importer")
        window.resizable(0, 0)

        # Header
        header = Label(window, text="Custom Deck Importer", font=("Helvetica", 20))
        header.pack(pady=(20, 30))

        # Input
        inputFrame = Frame(window)
        inputLabel = Label(inputFrame, text="Input Path:", width=10, anchor="e")
        inputBtn = Button(inputFrame, text=u"\u25BC", command=lambda:self.promptInput(window))
        inputElement = Entry(inputFrame, width=30)

        # Input Pack
        inputFrame.pack(fill=X)
        inputLabel.pack(side=LEFT, padx=(50, 0), pady=5)
        inputBtn.pack(side=RIGHT, padx=(0, 30))
        inputElement.pack(side=RIGHT, padx=(20, 0), pady=5)

        # Output
        outputFrame = Frame(window)
        outputLabel = Label(outputFrame, text="Output Path:", width=10, anchor="e")
        outputBtn = Button(outputFrame, text=u"\u25BC",)
        outputElement = Entry(outputFrame, width=30)

        # Output Pack
        outputFrame.pack(fill=X)
        outputLabel.pack(side=LEFT, padx=(50, 0), pady=5)
        outputBtn.pack(side=RIGHT, padx=(0, 30))
        outputElement.pack(side=RIGHT, padx=(20, 0), pady=5)

        # Log
        logLabel = Label(window, text="Log", anchor=W)
        logText = Text(window, relief=SUNKEN, bg="#e3e3e3", height=10)

        # Log Pack
        logLabel.pack(fill=X, padx=10, pady=(40, 0))
        logText.pack(fill=X, padx=10, pady=(0, 10))

        # Commands
        commandFrame = Frame(window)
        fetchBtn = Button(commandFrame, text="Fetch", command=lambda:self.promptInput(window))
        quitBtn = Button(commandFrame, text="Quit", command=window.destroy)

        # Commands Pack
        commandFrame.pack(fill=X, expand=False, padx=1, pady=(40, 1), anchor=S)
        quitBtn.pack(side=RIGHT)
        fetchBtn.pack(side=RIGHT)



        window.mainloop()
        #end canvas

        # DeckImport(input, output)


Tool()