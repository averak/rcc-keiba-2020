from . import model


class Race(model.Model):
    max_horses = 21

    def _hook_create(self, config):
        self.__name = config['name']
        self.__date = config['date']
        self.__weather = config['weather']
        self.__field = config['field']
        self.__turn = config['turn']
        self.__distance = config['distance']
        self.__prize_money = config['prize_money']
        self.__horses = config['horses'][:self.max_horses]

    @property
    def name(self):
        return self.__name.attr

    @property
    def date(self):
        return self.__date.attr

    @property
    def weather(self):
        return self.__weather.attr

    @property
    def field(self):
        return self.__field.attr

    @property
    def turn(self):
        return self.__turn.attr

    @property
    def distance(self):
        return self.__distance.attr

    @property
    def prize_money(self):
        return [money.attr for money in self.__prize_money]

    @property
    def horses(self):
        return self.__horses

    @property
    def n_horses(self):
        return len(self.__horses)

    @property
    def url(self):
        return 'https://race.netkeiba.com/race/shutuba.html?race_id=%s' % self
