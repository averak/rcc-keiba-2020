# -*- coding: utf-8 -*-
from . import attribute


class Wins(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('勝数がNoneです')
        if type(attr) is not int:
            raise Exception('勝数は0以上の整数で指定してください')
        if attr < 0:
            raise Exception('勝数は0以上の整数で指定してください')
