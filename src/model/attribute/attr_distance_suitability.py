# -*- coding: utf-8 -*-
from . import attribute
from . import attr_suitability


class DistanceSuitability(attr_suitability.Suitability):
    def _validation_exception(self):
        raise Exception('距離適正は0~1の小数を指定してください')
