import model


class ModelUtil:
    @classmethod
    def create_horse(cls, attrs):
        return model.Horse(
            id_=attrs.create_horse_id(attrs.sample()['horse_id']),
            name=attrs.create_name(attrs.sample()['horse_name']),
            birthday=attrs.create_date(attrs.sample()['date']),
            sex=attrs.create_sex(attrs.sample()['sex']),
            ped_id=attrs.create_ped_id(attrs.sample()['ped_id']),
            trainer_id=attrs.create_trainer_id(attrs.sample()['trainer_id']),
            wins=attrs.create_wins(attrs.sample()['wins']),
            win_rate=attrs.create_win_rate(attrs.sample()['win_rate']),
            rank_average=attrs.create_rank_average(
                attrs.sample()['rank_average']),
            money=attrs.create_money(attrs.sample()['money']),
            limb=attrs.create_limb(attrs.sample()['limb']),
            growth=attrs.create_growth(attrs.sample()['growth']),
            speed=attrs.create_speed(attrs.sample()['speed']),
            breeding_center=attrs.create_breeding_center(
                attrs.sample()['breeding_center']),
            course_suitability=attrs.create_course_suitability(
                attrs.sample()['course_suitability']),
            distance_suitability=attrs.create_distance_suitability(
                attrs.sample()['distance_suitability']),
            muddy_track_suitability=attrs.create_muddy_track_suitability(
                attrs.sample()['muddy_track_suitability']),
            summer_suitability=attrs.create_summer_suitability(
                attrs.sample()['summer_suitability']),
            winter_suitability=attrs.create_winter_suitability(
                attrs.sample()['winter_suitability']),
        )

    @classmethod
    def create_jockey(cls, attrs):
        return model.Jockey(
            id_=attrs.create_jockey_id(attrs.sample()['jockey_id']),
            name=attrs.create_name(attrs.sample()['jockey_name']),
            win_rate=attrs.create_win_rate(attrs.sample()['win_rate']),
            rank_average=attrs.create_rank_average(
                attrs.sample()['rank_average']),
        )

    @classmethod
    def create_ped(cls, attrs):
        return model.Ped(
            id_=attrs.create_ped_id(attrs.sample()['ped_id']),
            name=attrs.create_name(attrs.sample()['ped_name']),
            win_rate=attrs.create_win_rate(attrs.sample()['win_rate']),
            rank_average=attrs.create_rank_average(
                attrs.sample()['rank_average']),
        )

    @classmethod
    def create_trainer(cls, attrs):
        return model.Trainer(
            id_=attrs.create_trainer_id(attrs.sample()['trainer_id']),
            name=attrs.create_name(attrs.sample()['trainer_name']),
            win_rate=attrs.create_win_rate(attrs.sample()['win_rate']),
            rank_average=attrs.create_rank_average(
                attrs.sample()['rank_average']),
        )

    @classmethod
    def create_race(cls, attrs):
        return model.Race(
            id_=attrs.create_race_id(attrs.sample()['race_id']),
            name=attrs.create_name(attrs.sample()['race_name']),
            date=attrs.create_date(attrs.sample()['date']),
            weather=attrs.create_weather(attrs.sample()['weather']),
            field=attrs.create_field(attrs.sample()['field']),
            turn=attrs.create_turn(attrs.sample()['turn']),
            distance=attrs.create_distance(attrs.sample()['distance']),
            prize=attrs.create_race_prize(
                [attrs.create_money(400000) for i in range(5)]),
            horses=[cls.create_race_horse(attrs) for i in range(18)],
        )

    @classmethod
    def create_race_horse(cls, attrs):
        return model.RaceHorse(
            id_=attrs.create_horse_id(attrs.sample()['horse_id']),
            name=attrs.create_name(attrs.sample()['horse_name']),
            number=attrs.create_number(attrs.sample()['number']),
            rank=attrs.create_rank(attrs.sample()['rank']),
            age=attrs.create_age(attrs.sample()['age']),
            load=attrs.create_load(attrs.sample()['load']),
            odds=attrs.create_odds(attrs.sample()['odds']),
            weight=attrs.create_weight(attrs.sample()['weight']),
            weight_change=attrs.create_weight_change(
                attrs.sample()['weight_change']),
        )
