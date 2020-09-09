from . import attribute
from . import attr_suitability


class SummerSuitability(attr_suitability.Suitability):
    def _validation_exception(self):
        raise Exception('夏適正は0~1の小数を指定してください')
