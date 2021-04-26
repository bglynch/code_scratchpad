import unittest
from src import parse as pr


class ExtractTests(unittest.TestCase):
    def test_parse_address_of_eircode(self):
        self.assertEqual(pr.parse_address_of_eircode('1 Some Place, K67 KR86'), "1 Some Place")
        self.assertEqual(pr.parse_address_of_eircode('1 Some Place K67 KR86'), "1 Some Place")
        self.assertEqual(pr.parse_address_of_eircode('1 Some Place, K67KR86'), "1 Some Place")


if __name__ == '__main__':
    unittest.main()
