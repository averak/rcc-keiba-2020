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
        self.__prize = config['prize']
        self.__horses = config['horses']

    @property
    def name(self):
        return self.__name

    @property
    def date(self):
        return self.__date

    @property
    def weather(self):
        return self.__weather

    @property
    def field(self):
        return self.__field

    @property
    def turn(self):
        return self.__turn

    @property
    def distance(self):
        return self.__distance

    @property
    def prize(self):
        return self.__prize

    @property
    def horses(self):
        return self.__horses

    @property
    def n_horses(self):
        return len(self.__horses)

    @property
    def url(self):
        return 'https://race.netkeiba.com/race/shutuba.html?race_id=%s' % self.id
