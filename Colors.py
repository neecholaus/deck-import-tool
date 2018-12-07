class Colors:
    RED = "\033[1;31;40m"
    GREEN = "\033[1;32;40m"
    YELLOW = "\033[1;33;40m"
    RESET = "\033[0m"
    CHECK = GREEN + u"\u2713" + RESET
    WARNING = YELLOW + u"\u2022" + RESET
    EX = RED + u"\u02df" + RESET
