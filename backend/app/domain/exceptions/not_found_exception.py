

class NotFoundException(Exception):
    def __init__(self, message='Not Found Exception'):
        super().__init__(message)

