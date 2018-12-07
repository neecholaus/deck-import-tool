import os.path
from Colors import Colors

class Arguments:
    def __init__(self, input, output):
        self.validateInput(input)
        self.validateOutput(output)
    
    @staticmethod
    def validateInput(input):
        # Verify csv exists
        srcExists = os.path.isfile(input)

        # Handle non existent csv
        if(not srcExists):
            print(Colors.EX + " CSV could not be found.")
            print("Path: " + input + "")
            exit()

    def validateOutput(self, output):
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