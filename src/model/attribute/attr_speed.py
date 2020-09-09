from . import attribute


class Speed(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('速度は0以上の小数を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if type(attr) not in (int, float):
            return False
        if attr < 0:
            return False

        return True
