from . import attribute


class Weight(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('体重は0以上の整数を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if not isinstance(attr, int):
            return False
        if attr < 0:
            return False

        return True
