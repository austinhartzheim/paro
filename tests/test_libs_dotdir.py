import unittest
import unittest.mock
import os
from libs.dotdir import DotDir
from libs import errors


class TestDotDir(unittest.TestCase):

    @unittest.mock.patch('os.mkdir')
    def test_create(self, p_mkdir):
        '''
        Test that the create() method properly creates the .paro
        directory using os.mkdir.
        '''
        dd = DotDir()
        dd.create()
        p_mkdir.assert_called_once_with('.paro')

    @unittest.mock.patch('libs.dotdir.DotDir.exists')
    @unittest.mock.patch('os.mkdir')
    def test_create_already_exists(self, p_dotdir_exists, p_mkdir):
        '''
        Test that the .create() method raises an error when attempting
        to create a directory that already exists.
        '''
        p_dotdir_exists.return_value = True

        dd = DotDir()
        self.assertRaises(errors.DotDirAlreadyExists, dd.create)
        p_mkdir.assert_not_called()

    @unittest.mock.patch('os.path.exists')
    def test_exists(self, p_exists):
        '''
        Test that the .exists() method directly returns the
        value of os.path.exists().
        '''
        dd = DotDir()

        p_exists.return_value = True
        self.assertTrue(dd.exists())
        p_exists.assert_called_once_with('.paro')

        p_exists.reset_mock()

        p_exists.return_value = False
        self.assertFalse(dd.exists())
        p_exists.assert_called_once_with('.paro')

