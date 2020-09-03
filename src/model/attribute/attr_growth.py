# -*- coding: utf-8 -*-
from . import attribute


class Growth(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('成長特性は0以上の整数を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if type(attr) not in (int, float):
            return False
        if attr < 0 or attr > 1:
            return False

        return True
