from . import attribute
from . import attr_suitability


class CourseSuitability(attr_suitability.Suitability):
    def _validation_exception(self):
        raise Exception('コース適正は0~1の小数を指定してください')
