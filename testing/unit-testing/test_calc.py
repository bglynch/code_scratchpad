# Naming convention to start test files with 'test_'
import unittest
import calc


class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1),0)
        self.assertEqual(calc.add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1),-2)
        self.assertEqual(calc.subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1),-1)
        self.assertEqual(calc.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1),-1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)


        # self.assertRaises(Error-Expected, function-to-run, each-argument-seperatly)
        self.assertRaises(ValueError, calc.divide, 10, 0)
        
        # second way to test exceptions
        with self.assertRaises(ValueError):
            calc.divide(10,0)
        # 
    




# if we dont have this line tests are run as 'python3 -m unittest test_calc.py'
# else run as 'python3 test_calc.py'
if __name__ == '__main__':
    unittest.main()