import unittest
from lab import Rocket

class TestMyApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.name = "Ares I"
        cls.mass = 25400
        
    def setUp(self) -> None:
        self.obj = Rocket(self.name, self.mass)

    def test_if_object_created(self):
        self.assertEqual(self.obj.name, self.name)
        self.assertEqual(self.obj.mass, self.mass)
        self.assertIsInstance(self.obj, Rocket)
        self.assertNotIsInstance(self.obj, str)
    
    def test_correct_output(self):
        self.assertIn(self.name, self.obj.get_mass)
        self.assertIn(str(self.mass), self.obj.get_mass)
    
    def test_converter(self):
        for mass in [20, 30.1, 50.356, 524588, 646.64646]: # Ми можемо передавати будб які числові значення
            obj = Rocket(self.name, mass)
            self.assertAlmostEqual(obj.convert_to_pounds(), float(f"{mass * 2.20462262:.3f}"), 3)
        for mass in [-10, 0]: # Пеервірка чи в процесі роботи хтось не змінив масу на відємну
            self.obj.mass = mass
            self.assertIsNone(self.obj.convert_to_pounds())
        
    def test_mass_greater_then_zero(self):
        with self.assertRaises(AssertionError):
            obj = Rocket(self.name, -1)
        self.assertIsInstance(Rocket(self.name, 0), Rocket)
    
    def test_mass_as_a_string(self):
        with self.assertRaises(TypeError):
            Rocket(self.name, '152')
           

if __name__ == '__main__':
    unittest.main(verbosity=2)