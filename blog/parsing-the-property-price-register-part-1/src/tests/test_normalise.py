import unittest
from src import normalise as nm


class ExtractTests(unittest.TestCase):
    def test_parse_address_of_eircode(self):
        self.assertEqual(nm.normalise_county_name('1 Some Place, co cork'),    "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, co. cork'),   "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, co . cork'),   "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, co; cork'),   "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, co: cork'),   "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, co.cork'),    "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place co cork'),     "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place  co cork'),    "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place county cork'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place countycork'),  "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place  cork'),       "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place  cork.'),      "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, cork'),       "1 some place, co_cork")
        # part of a county
        self.assertEqual(nm.normalise_county_name('1 Some Place, west cork'),        "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, nr cork'),          "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, near cork'),        "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, north dublin'),     "1 some place, co_dublin")
        self.assertEqual(nm.normalise_county_name('1 Some Place, north tipperary'),  "1 some place, co_tipperary")
        self.assertEqual(nm.normalise_county_name('1 Some Place, south tipperary'),  "1 some place, co_tipperary")
        # county misspelling
        self.assertEqual(nm.normalise_county_name('1 Some Place, ci cork'),        "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, cp cork'),        "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, clo cork'),       "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, col cork'),       "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, ci cork'),        "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, cd cork'),        "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, ci cork'),        "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, c cork'),         "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, c0. cork'),       "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, cco. cork'),      "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, o cork'),         "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, cointy cork'),    "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, ccunty cork'),    "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, cunty cork'),     "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, couty cork'),     "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, couny cork'),     "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, count cork'),     "1 some place, co_cork")
        # county name misspelling
        # = cork
        self.assertEqual(nm.normalise_county_name('1 Some Place, corl'),     "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, cokr'),     "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, crok'),     "1 some place, co_cork")
        self.assertEqual(nm.normalise_county_name('1 Some Place, coork'),     "1 some place, co_cork")
        # = donegal
        self.assertEqual(nm.normalise_county_name('1 Some Place, dongal'),      "1 some place, co_donegal")
        self.assertEqual(nm.normalise_county_name('1 Some Place, doengal'),     "1 some place, co_donegal")
        self.assertEqual(nm.normalise_county_name('1 Some Place, donegak'),     "1 some place, co_donegal")
        # = dublin
        self.assertEqual(nm.normalise_county_name('1 Some Place, dubblin'),    "1 some place, co_dublin")
        self.assertEqual(nm.normalise_county_name('1 Some Place, dubin'),      "1 some place, co_dublin")
        self.assertEqual(nm.normalise_county_name('1 Some Place, dubliln'),    "1 some place, co_dublin")
        self.assertEqual(nm.normalise_county_name('1 Some Place, dublibn'),    "1 some place, co_dublin")
        self.assertEqual(nm.normalise_county_name('1 Some Place, dublibn'),    "1 some place, co_dublin")
        self.assertEqual(nm.normalise_county_name('1 Some Place, dubllin'),    "1 some place, co_dublin")
        self.assertEqual(nm.normalise_county_name('1 Some Place, dublni'),     "1 some place, co_dublin")
        self.assertEqual(nm.normalise_county_name('1 Some Place, dubiln'),     "1 some place, co_dublin")
        self.assertEqual(nm.normalise_county_name('1 Some Place, dulbin'),     "1 some place, co_dublin")
        self.assertEqual(nm.normalise_county_name('1 Some Place, city of dublin'),     "1 some place, co_dublin")
        # = galway
        self.assertEqual(nm.normalise_county_name('1 Some Place, galwyay'),     "1 some place, co_galway")
        self.assertEqual(nm.normalise_county_name('1 Some Place, galwy'),       "1 some place, co_galway")
        self.assertEqual(nm.normalise_county_name('1 Some Place, galwat'),      "1 some place, co_galway")
        self.assertEqual(nm.normalise_county_name('1 Some Place, galwa'),       "1 some place, co_galway")
        self.assertEqual(nm.normalise_county_name('1 Some Place, glaway'),      "1 some place, co_galway")
        self.assertEqual(nm.normalise_county_name('1 Some Place, glaway'),      "1 some place, co_galway")
        # = kildare
        self.assertEqual(nm.normalise_county_name('1 Some Place, kidare'),      "1 some place, co_kildare")
        self.assertEqual(nm.normalise_county_name('1 Some Place, kidlare'),     "1 some place, co_kildare")
        self.assertEqual(nm.normalise_county_name('1 Some Place, kildae'),      "1 some place, co_kildare")
        self.assertEqual(nm.normalise_county_name('1 Some Place, kildard'),     "1 some place, co_kildare")
        self.assertEqual(nm.normalise_county_name('1 Some Place, kilfdare'),    "1 some place, co_kildare")
        self.assertEqual(nm.normalise_county_name('1 Some Place, kiildare'),    "1 some place, co_kildare")
        self.assertEqual(nm.normalise_county_name('1 Some Place, kldare'),      "1 some place, co_kildare")
        # = kilkenny
        self.assertEqual(nm.normalise_county_name('1 Some Place, kikenny'),      "1 some place, co_kilkenny")
        self.assertEqual(nm.normalise_county_name('1 Some Place, kilkennny'),    "1 some place, co_kilkenny")
        self.assertEqual(nm.normalise_county_name('1 Some Place, killkenny'),    "1 some place, co_kilkenny")
        self.assertEqual(nm.normalise_county_name('1 Some Place, kilkennt'),     "1 some place, co_kilkenny")
        # = laois
        self.assertEqual(nm.normalise_county_name('1 Some Place, loais'),        "1 some place, co_laois")
        # = leitrim
        self.assertEqual(nm.normalise_county_name('1 Some Place, leirim'),      "1 some place, co_leitrim")
        self.assertEqual(nm.normalise_county_name('1 Some Place, letrim'),      "1 some place, co_leitrim")
        # = leitrim
        self.assertEqual(nm.normalise_county_name('1 Some Place, limerck'),      "1 some place, co_limerick")
        self.assertEqual(nm.normalise_county_name('1 Some Place, limericfk'),    "1 some place, co_limerick")
        self.assertEqual(nm.normalise_county_name('1 Some Place, lmerick'),      "1 some place, co_limerick")
        self.assertEqual(nm.normalise_county_name('1 Some Place, limrick'),      "1 some place, co_limerick")
        # = leitrim
        self.assertEqual(nm.normalise_county_name('1 Some Place, lonford'),      "1 some place, co_longford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, longfors'),     "1 some place, co_longford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, longofrd'),     "1 some place, co_longford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, longfod'),      "1 some place, co_longford")
        # = louth
        self.assertEqual(nm.normalise_county_name('1 Some Place, lough'),      "1 some place, co_louth")
        self.assertEqual(nm.normalise_county_name('1 Some Place, lout'),       "1 some place, co_louth")
        self.assertEqual(nm.normalise_county_name('1 Some Place, lourth'),     "1 some place, co_louth")
        # = mayo
        self.assertEqual(nm.normalise_county_name('1 Some Place, mmyo'),      "1 some place, co_mayo")
        self.assertEqual(nm.normalise_county_name('1 Some Place, moyo'),      "1 some place, co_mayo")
        self.assertEqual(nm.normalise_county_name('1 Some Place, maro'),      "1 some place, co_mayo")
        self.assertEqual(nm.normalise_county_name('1 Some Place, mayy'),      "1 some place, co_mayo")
        self.assertEqual(nm.normalise_county_name('1 Some Place, may'),       "1 some place, co_mayo")
        # = mayo
        self.assertEqual(nm.normalise_county_name('1 Some Place, maeth'),      "1 some place, co_meath")
        self.assertEqual(nm.normalise_county_name('1 Some Place, meah'),       "1 some place, co_meath")
        self.assertEqual(nm.normalise_county_name('1 Some Place, meth'),       "1 some place, co_meath")
        # = monaghan
        self.assertEqual(nm.normalise_county_name('1 Some Place, monagha'),    "1 some place, co_monaghan")
        self.assertEqual(nm.normalise_county_name('1 Some Place, mongaghan'),  "1 some place, co_monaghan")
        self.assertEqual(nm.normalise_county_name('1 Some Place, monoghan'),   "1 some place, co_monaghan")
        self.assertEqual(nm.normalise_county_name('1 Some Place, monagan'),    "1 some place, co_monaghan")
        self.assertEqual(nm.normalise_county_name('1 Some Place, managhan'),   "1 some place, co_monaghan")
        self.assertEqual(nm.normalise_county_name('1 Some Place, monaghn'),    "1 some place, co_monaghan")
        # = offaly
        self.assertEqual(nm.normalise_county_name('1 Some Place, offay'),      "1 some place, co_offaly")
        self.assertEqual(nm.normalise_county_name('1 Some Place, offally'),    "1 some place, co_offaly")
        # = roscommon
        self.assertEqual(nm.normalise_county_name('1 Some Place, rosscommon'), "1 some place, co_roscommon")
        self.assertEqual(nm.normalise_county_name('1 Some Place, rsocommon'),  "1 some place, co_roscommon")
        self.assertEqual(nm.normalise_county_name('1 Some Place, roscmmon'),   "1 some place, co_roscommon")
        self.assertEqual(nm.normalise_county_name('1 Some Place, rocommon'),   "1 some place, co_roscommon")
        self.assertEqual(nm.normalise_county_name('1 Some Place, roscommmon'), "1 some place, co_roscommon")
        self.assertEqual(nm.normalise_county_name('1 Some Place, rosommon'),   "1 some place, co_roscommon")
        self.assertEqual(nm.normalise_county_name('1 Some Place, rodcommon'),  "1 some place, co_roscommon")
        self.assertEqual(nm.normalise_county_name('1 Some Place, rocsommon'),  "1 some place, co_roscommon")
        # = sligo
        self.assertEqual(nm.normalise_county_name('1 Some Place, slligo'),     "1 some place, co_sligo")
        self.assertEqual(nm.normalise_county_name('1 Some Place, sigo'),       "1 some place, co_sligo")
        # = tipperary
        self.assertEqual(nm.normalise_county_name('1 Some Place, tippeary'),   "1 some place, co_tipperary")
        self.assertEqual(nm.normalise_county_name('1 Some Place, tiperary'),   "1 some place, co_tipperary")
        self.assertEqual(nm.normalise_county_name('1 Some Place, tipparery'),  "1 some place, co_tipperary")
        self.assertEqual(nm.normalise_county_name('1 Some Place, tipperay'),   "1 some place, co_tipperary")
        self.assertEqual(nm.normalise_county_name('1 Some Place, tippperary'), "1 some place, co_tipperary")
        self.assertEqual(nm.normalise_county_name('1 Some Place, tipperaray'), "1 some place, co_tipperary")
        self.assertEqual(nm.normalise_county_name('1 Some Place, tipperatry'), "1 some place, co_tipperary")
        self.assertEqual(nm.normalise_county_name('1 Some Place, tippereary'), "1 some place, co_tipperary")
        # = waterford
        self.assertEqual(nm.normalise_county_name('1 Some Place, waterfod'),   "1 some place, co_waterford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, waterfird'),  "1 some place, co_waterford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, warerford'),  "1 some place, co_waterford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, waterfored'), "1 some place, co_waterford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, waterfotd'),  "1 some place, co_waterford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, waterord'),   "1 some place, co_waterford")
        # = westmeath
        self.assertEqual(nm.normalise_county_name('1 Some Place, wesrmeath'),     "1 some place, co_westmeath")
        self.assertEqual(nm.normalise_county_name('1 Some Place, westemeath'),    "1 some place, co_westmeath")
        self.assertEqual(nm.normalise_county_name('1 Some Place, weatmeath'),     "1 some place, co_westmeath")
        self.assertEqual(nm.normalise_county_name('1 Some Place, westmeth'),      "1 some place, co_westmeath")
        self.assertEqual(nm.normalise_county_name('1 Some Place, wetmeath'),      "1 some place, co_westmeath")
        self.assertEqual(nm.normalise_county_name('1 Some Place, west meath'),    "1 some place, co_westmeath")
        # = wexford
        self.assertEqual(nm.normalise_county_name('1 Some Place, wexvord'),     "1 some place, co_wexford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, wexfors'),     "1 some place, co_wexford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, wxford'),      "1 some place, co_wexford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, wexfor'),      "1 some place, co_wexford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, weford'),      "1 some place, co_wexford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, wexfor'),      "1 some place, co_wexford")
        self.assertEqual(nm.normalise_county_name('1 Some Place, wexfod'),      "1 some place, co_wexford")
        # = wexford
        self.assertEqual(nm.normalise_county_name('1 Some Place, wiclow'),      "1 some place, co_wicklow")
        self.assertEqual(nm.normalise_county_name('1 Some Place, wickow'),      "1 some place, co_wicklow")
        self.assertEqual(nm.normalise_county_name('1 Some Place, wiicklow'),    "1 some place, co_wicklow")
        self.assertEqual(nm.normalise_county_name('1 Some Place, wicklo'),      "1 some place, co_wicklow")

        # remove mistakes
        self.assertEqual(nm.normalise_county_name('1 Some Place, co'),          "1 some place")
        self.assertEqual(nm.normalise_county_name('1 Some Place, cork po'),     "1 some place, co_cork")
        # negative change
        self.assertEqual(nm.normalise_county_name('1 Some Place, the louth'),          "1 some place, the louth")
        self.assertEqual(nm.normalise_county_name('1 Some Place, via louth'),          "1 some place, via louth")


# outliers
# 1 blackthorne drive, belfield, ferrybank  via waterford
# Kilkenny	2 mullinabro woods, newrath, via waterford
# 20 st finbarrs park, glasheen rd, the louth
# 17 island villas, barony of uppercross, city of dublin



# 58 hanaville park, terenure, city of dublin

# 64 rosehill, newport, via limerick
# 922 st patricks park, celbridge, countuy kildare



if __name__ == '__main__':
    unittest.main()
