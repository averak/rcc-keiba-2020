# -*- coding: utf-8 -*-
from . import attribute


class Suitability(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('適正は0~1の小数を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if type(attr) not in (int, float):
            return False
        if attr < 0 or attr > 1:
            return False

        return True
