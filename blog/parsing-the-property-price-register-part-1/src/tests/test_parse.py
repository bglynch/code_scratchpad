import unittest
from src import parse as pr


class ExtractTests(unittest.TestCase):
    def test_extract_eircode(self):
        self.assertEqual(pr.parse_address_of_eircode('12 Longlands, Swords, K67 KR86'), "K67 KR86")


if __name__ == '__main__':
    unittest.main()