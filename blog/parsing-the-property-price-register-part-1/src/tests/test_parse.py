import unittest
from src import parse as pr


class ExtractTests(unittest.TestCase):
    def test_parse_address_of_eircode(self):
        self.assertEqual(pr.parse_address_of_eircode('1 Some Place, K67 KR86'), "1 Some Place")
        self.assertEqual(pr.parse_address_of_eircode('1 Some Place K67 KR86'),  "1 Some Place")
        self.assertEqual(pr.parse_address_of_eircode('1 Some Place, K67KR86'),  "1 Some Place")

    def test_parse_address_of_dublin_postcode(self):
        self.assertEqual(pr.parse_address_of_dublin_postcode('1 some place, dublin_9'),   "1 some place")
        self.assertEqual(pr.parse_address_of_dublin_postcode('1 some place, dublin_14'),  "1 some place")
        self.assertEqual(pr.parse_address_of_dublin_postcode('1 some place, dublin_6w'),  "1 some place")
        self.assertEqual(pr.parse_address_of_dublin_postcode('1 place, dublin_10, town'), "1 place, town")
        self.assertEqual(pr.parse_address_of_dublin_postcode('1 place, town, dublin_6'),  "1 place, town")

    def test_parse_address_of_county(self):
        self.assertEqual(pr.parse_address_of_county('1 some place, co_dublin'), "1 some place")


if __name__ == '__main__':
    unittest.main()
