class NotSquareError(Exception):
    def __init__(self, *args):
        self.args = args


class NotPowOfTwoError(Exception):
    def __init__(self, *args):
        self.args = args


class NotSameSizeError(Exception):
    def __init__(self, *args):
        self.args = args
