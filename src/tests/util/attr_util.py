import model.attribute as attrs


class AttrUtil:
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
    def create_id(cls, val):
        return attrs.ID(val)

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
