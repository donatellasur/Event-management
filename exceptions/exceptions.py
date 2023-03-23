class ValidationException(Exception):
    pass


class ValidatorExceptions(ValidationException):
    def __init__(self, mssgs):
        self.__mssgs = mssgs

    def getMessages(self):
        return self.__mssgs

    def __str__(self):
        return 'Validation Exception:\n' + str(self.__mssgs)
