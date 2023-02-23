import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test for class Review"""

    def test_place_id(self):
        """Test class attributes named place id"""
        obj = Review()
        self.assertEqual(obj.place_id, "")
        obj.place_id = "gabrielitotititotitito"
        self.assertEqual(obj.place_id, "gabrielitotititotitito")

    def test_user_id(self):
        """Test class attributes named user id"""
        obj = Review()
        self.assertEqual(obj.user_id, "")
        obj.user_id = "gabrielitotititotitito"
        self.assertEqual(obj.user_id, "gabrielitotititotitito")

    def test_text(self):
        """Test class attributes named text"""
        obj = Review()
        self.assertEqual(obj.text, "")
        obj.text = "gabrielitotititotitito"
        self.assertEqual(obj.text, "gabrielitotititotitito")


if __name__ == '__main__':
    unittest.main()
