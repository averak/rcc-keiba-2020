# -*- coding: utf-8 -*-
from . import attribute


class Weather(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('天気がNoneです')
        if type(attr) not in [int, float]:
            raise Exception('天気は|0: 晴 0.5: 曇 1: 雨|で指定してください')
        if attr not in [0, 0.5, 1]:
            raise Exception('天気は|0: 晴 0.5: 曇 1: 雨|で指定してください')
