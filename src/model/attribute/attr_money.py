# -*- coding: utf-8 -*-
from . import attribute


class Money(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('獲得賞金がNoneです')
        if type(attr) is not int:
            raise Exception('獲得賞金は0以上の整数で指定してください')
        if attr < 0:
            raise Exception('獲得賞金は0以上の整数で指定してください')
