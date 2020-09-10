import unittest
import datetime
import model.attribute as attrs


class TestExtractor(unittest.TestCase):
    def setUp(self):
        from extractor import RaceExtractor
        self.race_extractor = RaceExtractor(attrs)

    @unittest.skip('Seleniumを利用した重いテストのため')
    def test_fetch_race_id(self):
        race_id = self.race_extractor.fetch_race_id_list(
            datetime.date(2020, 8, 8))
        self.assertEqual('202004020501', race_id[0].attr)

    @unittest.skip('Seleniumを利用した重いテストのため')
    def test_fetch_race_data(self):
        race_id = '202004020501'
        race_data = self.race_extractor.fetch_race_data(attrs.RaceID(race_id))
        self.assertEqual(race_id, race_data['レースID'].attr)
        self.assertEqual('2歳未勝利', race_data['レース名'].attr)
        self.assertEqual('芝', race_data['馬場状態'].attr)
        self.assertEqual(1600, race_data['走距離'].attr)
        self.assertEqual('雨', race_data['天気'].attr)
        self.assertEqual('左', race_data['周回方向'].attr)
        self.assertEqual('コウソクカレン', race_data['競走馬'][0]['馬名'])
        self.assertEqual(11, race_data['競走馬'][0]['着順'])
        self.assertEqual(1, race_data['競走馬'][0]['馬番'])
        self.assertEqual('牝', race_data['競走馬'][0]['性別'])
        self.assertEqual(2, race_data['競走馬'][0]['年齢'])
        self.assertEqual(54.0, race_data['競走馬'][0]['斤量'])
        self.assertEqual(9.0, race_data['競走馬'][0]['オッズ'])
        self.assertEqual(496, race_data['競走馬'][0]['体重'])
        self.assertEqual(-2, race_data['競走馬'][0]['体重増減'])
