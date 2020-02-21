#!/usr/bin/python3

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import unittest
import pep8


class Test_BaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.Base = BaseModel()
        cls.Base.name = "Julian"
        cls.Base.cod = 1193

    def test_save(self):

        self.Base2.save()
        self.assertNotEqual(self.Base2.created_at, self.Base2.updated_at)

    def test_to_dict(self):

        test_dict = self.base_mod.to_dict()
        self.assertTrue(test_dict.get("__class__"))
        self.assertTrue(type(test_dict) is dict)
        self.assertTrue("to_dict" in dir(self.base_mod))

if __name__ == "__main__":
    unittest.main()
