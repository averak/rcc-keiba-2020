from . import attribute
from . import attr_id


class TrainerID(attr_id.ID):
    def _validation_exception(self):
        raise Exception('調教師IDは0以上の整数を指定してください')
