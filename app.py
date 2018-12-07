import sys
import os.path
from Arguments import Arguments
from DeckImport import DeckImport
from Colors import Colors
from Tkinter import *
from tkFileDialog import *


class Tool:
    def promptInput(self):        
        input = askopenfilename(initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        self.inputElement.delete(0, END)
        if(Arguments.validateInput(input)):                        
            self.inputElement.insert(0, input)
            self.appendToLog("CSV path is valid.")
            self.input = input
        else:
            self.appendToLog("Selected input path is not valid.")

    def promptOutput(self):
        output = askdirectory()
        self.outputElement.delete(0, END)
        if(Arguments.validateOutput(output)):            
            self.outputElement.insert(0, output)
            self.appendToLog("Output path has been found.")
            self.output = output
        else:
            self.appendToLog("Output path is unavailable.")

    def fetch(self):
        DeckImport(self.input, self.output)

    def appendToLog(self, string):
        self.logText.insert(END, "\n" + string)

    def __init__(self):
        self.input = None
        self.output = None

        # Create canvas
        self.window = Tk()

        # Set window icon
        self.window.iconbitmap(r'favicon.ico')
 
        # Main window configuration
        self.window.title("Custom Deck Importer")
        self.window.resizable(0, 0)

        # Header
        self.header = Label(self.window, text="Custom Deck Importer", font=("Helvetica 15 bold"))
        self.header.pack(pady=(20, 30))

        # Input
        self.inputFrame = Frame(self.window)
        self.inputLabel = Label(self.inputFrame, text="Input Path:", width=10, anchor="e", font=("Helvetica 10 bold"))
        self.inputBtn = Button(self.inputFrame, text="Find", command=self.promptInput, padx=5)
        self.inputElement = Entry(self.inputFrame, width=50)        

        # Input Pack
        self.inputFrame.pack(fill=X)
        self.inputLabel.pack(side=LEFT, padx=(50, 0), pady=5)
        self.inputBtn.pack(side=RIGHT, padx=(5, 30))
        self.inputElement.pack(side=RIGHT, padx=(20, 0), pady=5)

        # Output
        self.outputFrame = Frame(self.window)
        self.outputLabel = Label(self.outputFrame, text="Output Path:", width=10, anchor="e", font=("Helvetica 10 bold"))
        self.outputBtn = Button(self.outputFrame, text="Find", command=lambda: self.promptOutput(), padx=5)
        self.outputElement = Entry(self.outputFrame, width=50)

        # Output Pack
        self.outputFrame.pack(fill=X)
        self.outputLabel.pack(side=LEFT, padx=(50, 0), pady=5)
        self.outputBtn.pack(side=RIGHT, padx=(5, 30))
        self.outputElement.pack(side=RIGHT, padx=(20, 0), pady=5)

        # Log
        self.logLabel = Label(self.window, text="Log", anchor=W)
        self.logText = Text(self.window, relief=SUNKEN, bg="#e3e3e3", height=10, width=50)

        # Log Pack
        self.logLabel.pack(fill=X, padx=10, pady=(40, 0))
        self.logText.pack(fill=X, padx=10, pady=(0, 10))

        # Commands
        self.commandFrame = Frame(self.window)
        self.quitBtn = Button(self.commandFrame, text="Quit", padx=5, pady=2, command=self.window.destroy)
        self.fetchBtn = Button(self.commandFrame, text="Fetch", padx=5, pady=2, command=self.fetch)

        # Commands Pack
        self.commandFrame.pack(fill=X, expand=False, padx=1, pady=(40, 1), anchor=S)
        self.quitBtn.pack(side=RIGHT, padx=5, pady=3)
        self.fetchBtn.pack(side=RIGHT, padx=5, pady=3)

        self.window.mainloop()


Tool()
