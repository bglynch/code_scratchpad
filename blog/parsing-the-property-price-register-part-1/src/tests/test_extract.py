import unittest
from src import extract as ex


class ExtractTests(unittest.TestCase):
    def test_extract_eircode(self):
        self.assertEqual(ex.extract_eircode_from_end_of_address('1 Some Place, K67 KR86'), "K67 KR86")
        self.assertEqual(ex.extract_eircode_from_end_of_address('1 Some Place K67 KR86'), "K67 KR86")
        self.assertEqual(ex.extract_eircode_from_end_of_address('1 Some Place, K67KR86'), "K67 KR86")

    def test_extract_dublin_postcode(self):
        self.assertEqual(ex.extract_dublin_postcode_from_address('1 some place, dublin_9'),   "Dublin 9")
        self.assertEqual(ex.extract_dublin_postcode_from_address('1 some place, dublin_14'),  "Dublin 14")
        self.assertEqual(ex.extract_dublin_postcode_from_address('1 some place, dublin_6w'),  "Dublin 6W")
        self.assertEqual(ex.extract_dublin_postcode_from_address('1 place, dublin_10, town'), "Dublin 10")
        self.assertEqual(ex.extract_dublin_postcode_from_address('1 place, town, dublin_6'),  "Dublin 6")

    def test_extract_county(self):
        self.assertEqual(ex.extract_county_from_address('1 some place, co_limerick'), "Limerick")
        self.assertEqual(ex.extract_county_from_address('1 some place, co_cork'),     "Cork")
        self.assertEqual(ex.extract_county_from_address('1 some place'),     None)


if __name__ == '__main__':
    unittest.main()
