from . import attribute


class Rank(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('順位は1以上の整数を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if not isinstance(attr, int):
            return False
        if attr < 1:
            return False

        return True
