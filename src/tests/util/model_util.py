# -*- coding: utf-8 -*-
import model


class ModelUtil:
    @classmethod
    def create_horse(cls, attrs):
        return model.Horse(
            id_=attrs.create_id(0),
            name=attrs.create_name('競走馬名'),
            birthday=attrs.create_birthday('2000年1月1日'),
            sex=attrs.create_sex('牡'),
            ped_id=attrs.create_ped_id(0),
            trainer_id=attrs.create_trainer_id(0),
            wins=attrs.create_wins(10),
            win_rate=attrs.create_win_rate(0.33),
            rank_average=attrs.create_rank_average(3.5),
            money=attrs.create_money(200000),
            limb=attrs.create_limb(0.8),
            growth=attrs.create_growth(0.8),
            speed=attrs.create_speed(20.7),
            breeding_center=attrs.create_breeding_center('産地名'),
            course_suitability=attrs.create_course_suitability(0.8),
            distance_suitability=attrs.create_distance_suitability(0.8),
            muddy_track_suitability=attrs.create_muddy_track_suitability(0.8),
            summer_suitability=attrs.create_summer_suitability(0.8),
            winter_suitability=attrs.create_winter_suitability(0.8),
        )

    @classmethod
    def create_jockey(cls, attrs):
        return model.Jockey(
            id_=attrs.create_id(0),
            name=attrs.create_name('騎手名'),
            win_rate=attrs.create_win_rate(0.33),
            rank_average=attrs.create_rank_average(3.5),
        )

    @classmethod
    def create_ped(cls, attrs):
        return model.Ped(
            id_=attrs.create_id(0),
            name=attrs.create_name('血統名'),
            win_rate=attrs.create_win_rate(0.33),
            rank_average=attrs.create_rank_average(3.5),
        )

    @classmethod
    def create_trainer(cls, attrs):
        return model.Trainer(
            id_=attrs.create_id(0),
            name=attrs.create_name('調教師名'),
            win_rate=attrs.create_win_rate(0.33),
            rank_average=attrs.create_rank_average(3.5),
        )
