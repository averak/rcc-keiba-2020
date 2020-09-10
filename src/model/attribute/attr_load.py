from . import attribute


class Load(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('斤量は0以上の小数を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if not isinstance(attr, float):
            return False
        if attr < 0:
            return False

        return True
