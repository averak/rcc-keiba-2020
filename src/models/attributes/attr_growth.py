# -*- coding: utf-8 -*-
from . import attribute


class Growth(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('成長特性がNoneです')
        if type(attr) not in [int, float]:
            raise Exception('成長特性は|0~1 0:早熟 1:晩成|の小数で指定してください')
        if attr < 0 or attr > 1:
            raise Exception('成長特性は|0~1 0:早熟 1:晩成|の小数で指定してください')
