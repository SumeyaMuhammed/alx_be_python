import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):

  def setUp(self):
    self.calc = SimpleCalculator()
  def test_add(self):
    self.assertEqual(self.calc.add(10,5),15)
    self.assertEqual(self.calc.add(10,-10),0)
    self.assertEqual(self.calc.add(10,0),10)
    self.assertEqual(self.calc.add(10,-5),5)
    self.assertEqual(self.calc.add(0,0),0)

  def test_subtract(self):
    self.assertEqual(self.calc.subtract(10,5),5)
    self.assertEqual(self.calc.subtract(10,-10),20)
    self.assertEqual(self.calc.subtract(10,0),10)
    self.assertEqual(self.calc.subtract(10,-5),15)
    self.assertEqual(self.calc.subtract(0,0),0)

  def test_multiply(self):
    self.assertEqual(self.calc.multiply(10,5),50)
    self.assertEqual(self.calc.multiply(10,-10),-100)
    self.assertEqual(self.calc.multiply(10,0),0)
    self.assertEqual(self.calc.multiply(10,-5),-50)
    self.assertEqual(self.calc.multiply(0,0),0)

  def test_divide(self):
    self.assertEqual(self.calc.divide(10,5),2)
    self.assertEqual(self.calc.divide(10,-10),-1)
    self.assertEqual(self.calc.divide(10,-5),-2)
    self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
  unittest.main()