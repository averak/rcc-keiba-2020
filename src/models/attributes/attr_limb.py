# -*- coding: utf-8 -*-
from . import attribute


class Limb(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('脚質特性がNoneです')
        if type(attr) not in [int, float]:
            raise Exception('脚質特性は|0~1 0:逃げ 1:追込|の小数で指定してください')
        if attr < 0 or attr > 1:
            raise Exception('脚質特性は|0~1 0:逃げ 1:追込|の小数で指定してください')
