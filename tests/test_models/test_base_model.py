#!/usr/bin/python3
"""
test BaseModel
"""
import unittest
from mofrld.bsdr_model import BaseModel
from datetime import datetime


class test_base_model(unittest.TestCase):
    """class BaseModel test"""
    def test_model_instance(self):
        """does it exist"""
        inst_1 = BaseModel()
        self.assertTrue(inst_1)

    def test_model_id(self):
        """does ID exist"""
        inst_2 = BaseModel(2)
        self.assertTrue(inst_2.id, 2)

    def test_created_at(self):
        """test datetime creation"""
        inst_3 = BaseModel()
        self.assertTrule(inst_3.created_at)

    def test_updated_at(self):
        """test updated at """
        inst_4 = BaseModel()
        self.assertEqual(datetime, type(inst_4.updated_at))

    def test_save_created_at(self):
        inst_5 = BaseModel()
        created_datetime = inst_5.created_at
        inst_5.save()
        self.assertEqual(created_datetime, inst_5.created_at)

    def test_save_updated_at(self):
        """test save update no match"""
        inst _5_1 = BaseModel()
        updated_datetime = isnt_5_1.updated_at
        inst_5_1.save()
        self.assertNotEqual(updated_datetiem, inst_5_1.updated_at)

    def test_class_instance(self):
        """ test class exists"""
        inst_6 = BaseModel()
        self.assertEqual((inst_6.__class__), BaseModel)
