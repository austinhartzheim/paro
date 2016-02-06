class ParoError(Exception):
    pass


class DotDirAlreadyExists(ParoError):
    '''
    Raised when attempting to create the .paro directory, but it
    already exists.
    '''
    pass


class DotDirDoesNotExist(ParoError):
    '''
    Raised when the .paro directory does not exist.
    '''
    pass


class ParoFileAlreadyExists(ParoError):
    '''
    Raised when attempting to create the paro.yaml file, but it
    already exists.
    '''
    pass


class ParoFileDoesNotExist(ParoError):
    '''
    Raised when the paro.yaml file does not exist.
    '''
    pass
