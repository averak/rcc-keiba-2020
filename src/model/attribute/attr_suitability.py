# -*- coding: utf-8 -*-
from . import attribute


class Suitability(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('適正がNoneです')
        if type(attr) not in [int, float]:
            raise Exception('適正は0~1の小数で指定してください')
        if attr < 0 or attr > 1:
            raise Exception('適正は0~1の小数で指定してください')
