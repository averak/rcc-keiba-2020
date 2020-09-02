# -*- coding: utf-8 -*-
from . import attribute
from . import attr_suitability


class MuddyTrackSuitability(attr_suitability.Suitability):
    def _validation_exception(self):
        raise Exception('重馬場適正は0~1の小数を指定してください')
