# -*- coding: utf-8 -*-
from . import attribute


class Speed(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('速度がNoneです')
        if type(attr) not in [int, float]:
            raise Exception('速度は0以上の小数で指定してください')
        if attr < 0:
            raise Exception('速度は0以上の小数で指定してください')
