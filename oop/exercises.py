import unittest

def square(num = 3):
  result = num ** 2
  return result

class TastSquare(unittest.TestCase):
  def test_square(self):
    self.assertEqual(square(3), 9)
    self.assertEqual(square(0), 0)
    self.assertEqual(square(-3), 9)

  def test_error(self):
    self.assertRaises(TypeError, square, "2")



if __name__ == "__main__":
  unittest.main()