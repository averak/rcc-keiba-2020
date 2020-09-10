import unittest
import datetime
import model.attribute as attrs
from extractor import RaceExtractor


class TestPostTextBuilder(unittest.TestCase):
    def setUp(self):
        self.race_extractor = RaceExtractor(attrs.RaceID)

    @unittest.skip('Seleniumを利用した重いテストのため')
    def test_fetch_race_id(self):
        race_id = self.race_extractor.fetch_race_id_list(datetime.date(2020, 8, 8))
        self.assertEqual('202004020501', race_id[0].attr)
