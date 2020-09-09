from . import model


class Ped(model.Model):
    def _hook_create(self, config):
        self.__name = config['name']
        self.__win_rate = config['win_rate']
        self.__rank_average = config['rank_average']

    @property
    def name(self):
        return self.__name

    @property
    def win_rate(self):
        return self.__win_rate

    @property
    def rank_average(self):
        return self.__rank_average

    @property
    def url(self):
        return 'https://db.netkeiba.com/horse/ped/%s' % self.id
