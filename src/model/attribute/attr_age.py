from . import attribute


class Age(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('年齢は0以上の整数を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if not isinstance(attr, int):
            return False
        if attr < 0:
            return False

        return True
