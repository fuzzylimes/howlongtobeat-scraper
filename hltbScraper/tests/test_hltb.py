from unittest import TestCase

from hltbScraper import scraper as hltb

class TestScraper(TestCase):
    def test_HLTB(self):
        title = 'Final Fantasy'
        a = hltb.HLTB(title)
        self.assertTrue(isinstance(a,dict))
        self.assertTrue(title in a.keys())
        self.assertTrue('url' in a[title].keys())
        self.assertTrue('Main Story' in a[title].keys())
        self.assertTrue('Main + Extra' in a[title].keys())
        self.assertTrue('Completionist' in a[title].keys())

    def test_HLTB_not_found(self):
        with self.assertRaises(Exception):
            title = 'asfkjasf'
            hltb.HLTB(title)

    def test_get_page(self):
        a = hltb.GetPage('Final Fantasy')
        self.assertTrue(isinstance(a, str))
