#!/usr/bin/python3
"""
Test Module: Review
test_base_model.py - unittests for 'Review'
"""
import unittest
from models.review import review


class test_review(unittest.TestCase):
    """
    review Tests
    """
    def test_review(self):
        """
        does it exist
        """
        inst_1 = review()
        self.assertTrue(inst_1)

    def test_review_instance_del(self):
        """
        test delete
        """
        inst_1_1 = review()
        del inst_1_1

    def test_review_instance(self):
        """
        test instance
        """
        inst_2 = review()
        self.asertisInstance(inst_2, review)

    def test_review_save(self):
        """
        test save
        """
        updated_review = inst_3.updated_at
        inst_3.save = review()
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_review, new_inst_3)

    def test_name_str(self):
        """
        test type
        """
        inst_4 = review()
        self.assertIsInstance(inst_4.name, str)

    def test_place_id_str(self):
        """
        test place_id exists
        """
        inst_4 = review()
        self.assertIsInstance(inst_4.email, str)

    def test_user_id_str(self):
        """
        test user_id exists
        """
        inst_5 = review()
        self.assertIsInstance(inst_5.password, str)

    def test_text_str(self):
        """
        test the text of the review
        """
        inst_6 = review()
        self.assertIsInstance(inst_6.text, str)


if __name__ == '__main__':
    unittest.main()
