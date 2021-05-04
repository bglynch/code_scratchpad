import unittest
from src import normalise as nm


class NormaliseTests(unittest.TestCase):
    def test_normalise_dublin_postcode(self):
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, dublin4'),        "1 some place, dublin_4")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, dublin 4'),       "1 some place, dublin_4")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, dublin  4'),      "1 some place, dublin_4")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, dublin 04'),      "1 some place, dublin_4")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, dublin 14'),      "1 some place, dublin_14")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, dublin 6w'),      "1 some place, dublin_6w")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, dublin 6 west'),  "1 some place, dublin_6w")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, dublin. 15'),     "1 some place, dublin_15")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, dublin 15.'),     "1 some place, dublin_15")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, d9'),             "1 some place, dublin_9")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, d 15'),           "1 some place, dublin_15")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, d/15'),           "1 some place, dublin_15")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, d.15'),           "1 some place, dublin_15")
        self.assertEqual(nm.normalise_dublin_postcode('1 some place, d. 15'),          "1 some place, dublin_15")
        self.assertEqual(nm.normalise_dublin_postcode('1 place dublin 10, dublin 10'), "1 place, dublin_10")
        self.assertEqual(nm.normalise_dublin_postcode('1 place dublin 10, town'),      "1 place, dublin_10, town")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, towndublin 6'),        "1 place, town, dublin_6")
        # no change test
        self.assertEqual(nm.normalise_dublin_postcode('apt 58, block d2, town'),       "apt 58, block d2, town")
        self.assertEqual(nm.normalise_dublin_postcode('apt d4, harvey dock, youghal'), "apt d4, harvey dock, youghal")
        self.assertEqual(nm.normalise_dublin_postcode('apartment d4, youghal'),        "apartment d4, youghal")
        self.assertEqual(nm.normalise_dublin_postcode('place, apt d07 student accom'), "place, apt d07 student accom")
        self.assertEqual(nm.normalise_dublin_postcode('apt   d4, corm apts, foxford'), "apt d4, corm apts, foxford")
        self.assertEqual(nm.normalise_dublin_postcode('d2, cornmullen, fooxford'),     "d2, cornmullen, fooxford")
        self.assertEqual(nm.normalise_dublin_postcode('51/d2 woodfield grove'),        "51/d2 woodfield grove")
        # bad spellings
        self.assertEqual(nm.normalise_dublin_postcode('1 place, bublin 6'),  "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dbulin 6'),  "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, diblin 6'),  "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, diblin 6'),  "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dubiln 6'),  "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dubin 6'),   "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dublbin 6'), "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dubli 6'),   "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dublini 6'), "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dublinn 6'), "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dubllin 6'), "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dubln 6'),   "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dublni 6'),  "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, duboin 6'),  "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dulbin 6'),  "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dulin 6'),   "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dunlin 6'),  "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dunlin6'),   "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dublihn 6'), "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dubkin 6'),  "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dublihn 6'), "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, ddublin 6'), "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dubline 6'), "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dyublin 6'), "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dyublin 6'), "1 place, dublin_6")
        self.assertEqual(nm.normalise_dublin_postcode('1 place, dubglin 6'), "1 place, dublin_6")

    def test_normalise_county(self):
        self.assertEqual(nm.normalise_county('1 Some Place, co cork'),    "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place, co. cork'),   "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place, co . cork'),  "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place, co; cork'),   "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place, co: cork'),   "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place, co.cork'),    "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place co cork'),     "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place  co cork'),    "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place county cork'), "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place countycork'),  "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place  cork'),       "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place  cork.'),      "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place, cork'),       "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('coast rd, fountainstownco cork'), "coast rd, fountainstown, co_cork")
        # part of a county
        self.assertEqual(nm.normalise_county('1 Some Place, west cork'),        "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place, nr cork'),          "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place, near cork'),        "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place, near cork city'),   "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place, north dublin'),     "1 some place, co_dublin")
        self.assertEqual(nm.normalise_county('1 Some Place, north tipperary'),  "1 some place, co_tipperary")
        self.assertEqual(nm.normalise_county('1 Some Place, south tipperary'),  "1 some place, co_tipperary")
        self.assertEqual(nm.normalise_county('1 some place, city of dublin'),   "1 some place, co_dublin")
        # county at end of address
        self.assertEqual(nm.normalise_county('1 Some Place tipperary'),    "1 some place, co_tipperary")
        # remove mistakes
        self.assertEqual(nm.normalise_county('1 Some Place, co'),          "1 some place")
        self.assertEqual(nm.normalise_county('1 Some Place, cork po'),     "1 some place, co_cork")
        self.assertEqual(nm.normalise_county('1 Some Place, port laois'),  "1 some place, portlaoise")
        self.assertEqual(nm.normalise_county('1 Some Place, port laoise'), "1 some place, portlaoise")
        # negative change
        self.assertEqual(nm.normalise_county('1 Some Place, the louth'),   "1 some place, the louth")
        self.assertEqual(nm.normalise_county('1 Some Place, via louth'),   "1 some place, via louth")

    def test_normalise_county_prefix_spelling(self):
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, ci cork'),      "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, cp cork'),      "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, clo cork'),     "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, col cork'),     "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, ci cork'),      "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, cd cork'),      "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, ci cork'),      "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, c cork'),       "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, c0. cork'),     "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, cco. cork'),    "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, o cork'),       "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, cointy cork'),  "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, ccunty cork'),  "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, cunty cork'),   "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, couty cork'),   "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, couny cork'),   "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, count cork'),   "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, coutny cork'),  "1 some place, county cork")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 some place, countuy cork'), "1 some place, county cork")
        # negative
        self.assertEqual(nm.normalise_county_prefix_spelling('1 place, old dublin road'),   "1 place, old dublin road")
        self.assertEqual(nm.normalise_county_prefix_spelling('1 place, i f s c dublin 1'),   "1 place, ifsc, dublin 1")

    def test_normalise_county_spelling(self):
        # = cork
        self.assertEqual(nm.normalise_county_spelling('1 some place, corl'),     "1 some place, cork")
        self.assertEqual(nm.normalise_county_spelling('1 some place, cokr'),     "1 some place, cork")
        self.assertEqual(nm.normalise_county_spelling('1 some place, crok'),     "1 some place, cork")
        self.assertEqual(nm.normalise_county_spelling('1 some place, coork'),     "1 some place, cork")
        # = donegal
        self.assertEqual(nm.normalise_county_spelling('1 some place, dongal'),      "1 some place, donegal")
        self.assertEqual(nm.normalise_county_spelling('1 some place, doengal'),     "1 some place, donegal")
        self.assertEqual(nm.normalise_county_spelling('1 some place, donegak'),     "1 some place, donegal")
        # = dublin
        self.assertEqual(nm.normalise_county_spelling('1 some place, dubblin'),    "1 some place, dublin")
        self.assertEqual(nm.normalise_county_spelling('1 some place, dubin'),      "1 some place, dublin")
        self.assertEqual(nm.normalise_county_spelling('1 some place, dubliln'),    "1 some place, dublin")
        self.assertEqual(nm.normalise_county_spelling('1 some place, dublibn'),    "1 some place, dublin")
        self.assertEqual(nm.normalise_county_spelling('1 some place, dublibn'),    "1 some place, dublin")
        self.assertEqual(nm.normalise_county_spelling('1 some place, dubllin'),    "1 some place, dublin")
        self.assertEqual(nm.normalise_county_spelling('1 some place, dublni'),     "1 some place, dublin")
        self.assertEqual(nm.normalise_county_spelling('1 some place, dubiln'),     "1 some place, dublin")
        self.assertEqual(nm.normalise_county_spelling('1 some place, dulbin'),     "1 some place, dublin")
        # = galway
        self.assertEqual(nm.normalise_county_spelling('1 some place, galwyay'),     "1 some place, galway")
        self.assertEqual(nm.normalise_county_spelling('1 some place, galwy'),       "1 some place, galway")
        self.assertEqual(nm.normalise_county_spelling('1 some place, galwat'),      "1 some place, galway")
        self.assertEqual(nm.normalise_county_spelling('1 some place, galwa'),       "1 some place, galway")
        self.assertEqual(nm.normalise_county_spelling('1 some place, glaway'),      "1 some place, galway")
        self.assertEqual(nm.normalise_county_spelling('1 some place, glaway'),      "1 some place, galway")
        # = kildare
        self.assertEqual(nm.normalise_county_spelling('1 some place, kidare'),      "1 some place, kildare")
        self.assertEqual(nm.normalise_county_spelling('1 some place, kidlare'),     "1 some place, kildare")
        self.assertEqual(nm.normalise_county_spelling('1 some place, kildae'),      "1 some place, kildare")
        self.assertEqual(nm.normalise_county_spelling('1 some place, kildard'),     "1 some place, kildare")
        self.assertEqual(nm.normalise_county_spelling('1 some place, kilfdare'),    "1 some place, kildare")
        self.assertEqual(nm.normalise_county_spelling('1 some place, kiildare'),    "1 some place, kildare")
        self.assertEqual(nm.normalise_county_spelling('1 some place, kldare'),      "1 some place, kildare")
        # = kilkenny
        self.assertEqual(nm.normalise_county_spelling('1 some place, kikenny'),      "1 some place, kilkenny")
        self.assertEqual(nm.normalise_county_spelling('1 some place, kilkennny'),    "1 some place, kilkenny")
        self.assertEqual(nm.normalise_county_spelling('1 some place, killkenny'),    "1 some place, kilkenny")
        self.assertEqual(nm.normalise_county_spelling('1 some place, kilkennt'),     "1 some place, kilkenny")
        # = laois
        self.assertEqual(nm.normalise_county_spelling('1 some place, loais'),        "1 some place, laois")
        # = leitrim
        self.assertEqual(nm.normalise_county_spelling('1 some place, leirim'),      "1 some place, leitrim")
        self.assertEqual(nm.normalise_county_spelling('1 some place, letrim'),      "1 some place, leitrim")
        # = leitrim
        self.assertEqual(nm.normalise_county_spelling('1 some place, limerck'),      "1 some place, limerick")
        self.assertEqual(nm.normalise_county_spelling('1 some place, limericfk'),    "1 some place, limerick")
        self.assertEqual(nm.normalise_county_spelling('1 some place, lmerick'),      "1 some place, limerick")
        self.assertEqual(nm.normalise_county_spelling('1 some place, limrick'),      "1 some place, limerick")
        # = leitrim
        self.assertEqual(nm.normalise_county_spelling('1 some place, lonford'),      "1 some place, longford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, longfors'),     "1 some place, longford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, longofrd'),     "1 some place, longford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, longfod'),      "1 some place, longford")
        # = louth
        self.assertEqual(nm.normalise_county_spelling('1 some place, lough'),      "1 some place, louth")
        self.assertEqual(nm.normalise_county_spelling('1 some place, lout'),       "1 some place, louth")
        self.assertEqual(nm.normalise_county_spelling('1 some place, lourth'),     "1 some place, louth")
        # = mayo
        self.assertEqual(nm.normalise_county_spelling('1 some place, mmyo'),      "1 some place, mayo")
        self.assertEqual(nm.normalise_county_spelling('1 some place, moyo'),      "1 some place, mayo")
        self.assertEqual(nm.normalise_county_spelling('1 some place, maro'),      "1 some place, mayo")
        self.assertEqual(nm.normalise_county_spelling('1 some place, mayy'),      "1 some place, mayo")
        self.assertEqual(nm.normalise_county_spelling('1 some place, may'),       "1 some place, mayo")
        # = mayo
        self.assertEqual(nm.normalise_county_spelling('1 some place, maeth'),      "1 some place, meath")
        self.assertEqual(nm.normalise_county_spelling('1 some place, meah'),       "1 some place, meath")
        self.assertEqual(nm.normalise_county_spelling('1 some place, meth'),       "1 some place, meath")
        # = monaghan
        self.assertEqual(nm.normalise_county_spelling('1 some place, monagha'),    "1 some place, monaghan")
        self.assertEqual(nm.normalise_county_spelling('1 some place, mongaghan'),  "1 some place, monaghan")
        self.assertEqual(nm.normalise_county_spelling('1 some place, monoghan'),   "1 some place, monaghan")
        self.assertEqual(nm.normalise_county_spelling('1 some place, monagan'),    "1 some place, monaghan")
        self.assertEqual(nm.normalise_county_spelling('1 some place, managhan'),   "1 some place, monaghan")
        self.assertEqual(nm.normalise_county_spelling('1 some place, monaghn'),    "1 some place, monaghan")
        # = offaly
        self.assertEqual(nm.normalise_county_spelling('1 some place, offay'),      "1 some place, offaly")
        self.assertEqual(nm.normalise_county_spelling('1 some place, offally'),    "1 some place, offaly")
        # = roscommon
        self.assertEqual(nm.normalise_county_spelling('1 some place, rosscommon'), "1 some place, roscommon")
        self.assertEqual(nm.normalise_county_spelling('1 some place, rsocommon'),  "1 some place, roscommon")
        self.assertEqual(nm.normalise_county_spelling('1 some place, roscmmon'),   "1 some place, roscommon")
        self.assertEqual(nm.normalise_county_spelling('1 some place, rocommon'),   "1 some place, roscommon")
        self.assertEqual(nm.normalise_county_spelling('1 some place, roscommmon'), "1 some place, roscommon")
        self.assertEqual(nm.normalise_county_spelling('1 some place, rosommon'),   "1 some place, roscommon")
        self.assertEqual(nm.normalise_county_spelling('1 some place, rodcommon'),  "1 some place, roscommon")
        self.assertEqual(nm.normalise_county_spelling('1 some place, rocsommon'),  "1 some place, roscommon")
        # = sligo
        self.assertEqual(nm.normalise_county_spelling('1 some place, slligo'),     "1 some place, sligo")
        self.assertEqual(nm.normalise_county_spelling('1 some place, sigo'),       "1 some place, sligo")
        # = tipperary
        self.assertEqual(nm.normalise_county_spelling('1 some place, tippeary'),   "1 some place, tipperary")
        self.assertEqual(nm.normalise_county_spelling('1 some place, tiperary'),   "1 some place, tipperary")
        self.assertEqual(nm.normalise_county_spelling('1 some place, tipparery'),  "1 some place, tipperary")
        self.assertEqual(nm.normalise_county_spelling('1 some place, tipperay'),   "1 some place, tipperary")
        self.assertEqual(nm.normalise_county_spelling('1 some place, tippperary'), "1 some place, tipperary")
        self.assertEqual(nm.normalise_county_spelling('1 some place, tipperaray'), "1 some place, tipperary")
        self.assertEqual(nm.normalise_county_spelling('1 some place, tipperatry'), "1 some place, tipperary")
        self.assertEqual(nm.normalise_county_spelling('1 some place, tippereary'), "1 some place, tipperary")
        # = waterford
        self.assertEqual(nm.normalise_county_spelling('1 some place, waterfod'),   "1 some place, waterford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, waterfird'),  "1 some place, waterford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, warerford'),  "1 some place, waterford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, waterfored'), "1 some place, waterford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, waterfotd'),  "1 some place, waterford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, waterord'),   "1 some place, waterford")
        # = westmeath
        self.assertEqual(nm.normalise_county_spelling('1 some place, wesrmeath'),     "1 some place, westmeath")
        self.assertEqual(nm.normalise_county_spelling('1 some place, westemeath'),    "1 some place, westmeath")
        self.assertEqual(nm.normalise_county_spelling('1 some place, weatmeath'),     "1 some place, westmeath")
        self.assertEqual(nm.normalise_county_spelling('1 some place, westmeth'),      "1 some place, westmeath")
        self.assertEqual(nm.normalise_county_spelling('1 some place, wetmeath'),      "1 some place, westmeath")
        self.assertEqual(nm.normalise_county_spelling('1 some place, west meath'),    "1 some place, westmeath")
        # = wexford
        self.assertEqual(nm.normalise_county_spelling('1 some place, wexvord'),     "1 some place, wexford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, wexfors'),     "1 some place, wexford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, wxford'),      "1 some place, wexford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, wexfor'),      "1 some place, wexford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, weford'),      "1 some place, wexford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, wexfor'),      "1 some place, wexford")
        self.assertEqual(nm.normalise_county_spelling('1 some place, wexfod'),      "1 some place, wexford")
        # = wexford
        self.assertEqual(nm.normalise_county_spelling('1 some place, wiclow'),      "1 some place, wicklow")
        self.assertEqual(nm.normalise_county_spelling('1 some place, wickow'),      "1 some place, wicklow")
        self.assertEqual(nm.normalise_county_spelling('1 some place, wiicklow'),    "1 some place, wicklow")
        self.assertEqual(nm.normalise_county_spelling('1 some place, wicklo'),      "1 some place, wicklow")


if __name__ == '__main__':
    unittest.main()
