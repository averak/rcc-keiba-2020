from . import attribute


class WeightChange(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('体重は整数を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if not isinstance(attr, int):
            return False

        return True
