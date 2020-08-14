# -*- coding: utf-8 -*-
from . import attribute


class ID(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('IDがNoneです')
        if type(attr) is not int:
            raise Exception('IDは0以上の整数を指定してください')
        if attr < 0:
            raise Exception('IDは0以上の整数を指定してください')
