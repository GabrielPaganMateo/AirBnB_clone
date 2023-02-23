import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test class for File Storage"""

    def test_all(self):
        """Test class method named all"""
        storage = FileStorage()
        all_objs = storage.all()
        self.assertEqual(all_objs, {})
        storage = FileStorage()
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()
        all_objects_reloaded = storage.reload()
        self.assertNotEqual(all_objects_reloaded, all_objs)

    def test_new(self):
        """Test class method named new"""
        storage = FileStorage()
        obj1 = BaseModel()
        storage.new(obj1)
        obj_name = f'BaseModel.{obj1.id}'
        var = storage.all()[obj_name]
        self.assertEqual(obj1, var)
        obj2 = BaseModel()
        storage.new(obj2)
        obj_name = f'BaseModel.{obj2.id}'
        var = storage.all()[obj_name]
        self.assertNotEqual(obj1, var)

    def test_save(self):
        """Test class method named save"""
        obj2 = BaseModel()
        obj2.name = "My_First_Model"
        obj2.my_number = 89
        obj2.save()
        self.assertIn(obj2.name, obj2.__dict__.values())
        self.assertIn(obj2.my_number, obj2.__dict__.values())
        obj2.name = "My_Second_Model"
        obj2.save()
        self.assertIn("My_Second_Model", obj2.__dict__.values())
        self.assertNotIn("My_First_Model", obj2.__dict__.values())

    def test_reload(self):
        """Test class method named reload"""
        storage = FileStorage()
        all_objs = storage.all()
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()
        all_objects_reloaded = storage.reload()
        self.assertNotEqual(all_objects_reloaded, all_objs)


if __name__ == '__main__':
    unittest.main()
