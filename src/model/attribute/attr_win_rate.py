# -*- coding: utf-8 -*-
from . import attribute


class WinRate(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('勝率がNoneです')
        if type(attr) not in [int, float]:
            raise Exception('勝率は0~1の小数で指定してください')
        if attr < 0 or attr > 1:
            raise Exception('勝率は0~1の小数で指定してください')
