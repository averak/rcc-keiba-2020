# -*- coding: utf-8 -*-
from . import attribute


class RankAverage(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('順位平均がNoneです')
        if type(attr) not in [int, float]:
            raise Exception('順位平均は1以上の小数で指定してください')
        if attr < 1:
            raise Exception('順位平均は1以上の小数で指定してください')
