import unittest
from src import extract as ex


class ExtractTests(unittest.TestCase):
    def test_extract_eircode(self):
        self.assertEqual(ex.extract_eircode_from_end_of_address('1 Some Place, K67 KR86'), "K67 KR86")
        self.assertEqual(ex.extract_eircode_from_end_of_address('1 Some Place K67 KR86'), "K67 KR86")
        self.assertEqual(ex.extract_eircode_from_end_of_address('1 Some Place, K67KR86'), "K67 KR86")


if __name__ == '__main__':
    unittest.main()
