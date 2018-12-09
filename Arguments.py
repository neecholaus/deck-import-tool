import os.path
from Colors import Colors


class Arguments:
    def __init__(self, input, output):
        print("")

    @staticmethod
    def validateInput(input):
        srcExists = os.path.isfile(input)
        return True if srcExists else False

    @staticmethod
    def validateOutput(output):
        dirExists = os.path.isdir(output)

        # Handle non existent output dir
        if(not dirExists):
            try:
                os.makedirs(output)
            except:
                # print("Output directory could not be created.")
                # print(output)
                return False

        return True
