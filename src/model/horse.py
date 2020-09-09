from . import model


class Horse(model.Model):
    def _hook_create(self, config):
        self.__name = config['name']
        self.__date = config['date']
        self.__sex = config['sex']
        self.__ped_id = config['ped_id']
        self.__trainer_id = config['trainer_id']
        self.__wins = config['wins']
        self.__win_rate = config['win_rate']
        self.__rank_average = config['rank_average']
        self.__money = config['money']
        self.__limb = config['limb']
        self.__growth = config['growth']
        self.__speed = config['speed']
        self.__breeding_center = config['breeding_center']
        self.__course_suitability = config['course_suitability']
        self.__distance_suitability = config['distance_suitability']
        self.__muddy_track_suitability = config['muddy_track_suitability']
        self.__summer_suitability = config['summer_suitability']
        self.__winter_suitability = config['winter_suitability']

    @property
    def name(self):
        return self.__name.attr

    @property
    def birthday(self):
        return self.__birthday.attr

    @property
    def sex(self):
        return self.__sex.attr

    @property
    def ped_id(self):
        return self.__ped_id.attr

    @property
    def trainer_id(self):
        return self.__trainer_id.attr

    @property
    def wins(self):
        return self.__wins.attr

    @property
    def win_rate(self):
        return self.__win_rate.attr

    @property
    def rank_average(self):
        return self.__rank_average.attr

    @property
    def money(self):
        return self.__money.attr

    @property
    def limb(self):
        return self.__limb.attr

    @property
    def growth(self):
        return self.__growth.attr

    @property
    def speed(self):
        return self.__speed.attr

    @property
    def breeding_center(self):
        return self.__breeding_center.attr

    @property
    def course_suitability(self):
        return self.__course_suitability.attr

    @property
    def distance_suitability(self):
        return self.__distance_suitability.attr

    @property
    def muddy_track_suitability(self):
        return self.__muddy_track_suitability.attr

    @property
    def summer_suitability(self):
        return self.__summer_suitability.attr

    @property
    def winter_suitability(self):
        return self.__winter_suitability.attr
