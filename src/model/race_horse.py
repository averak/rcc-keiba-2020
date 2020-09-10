from . import model


class RaceHorse(model.Model):
    def _hook_create(self, config):
        self.__name = config['name']
        self.__number = config['number']
        self.__rank = config['rank']
        self.__age = config['age']
        self.__load = config['load']
        self.__odds = config['odds']
        self.__weight = config['weight']
        self.__weight_change = config['weight_change']

    @property
    def name(self):
        return self.__name

    @property
    def number(self):
        return self.__number

    @property
    def rank(self):
        return self.__rank

    @property
    def age(self):
        return self.__age

    @property
    def load(self):
        return self.__load

    @property
    def odds(self):
        return self.__odds

    @property
    def weight(self):
        return self.__weight

    @property
    def weight_change(self):
        return self.__weight_change

    @property
    def url(self):
        return 'https://db.netkeiba.com/horse/%s' % self.id
