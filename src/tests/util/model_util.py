# -*- coding: utf-8 -*-
import model


class ModelUtil:
    @classmethod
    def create_horse(cls, attrs):
        return model.Horse(
            id_=attrs.id,
            name=attrs.name,
            birthday=attrs.birthday,
            sex=attrs.sex,
            ped_id=attrs.ped_id,
            trainer_id=attrs.trainer_id,
            wins=attrs.wins,
            win_rate=attrs.win_rate,
            rank_average=attrs.rank_average,
            money=attrs.money,
            limb=attrs.limb,
            growth=attrs.growth,
            speed=attrs.speed,
            breeding_center=attrs.breeding_center,
            course_suitability=attrs.course_suitability,
            distance_suitability=attrs.distance_suitability,
            muddy_track_suitability=attrs.muddy_track_suitability,
            summer_suitability=attrs.summer_suitability,
            winter_suitability=attrs.winter_suitability,
        )

    @classmethod
    def create_jockey(cls, attrs):
        return model.Jockey(
            id_=attrs.id,
            name=attrs.name,
            win_rate=attrs.win_rate,
            rank_average=attrs.rank_average,
        )
