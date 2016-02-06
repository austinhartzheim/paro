import os.path
from libs import errors


class DotDir():

    def create(self):
        '''
        Create the .paro directory if it does not exist.

        :raises: :class:`libs.errors.DotDirAlreadyExists` if the .paro
          directory already exists.
        '''
        if self.exists():
            raise errors.DotDirAlreadyExists()

        os.mkdir('.paro')

    def exists(self):
        '''
        Check if the .paro directory exists in the CWD.

        :returns bool: True if the file exists, False if it does not.
        '''
        if os.path.exists('.paro'):
            return True
        return False

    @property
    def path(self):
        return os.path.abspath('.paro')
