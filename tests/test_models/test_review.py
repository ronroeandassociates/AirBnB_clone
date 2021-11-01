#!/usr/bin/python3
"""
Test Module: Review
test_base_model.py - unittests for 'Review'
"""
import unittest
from models.review import Review


class test_Review(unittest.TestCase):

    """
    Review Tests
    """

    def test_Review(self):
        """
        does it exist
        """
        inst_1 = Review()
        self.assertTrue(inst_1)

    def test_Review_instance_del(self):
        """
        test delete
        """
        inst_1_1 = Review()
        del inst_1_1

    def test_Review_instance(self):
        """
        test instance
        """

        inst_2 = Review()
        self.asertisInstance(inst_2, Review)

    def test_Review_save(self):
        """
        test save
        """

        inst_3 = Review()
        updated_Review = inst_3.updated_at
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_Review, new_inst_3)

    def test_name_str(self):
        """

        test type

        """
        inst_4 = Review()

        self.assertIsInstance(inst_4.name, str)

    def test_place_id_str(self):
        """
        test place_id exists
        """

        inst_4 = Review()
        self.assertIsInstance(inst_4.email, str)

    def test_user_id_str(self):
        """
        test user_id exists
        """

        inst_5 = Review()
        self.assertIsInstance(inst_5.password, str)

    def test_text_str(self):
        """
        test the text of the Review
        """

        inst_6 = Review()
        self.assertIsInstance(inst_6.text, str)


if __name__ == '__main__':

    unittest.main()
