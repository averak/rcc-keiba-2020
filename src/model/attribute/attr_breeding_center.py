# -*- coding: utf-8 -*-
from . import attribute
from . import attr_name


class BreedingCenter(attr_name.Name):
    def _validation_exception(self):
        raise Exception('産地名は1文字以上の文字列を指定してください')
