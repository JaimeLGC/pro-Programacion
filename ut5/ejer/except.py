class NotIntError(Exception):
    def __init__(self, message="Miloco..."):
        super().__init__(message)


def getint() -> int:
    num = input("Give me an integer number: ")
    try:
        int(num)
    except ValueError as err:
        print(f"Not a valid integer. Try it again! {err}")
        getint()
    else:
        print("lessgo")


def getint2():
    pass


getint()
