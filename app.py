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
        if(Arguments.validateInput(input)):            
            self.inputElement.delete(0, END)
            self.inputElement.insert(0, input)
            self.appendToLog("CSV path is valid.")
        else:
            self.appendToLog("Selected input path is not valid.")

    def promptOutput(self):
        output = askdirectory()
        if(Arguments.validateOutput(output)):
            self.outputElement.delete(0, END)
            self.outputElement.insert(0, output)
            self.appendToLog("Output path has been found.")
        else:
            self.appendToLog("Output path is unavailable.")

    def appendToLog(self, string):
        self.logText.insert(END, "\n" + string)

    def __init__(self):
        # Create canvas
        self.window = Tk()

        # Set window icon
        self.window.iconbitmap(r'favicon.ico')
 
        # Main window configuration
        self.window.title("Custom Deck Importer")
        self.window.resizable(0, 0)

        # Header
        self.header = Label(self.window, text="Custom Deck Importer", font=("Helvetica", 20))
        self.header.pack(pady=(20, 30))

        # Input
        self.inputFrame = Frame(self.window)
        self.inputLabel = Label(self.inputFrame, text="Input Path:", width=10, anchor="e")
        self.inputBtn = Button(self.inputFrame, text="Find", command=self.promptInput)
        self.inputElement = Entry(self.inputFrame, width=30)        

        # Input Pack
        self.inputFrame.pack(fill=X)
        self.inputLabel.pack(side=LEFT, padx=(50, 0), pady=5)
        self.inputBtn.pack(side=RIGHT, padx=(0, 30))
        self.inputElement.pack(side=RIGHT, padx=(20, 0), pady=5)

        # Output
        self.outputFrame = Frame(self.window)
        self.outputLabel = Label(self.outputFrame, text="Output Path:", width=10, anchor="e")
        self.outputBtn = Button(self.outputFrame, text="Find", command=lambda: self.promptOutput())
        self.outputElement = Entry(self.outputFrame, width=30)

        # Output Pack
        self.outputFrame.pack(fill=X)
        self.outputLabel.pack(side=LEFT, padx=(50, 0), pady=5)
        self.outputBtn.pack(side=RIGHT, padx=(0, 30))
        self.outputElement.pack(side=RIGHT, padx=(20, 0), pady=5)

        # Log
        self.logLabel = Label(self.window, text="Log", anchor=W)
        self.logText = Text(self.window, relief=SUNKEN, bg="#e3e3e3", height=10)

        # Log Pack
        self.logLabel.pack(fill=X, padx=10, pady=(40, 0))
        self.logText.pack(fill=X, padx=10, pady=(0, 10))

        # Commands
        self.commandFrame = Frame(self.window)
        self.fetchBtn = Button(self.commandFrame, text="Fetch")
        self.quitBtn = Button(self.commandFrame, text="Quit", command=self.window.destroy)

        # Commands Pack
        self.commandFrame.pack(fill=X, expand=False, padx=1, pady=(40, 1), anchor=S)
        self.quitBtn.pack(side=RIGHT)
        self.fetchBtn.pack(side=RIGHT)

        self.window.mainloop()
        # end canvas

        # DeckImport(input, output)


Tool()
