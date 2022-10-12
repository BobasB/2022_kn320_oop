import unittest
from lab import Rocket

class TestMyApp(unittest.TestCase):
    def test_if_object_created(self):
        name = "Ares I"
        mass = 25400
        obj = Rocket(name, mass)
        self.assertEqual(obj.name, name)
        self.assertEqual(obj.mass, mass)
        self.assertIsInstance(obj, Rocket)
        self.assertNotIsInstance(obj, str)
    
    def test_mock(self):
        self.assertTrue(True)
    

#if __name__ == '__main__':
#    unittest.main(verbosity=2)