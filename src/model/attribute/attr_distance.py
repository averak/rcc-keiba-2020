from . import attribute


class Distance(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('走距離は0以上の整数を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if type(attr) is not int:
            return False
        if attr < 0:
            return False

        return True
