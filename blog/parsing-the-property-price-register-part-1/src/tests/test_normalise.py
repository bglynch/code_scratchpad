import unittest
from src import normalise as nm


class ExtractTests(unittest.TestCase):
    def test_parse_address_of_eircode(self):
        self.assertEqual(nm.normalise_county_name('1 Some Place, co cork'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, co. cork'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, co .cork'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, co.cork'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place co cork'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place  co cork'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place county cork'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place countycork'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place cork county'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place  cork'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place  cork.'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, cork'), "1 some place, co_cork")
# outliers
# 1 blackthorne drive, belfield, ferrybank  via waterford
# 17 island villas, barony of uppercross, city of dublin
# Kilkenny	2 mullinabro woods, newrath, via waterford
# 20 st finbarrs park, glasheen rd, the louth
# 20 slade castle avenue, saggart, cointy dublin



# 58 hanaville park, terenure, city of dublin

# 64 rosehill, newport, via limerick
# 922 st patricks park, celbridge, countuy kildare



if __name__ == '__main__':
    unittest.main()
