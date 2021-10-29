#!/usr/bin/python3
"""
test Module: State
test_state.py - unittests for "State'
"""
import unittest
from models.amenity import State


class test_state(unittest.TestCase):
    """
    State Tests
    """

    def test_state(self):
        """
        does it exist
        """
        inst_1 = State()
        self.assertTrue(inst_1)

    def test_state_instance_del(self):
        """
        test delete
        """
        inst_1_1 = State()
        del inst_1_1

    def test_state_instance(self):
        """
        test instance
        """
        inst_2 = State()
        self.asertisInstance(inst_2, State)

    def test_state_save(self):
        """
        test save
        """
        updated_state = inst_3.updated_at
        inst_3.save = State()
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_State, new_inst_3)

    def test_name_str(self):
        """
        test type
        """
        inst_4 = State()
        self.assertIsInstance(inst_4.state, str)
