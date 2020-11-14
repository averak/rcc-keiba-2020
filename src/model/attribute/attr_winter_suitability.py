from . import attr_suitability


class WinterSuitability(attr_suitability.Suitability):
    def _validation_exception(self):
        raise Exception('冬適正は0~1の小数を指定してください')
