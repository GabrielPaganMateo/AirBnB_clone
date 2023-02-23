import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test for class City"""

    def test_state_id(self):
        """Test class attributes named state_id"""
        obj = City()
        self.assertEqual(obj.state_id, "")
        obj.state_id = "gabrielitotititotitito"
        self.assertEqual(obj.state_id, "gabrielitotititotitito")

    def test_name(self):
        """Test class attributes named name"""
        obj = City()
        self.assertEqual(obj.name, "")
        obj.name = "gabrielitotititotitito"
        self.assertEqual(obj.name, "gabrielitotititotitito")


if __name__ == '__main__':
    unittest.main()
