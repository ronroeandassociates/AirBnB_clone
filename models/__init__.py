#!/usr/bin/python3
"""
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


available_rooms = {'BaseModel' : BaseModel}
storage = FileStorage()
storage.reload()
