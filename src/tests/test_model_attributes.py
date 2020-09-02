# -*- coding: utf-8 -*-
import unittest
import model.attribute as attrs
from util.attr_util import AttrUtil


class TestModelAttribute(unittest.TestCase):
    def setUp(self):
        pass

    def attrs(self):
        return AttrUtil

    def test_birthday(self):
        attr = self.attrs().create_birthday('2000年1月1日')
        self.assertEqual('2000年1月1日', attr.attr)

    def test_breeding_center(self):
        attr = self.attrs().create_breeding_center('産地名')
        self.assertEqual('産地名', attr.attr)

    def test_course_suitability(self):
        attr = self.attrs().create_course_suitability(0.8)
        self.assertEqual(0.8, attr.attr)

    def test_distance(self):
        attr = self.attrs().create_distance(200)
        self.assertEqual(200, attr.attr)

    def test_distance_suitability(self):
        attr = self.attrs().create_distance_suitability(0.8)
        self.assertEqual(0.8, attr.attr)

    def test_ground(self):
        attr = self.attrs().create_ground('ダート')
        self.assertEqual('ダート', attr.attr)

    def test_growth(self):
        attr = self.attrs().create_growth(0.8)
        self.assertEqual(0.8, attr.attr)

    def test_id(self):
        attr = self.attrs().create_id(0)
        self.assertEqual(0, attr.attr)

    def test_limb(self):
        attr = self.attrs().create_limb(0.8)
        self.assertEqual(0.8, attr.attr)

    def test_money(self):
        attr = self.attrs().create_money(200000)
        self.assertEqual(200000, attr.attr)

    def test_muddy_track_suitability(self):
        attr = self.attrs().create_muddy_track_suitability(0.8)
        self.assertEqual(0.8, attr.attr)

    def test_name(self):
        attr = self.attrs().create_name('名前')
        self.assertEqual('名前', attr.attr)

    def test_ped_id(self):
        attr = self.attrs().create_ped_id(0)
        self.assertEqual(0, attr.attr)

    def test_rank_average(self):
        attr = self.attrs().create_rank_average(3.5)
        self.assertEqual(3.5, attr.attr)

    def test_sex(self):
        attr = self.attrs().create_sex('牡')
        self.assertEqual('牡', attr.attr)

    def test_speed(self):
        attr = self.attrs().create_speed(20.7)
        self.assertEqual(20.7, attr.attr)

    def test_suitability(self):
        attr = self.attrs().create_suitability(0.8)
        self.assertEqual(0.8, attr.attr)

    def test_summer_suitability(self):
        attr = self.attrs().create_summer_suitability(0.8)
        self.assertEqual(0.8, attr.attr)

    def test_trainer_id(self):
        attr = self.attrs().create_trainer_id(0)
        self.assertEqual(0, attr.attr)

    def test_weather(self):
        attr = self.attrs().create_weather('晴')
        self.assertEqual('晴', attr.attr)

    def test_win_rate(self):
        attr = self.attrs().create_win_rate(0.33)
        self.assertEqual(0.33, attr.attr)

    def test_wins(self):
        attr = self.attrs().create_wins(10)
        self.assertEqual(10, attr.attr)

    def test_winter_suitability(self):
        attr = self.attrs().create_winter_suitability(0.8)
        self.assertEqual(0.8, attr.attr)
