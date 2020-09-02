# -*- coding: utf-8 -*-
import unittest
import model.attribute as attrs


class TestModelAttribute(unittest.TestCase):
    def setUp(self):
        pass

    def test_id_create(self):
        id_ = attrs.ID(0)
        self.assertEqual(0, id_.attr)

    def test_name_create(self):
        name = attrs.Name('競走馬名')
        self.assertEqual('競走馬名', name.attr)

    def test_birthday_create(self):
        birthday = attrs.Birthday('2000年1月1日')
        self.assertEqual('2000年1月1日', birthday.attr)

    def test_weather_create(self):
        weather = attrs.Weather(0.5)
        self.assertEqual(0.5, weather.attr)

    def test_ground_create(self):
        ground = attrs.Ground(0)
        self.assertEqual(0, ground.attr)

    def test_distance_create(self):
        distance = attrs.Distance(200)
        self.assertEqual(200, distance.attr)

    def test_growth_create(self):
        growth = attrs.Growth(0.8)
        self.assertEqual(0.8, growth.attr)

    def test_limb_create(self):
        limb = attrs.Limb(0.8)
        self.assertEqual(0.8, limb.attr)

    def test_money_create(self):
        money = attrs.Money(200000)
        self.assertEqual(200000, money.attr)

    def test_suitability_create(self):
        suitabiliy = attrs.Suitability(0.8)
        self.assertEqual(0.8, suitabiliy.attr)

    def test_rank_average_create(self):
        rank_average = attrs.RankAverage(3.5)
        self.assertEqual(3.5, rank_average.attr)

    def test_speed_create(self):
        speed = attrs.Speed(20.7)
        self.assertEqual(20.7, speed.attr)

    def test_wins_create(self):
        wins = attrs.Wins(10)
        self.assertEqual(10, wins.attr)

    def test_win_rate_create(self):
        wins = attrs.WinRate(0.33)
        self.assertEqual(0.33, wins.attr)

    def test_sex_create(self):
        sex = attrs.Sex('牡')
        self.assertEqual('牡', sex.attr)
