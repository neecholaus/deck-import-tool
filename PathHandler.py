import os.path


class PathHandler:
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
                return False

        return True
