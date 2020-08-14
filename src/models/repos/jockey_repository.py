# -*- coding: utf-8 -*-
from . import repository
from .. import jockey


class JockeyRepository(repository.Repository):
    def _restrict(self, data):
        if type(data) is not jockey.Jockey:
            raise Exception('Jockeyオブジェクトを指定してください')

    def _is_match(self, data, id_):
        return data.id == id_
