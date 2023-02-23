import unittest
import io
import unittest.mock
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Base Model class"""

    def test_init(self):
        """Test init method"""
        obj_1 = BaseModel()
        self.assertIsNotNone(obj_1.id)
        self.assertIsNotNone(obj_1.created_at)
        self.assertEqual(obj_1.created_at, obj_1.updated_at)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, obj, mock_stdout):
        """Initializing auxiliar method"""
        print(obj)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test str method"""
        obj = BaseModel()
        obj_str = f'[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}\n'
        self.assert_stdout(obj_str, obj)

    def test_save(self):
        """Test save method"""
        obj = BaseModel()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        obj = BaseModel()
        a_dict = obj.to_dict()
        obj_dict = {
            'id': obj.id,
            '__class__': obj.__class__.__name__,
            'created_at': obj.created_at.isoformat(),
            'updated_at': obj.updated_at.isoformat()}
        self.assertDictEqual(a_dict, obj_dict)


if __name__ == '__main__':
    unittest.main()
