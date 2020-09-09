import model.attribute as attrs


class AttrUtil:
    @classmethod
    def sample(self):
        return {
            'horse_id': '2018103973',
            'horse_name': 'アデウス',
            'jockey_id': '00666',
            'jockey_name': '武豊',
            'ped_id': '000a0124c7',
            'ped_name': 'シャンパンドーロ',
            'trainer_id': '01071',
            'trainer_name': '池江泰寿',
            'race_id': '202006040201',
            'race_name': '2歳未勝利',
            'date': '2018年4月2日',
            'sex': '牝',
            'wins': 10,
            'win_rate': 0.33,
            'rank_average': 3.5,
            'money': 200000,
            'limb': 0.8,
            'growth': 0.8,
            'speed': 20.7,
            'breeding_center': '新ひだか町',
            'course_suitability': 0.8,
            'distance_suitability': 0.8,
            'muddy_track_suitability': 0.8,
            'summer_suitability': 0.8,
            'winter_suitability': 0.8,
            'weather': '晴',
            'field': '芝',
            'turn': '右',
            'distance': 1200,
        }

    @classmethod
    def create_breeding_center(cls, val):
        return attrs.BreedingCenter(val)

    @classmethod
    def create_course_suitability(cls, val):
        return attrs.CourseSuitability(val)

    @classmethod
    def create_date(cls, val):
        return attrs.Date(val)

    @classmethod
    def create_distance(cls, val):
        return attrs.Distance(val)

    @classmethod
    def create_distance_suitability(cls, val):
        return attrs.DistanceSuitability(val)

    @classmethod
    def create_field(cls, val):
        return attrs.Field(val)

    @classmethod
    def create_growth(cls, val):
        return attrs.Growth(val)

    @classmethod
    def create_horse_id(cls, val):
        return attrs.HorseID(val)

    @classmethod
    def create_horses(cls, val):
        return attrs.Horses(val)

    @classmethod
    def create_id(cls, val):
        return attrs.ID(val)

    @classmethod
    def create_jockey_id(cls, val):
        return attrs.JockeyID(val)

    @classmethod
    def create_limb(cls, val):
        return attrs.Limb(val)

    @classmethod
    def create_money(cls, val):
        return attrs.Money(val)

    @classmethod
    def create_muddy_track_suitability(cls, val):
        return attrs.MuddyTrackSuitability(val)

    @classmethod
    def create_name(cls, val):
        return attrs.Name(val)

    @classmethod
    def create_ped_id(cls, val):
        return attrs.PedID(val)

    @classmethod
    def create_race_id(cls, val):
        return attrs.RaceID(val)

    @classmethod
    def create_race_prize(cls, val):
        return attrs.RacePrize(val)

    @classmethod
    def create_rank_average(cls, val):
        return attrs.RankAverage(val)

    @classmethod
    def create_sex(cls, val):
        return attrs.Sex(val)

    @classmethod
    def create_speed(cls, val):
        return attrs.Speed(val)

    @classmethod
    def create_suitability(cls, val):
        return attrs.Suitability(val)

    @classmethod
    def create_summer_suitability(cls, val):
        return attrs.SummerSuitability(val)

    @classmethod
    def create_trainer_id(cls, val):
        return attrs.TrainerID(val)

    @classmethod
    def create_turn(cls, val):
        return attrs.Turn(val)

    @classmethod
    def create_weather(cls, val):
        return attrs.Weather(val)

    @classmethod
    def create_win_rate(cls, val):
        return attrs.WinRate(val)

    @classmethod
    def create_wins(cls, val):
        return attrs.Wins(val)

    @classmethod
    def create_winter_suitability(cls, val):
        return attrs.WinterSuitability(val)
