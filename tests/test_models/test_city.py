#!/usr/bin/python3
"""
Test Module: Ameinity
test_base_model.py - unittests for "Amenity'
"""
import unittest
from models.city import City


class test_city(unittest.TestCase):
    """
    City  Tests
    """
    def test_city(self):
        """
        does it exist
        """
        inst_1 = City()
        self.assertTrue(inst_1)

    def test_city_instance_del(self):
        """
        test delete
        """
        inst_1_1 = City()
        del inst_1_1

    def test_city_instance(self):
        """
        test instance
        """
        inst_2 = City()
        self.asertisInstance(inst_2, City)

    def test_city_save(self):
        """
        test save
        """
        updated_city = inst_3.updated_at
        inst_3.save = City()
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_city, new_inst_3)

    def test_city_str(self):
        """
        test type
        """
        inst_4 = City()
        self.assertIsInstance(inst_4.city, str)
