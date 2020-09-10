import unittest
import datetime
import model.attribute as attrs
import model


class TestExtractor(unittest.TestCase):
    def setUp(self):
        from extractor import RaceExtractor
        self.race_extractor = RaceExtractor(attrs, model)

    @unittest.skip('Seleniumを利用した重いテストのため')
    def test_fetch_race_id(self):
        race_id = self.race_extractor.fetch_race_id_list(
            datetime.date(2020, 8, 8))
        self.assertEqual('202004020501', race_id[0].attr)

    @unittest.skip('Seleniumを利用した重いテストのため')
    def test_fetch_race_data(self):
        race_id = '202004020501'
        race_data = self.race_extractor.fetch_race_data(attrs.RaceID(race_id))
        self.assertEqual(race_id, race_data.id.attr)
        self.assertEqual('新潟1R', race_data.name.attr)
        self.assertEqual('芝', race_data.field.attr)
        self.assertEqual(1600, race_data.distance.attr)
        self.assertEqual('雨', race_data.weather.attr)
        self.assertEqual('左', race_data.turn.attr)
        self.assertEqual('2018104971', race_data.horses[0].id.attr)
        self.assertEqual('コウソクカレン', race_data.horses[0].name.attr)
        self.assertEqual(1, race_data.horses[0].number.attr)
        self.assertEqual(11, race_data.horses[0].rank.attr)
        self.assertEqual(2, race_data.horses[0].age.attr)
        self.assertEqual(54.0, race_data.horses[0].load.attr)
        self.assertEqual(9.0, race_data.horses[0].odds.attr)
        self.assertEqual(496, race_data.horses[0].weight.attr)
        self.assertEqual(-2, race_data.horses[0].weight_change.attr)
