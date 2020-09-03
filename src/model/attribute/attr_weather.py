# -*- coding: utf-8 -*-
from . import attribute


class Weather(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('天気は晴/曇/雨のいずれかを指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if attr not in ('晴', '曇', '雨'):
            return False

        return True
