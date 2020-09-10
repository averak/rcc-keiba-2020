from . import attribute


class Odds(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('オッズは0以上の小数を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if not isinstance(attr, float):
            return False
        if attr < 0:
            return False

        return True
