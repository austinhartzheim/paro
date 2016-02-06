import os.path
import yaml
from libs import errors


class ParoFile():

    VERSION = 0
    INITIAL_STATE = {
        'file-version': VERSION,
        'script': []
    }

    def __init__(self):
        self.data = {}

    def create(self):
        '''
        Create the paro.yaml file if it does not exist.

        :raises: :class:`libs.errors.ParoFileAlreadyExists` if the
          paro.yaml file already exists.
        '''
        if self.exists():
            raise errors.ParoFileAlreadyExists()

        with open('paro.yaml', 'w') as pf:
            yaml.dump(self.INITIAL_STATE, pf)

    def exists(self):
        '''
        Search the current path for files indicating that we are in a
        paro working directory.

        :returns bool: True if the file exists, False if it does not.
        '''
        # TODO: Add path searching
        if os.path.exists('paro.yaml'):
            return True
        return False

    def load(self):
        '''
        Load data from the paro.yaml file.
        '''
        if not self.exists():
            raise errors.ParoFileDoesNotExist()

        with open('paro.yaml') as pf:
            self.data = yaml.load(pf)

    @property
    def path(self):
        return os.path.abspath('paro.yaml')
