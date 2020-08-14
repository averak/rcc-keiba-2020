# -*- coding: utf-8 -*-
from . import repository
from .. import horse


class HorseRepository(repository.Repository):
    def _restrict(self, data):
        if type(data) is not horse.Horse:
            raise Exception('Horseオブジェクトを指定してください')

    def _is_match(self, data, id_):
        return data.id == id_
