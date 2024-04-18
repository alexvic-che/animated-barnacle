import unittest
from city_function import Gorod_Strana as GS

class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = GS('santiago', 'chili')
        self.assertEquals(formatted_name, "Santiago, Chili")

if __name__== "__main__":
    unittest.main()
