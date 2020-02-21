"""This file marks the models directory as a python package directory"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
