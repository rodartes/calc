import unittest
import calculator2

class TestCalc(unittest.TestCase):
   def test_add(self):
      self.assertEqual(calculator2.sum(1,-1), 0)
      self.assertEqual(calculator2.sum(2,2), 4)
      self.assertEqual(calculator2.sum(-2,-2), -4)

   def test_sub(self):
      self.assertEqual(calculator2.diff(5,3), 2)
      self.assertEqual(calculator2.diff(-1,5), -6)
      self.assertEqual(calculator2.diff(0,0), 0)

   def test_mul(self):
      self.assertEqual(calculator2.prod(2,0), 0)
      self.assertEqual(calculator2.prod(2,-2), -4)
      self.assertEqual(calculator2.prod(-2,-2), 4)

   def test_div(self):
      self.assertEqual(calculator2.quo(8,4), 2)
      self.assertEqual(calculator2.quo(8,-4), -2)
      self.assertEqual(calculator2.quo(10,0), "Undefined")

if __name__ == '__main__':
   unittest.main()
