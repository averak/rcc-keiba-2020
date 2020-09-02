# -*- coding: utf-8 -*-
import model.attribute as attrs


class AttrUtil:
    id = attrs.ID(0)
    name = attrs.Name('名前')
    birthday = attrs.Birthday('2000年1月1日')
    sex = attrs.Sex('牡')
    ped_id = None
    trainer_id = None
    wins = attrs.Wins(10)
    win_rate = attrs.WinRate(0.33)
    rank_average = attrs.RankAverage(3.5)
    money = attrs.Money(200000)
    limb = attrs.Limb(0.8)
    growth = attrs.Growth(0.8)
    speed = attrs.Speed(20.7)
    breeding_center = None
    course_suitability = None
    distance_suitability = None
    muddy_track_suitability = None
    summer_suitability = None
    winter_suitability = None
