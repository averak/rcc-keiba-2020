from . import model


class Jockey(model.Model):
    def _hook_create(self, config):
        self.__name = config['name']
        self.__win_rate = config['win_rate']
        self.__rank_average = config['rank_average']

    @property
    def name(self):
        return self.__name.attr

    @property
    def win_rate(self):
        return self.__win_rate.attr

    @property
    def rank_average(self):
        return self.__rank_average.attr
