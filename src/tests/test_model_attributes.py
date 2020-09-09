import unittest
import model.attribute as attrs
from util.attr_util import AttrUtil
from util.model_util import ModelUtil


class TestModelAttribute(unittest.TestCase):
    def setUp(self):
        self.sample = self.attrs.sample()

    @property
    def attrs(self):
        return AttrUtil

    def test_breeding_center(self):
        attr = self.attrs.create_breeding_center(
            self.sample['breeding_center'])
        self.assertEqual(self.sample['breeding_center'], attr.attr)

    def test_course_suitability(self):
        attr = self.attrs.create_course_suitability(
            self.sample['course_suitability'])
        self.assertEqual(self.sample['course_suitability'], attr.attr)

    def test_date(self):
        attr = self.attrs.create_date(self.sample['date'])
        self.assertEqual(self.sample['date'], attr.attr)

    def test_distance(self):
        attr = self.attrs.create_distance(self.sample['distance'])
        self.assertEqual(self.sample['distance'], attr.attr)

    def test_distance_suitability(self):
        attr = self.attrs.create_distance_suitability(
            self.sample['distance_suitability'])
        self.assertEqual(self.sample['distance_suitability'], attr.attr)

    def test_field(self):
        attr = self.attrs.create_field(self.sample['field'])
        self.assertEqual(self.sample['field'], attr.attr)

    def test_growth(self):
        attr = self.attrs.create_growth(self.sample['growth'])
        self.assertEqual(self.sample['growth'], attr.attr)

    def test_horse_id(self):
        attr = self.attrs.create_horse_id(self.sample['horse_id'])
        self.assertEqual(self.sample['horse_id'], attr.attr)

    def test_jockey_id(self):
        attr = self.attrs.create_jockey_id(self.sample['jockey_id'])
        self.assertEqual(self.sample['jockey_id'], attr.attr)

    def test_limb(self):
        attr = self.attrs.create_limb(self.sample['limb'])
        self.assertEqual(self.sample['limb'], attr.attr)

    def test_money(self):
        attr = self.attrs.create_money(self.sample['money'])
        self.assertEqual(self.sample['money'], attr.attr)

    def test_muddy_track_suitability(self):
        attr = self.attrs.create_muddy_track_suitability(
            self.sample['muddy_track_suitability'])
        self.assertEqual(self.sample['muddy_track_suitability'], attr.attr)

    def test_name(self):
        attr = self.attrs.create_name(self.sample['horse_name'])
        self.assertEqual(self.sample['horse_name'], attr.attr)

    def test_ped_id(self):
        attr = self.attrs.create_ped_id(self.sample['ped_id'])
        self.assertEqual(self.sample['ped_id'], attr.attr)

    def test_race_id(self):
        attr = self.attrs.create_race_id(self.sample['race_id'])
        self.assertEqual(self.sample['race_id'], attr.attr)

    def test_race_prize(self):
        race_prize = [
            self.attrs.create_money(400000)
            for i in range(5)
        ]
        attr = self.attrs.create_race_prize(race_prize)
        self.assertEqual('40,40,40,40,40万円', str(attr))

    def test_rank_average(self):
        attr = self.attrs.create_rank_average(self.sample['rank_average'])
        self.assertEqual(self.sample['rank_average'], attr.attr)

    def test_sex(self):
        attr = self.attrs.create_sex(self.sample['sex'])
        self.assertEqual(self.sample['sex'], attr.attr)

    def test_speed(self):
        attr = self.attrs.create_speed(self.sample['speed'])
        self.assertEqual(self.sample['speed'], attr.attr)

    def test_summer_suitability(self):
        attr = self.attrs.create_summer_suitability(self.sample['summer_suitability'])
        self.assertEqual(self.sample['summer_suitability'], attr.attr)

    def test_trainer_id(self):
        attr = self.attrs.create_trainer_id(self.sample['trainer_id'])
        self.assertEqual(self.sample['trainer_id'], attr.attr)

    def test_turn(self):
        attr = self.attrs.create_turn(self.sample['turn'])
        self.assertEqual(self.sample['turn'], attr.attr)

    def test_weather(self):
        attr = self.attrs.create_weather(self.sample['weather'])
        self.assertEqual(self.sample['weather'], attr.attr)

    def test_win_rate(self):
        attr = self.attrs.create_win_rate(self.sample['win_rate'])
        self.assertEqual(self.sample['win_rate'], attr.attr)

    def test_wins(self):
        attr = self.attrs.create_wins(self.sample['wins'])
        self.assertEqual(self.sample['wins'], attr.attr)

    def test_winter_suitability(self):
        attr = self.attrs.create_winter_suitability(self.sample['winter_suitability'])
        self.assertEqual(self.sample['winter_suitability'], attr.attr)
