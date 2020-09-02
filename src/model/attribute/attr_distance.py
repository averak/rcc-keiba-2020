# -*- coding: utf-8 -*-
from . import attribute


class Distance(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('走距離がNoneです')
        if type(attr) is not int:
            raise Exception('走距離は0以上の整数で指定してください')
        if attr < 0:
            raise Exception('走距離は0以上の整数で指定してください')
