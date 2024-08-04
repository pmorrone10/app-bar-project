class InvalidBeerException(Exception):
    def __init__(self, message='Problems loading beer'):
        super().__init__(message)
