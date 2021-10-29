#!/usr/bin/python3
"""
file test strage
file storage test
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.engine.filestorage import BaseModel
from models.engine.file_storage import FileStorage


class test_file_storage(unittest.TestCase):
    """
    test file storage
    """
    def setUp(self):
        """ setup test for FileStorage
        """
        self.storage = FileStorage()

    def test_attrs(self):
        """
        test for attributes
        """
        self.assertFalse(hasattr(self.storage, "mw.json"))


if "__name__" == __main__:
        unittest.main()
